import pandas as pd
import glob
from datetime import datetime
import time
import paho.mqtt.client as mqtt
import sys
import simplejson
import os
import threading  # Import threading for concurrent operations

import configs.config_publisher as sconfig
from producer import *

class CsvToProtobufMqttPublisher:
    def __init__(self):
        self.broker = sconfig.broker
        self.port = sconfig.port
        self.mtype = sconfig.mtype
        self.username = sconfig.username
        self.password = sconfig.password
        self.reference_timestamp = sconfig.reference_timestamp
        self.previous_timestamp = sconfig.previous_timestamp
        
        self.debugging = sconfig.debugging
        self.logging = sconfig.logging
        self.streaming_protobuf = sconfig.streaming_protobuf
        
        self.eqp_id = sys.argv[1]
        self.mqtt_topic = f'{self.mtype}/{self.eqp_id}'
        self.logpath = f"./logs/log_{self.mtype}{self.eqp_id}_{int(time.time())}.txt"

    def calculate_delays_adjacent(self, file):
        for chunk in pd.read_csv(file, chunksize=10000, low_memory=True, engine='python'):
            if 'timestamp' not in chunk.columns:
                raise KeyError("The column 'timestamp' is not found in the CSV file", chunk.columns)

            chunk['timestamp'] = pd.to_datetime(chunk['timestamp'], errors='coerce')
            chunk = chunk.sort_values(by='timestamp').reset_index(drop=True)
            
            for row in chunk.itertuples(index=False):
                delay = row.timestamp - self.previous_timestamp
                # Ensure row data is serializable
                row_dict = row._asdict()
                row_dict['timestamp'] = row_dict['timestamp'].isoformat() if row_dict['timestamp'] is not None else None
                # Convert the entire row dictionary to JSON
                if self.streaming_protobuf:
                    row_base64 = dictToTransport(row_dict, tostream=True)
                    yield row_base64, delay.total_seconds()
                else :
                    yield simplejson.dumps(row_dict, ignore_nan=True), delay.total_seconds()
                self.previous_timestamp = row.timestamp

    def process_and_send_messages(self, client):
        csv_files = glob.glob(f"transport_{self.eqp_id}.csv")
        for file in csv_files:
            for msg, delay in self.calculate_delays_adjacent(file):
                time.sleep(delay)  # Wait for the specified delay before sending the message
                if not self.debugging :
                    client.publish(self.mqtt_topic, msg)
                if self.logging :
                    with open(self.logpath,"a") as f:
                        f.write(f"{msg} \n")
                        f.write("========================================\n")

    def run_producer(self):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code "+str(rc))
            client.subscribe("control/start")

        def on_message(client, userdata, message):
            if message.topic == "control/start" and message.payload.decode() == "start":
                client.unsubscribe("control/start")  # Unsubscribe from the start command topic
                # Create and start a thread to process and send messages
                thread = threading.Thread(target=self.process_and_send_messages, args=(client,))
                thread.start()

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.username_pw_set(self.username, self.password)
        client.connect(self.broker, self.port, 60)
        client.loop_forever()


if __name__ == "__main__":
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if len(sys.argv) < 2:
        print("Usage: python3 send_tramsport_sensor_simulation.py <eqp_id>")
        sys.exit(1)
    
    mqtt_publisher = CsvToProtobufMqttPublisher()
    mqtt_publisher.run_producer()

