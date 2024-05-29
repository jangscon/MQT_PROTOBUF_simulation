# Protobuf Serialization to MQTT and Kafka Example

## How to Install Protobuf

1. Download the file from [protobuf releases](https://github.com/protocolbuffers/protobuf/releases) based on your CPU architecture.
    1.1. For Rasp4:
        ```bash
        $ curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v27.0/protoc-27.0-linux-aarch_64.zip
        ```
    1.2. For Scouter:
        ```bash
        $ curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v27.0/protoc-27.0-linux-x86_64.zip
        ```
2. Unzip the downloaded file:
    ```bash
    $ unzip [downloaded zip file] -d protoc3
    ```
3. Move the files and change ownership based on your environment:
    3.1. For Rasp4:
        ```bash
        $ sudo mv protoc3/bin/* /usr/bin/
        $ sudo mv protoc3/include/* /usr/include/
        $ sudo chown $USER /usr/bin/protoc
        $ sudo chown -R $USER /usr/include/google
        ```
    3.2. For Scouter:
        ```bash
        $ sudo mv protoc3/bin/* /home/scouter/anaconda3/bin/
        $ sudo mv protoc3/include/* /home/scouter/anaconda3/include/
        $ sudo chown $USER /home/scouter/anaconda3/bin/protoc
        $ sudo chown -R $USER /home/scouter/anaconda3/include/google
        ```
4. Install the Protobuf Python package:
    ```bash
    $ pip3 install --upgrade protobuf  # Version 5.27.0
    ```

## Running the Publisher

1. Modify `configs/config_producer.py`:
    - Write the column names and their data types of the CSV in `type_dict`.
2. Update the MQTT connection information in `configs/config_producer.py`.
3. Place the CSV file in the current directory before running the script:
    - Example: `transport_201.csv`
4. Execute `send_tramsport_sensor_simulation`:
    4.1. Running individually:
        ```bash
        $ python3 send_tramsport_sensor_simulation.py [eqp_id]
        ```
    4.2. External execution:
        - Prepare the CSV file and modify the config files as needed.
