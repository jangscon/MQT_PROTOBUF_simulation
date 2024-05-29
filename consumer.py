import hobit_pb2
import sys

def printMsg(msgdict) :
    print("="*85)
    print(f"{' key':<15}|{' value':<50}| data type")
    print("="*85)
    for k, v in msgdict.items():
        print(f"{k:<15}|{v:<50}|({type(v)})")
    print("="*85)

def getTransMsg(tran_obj):
    trans_msg = dict()
    trans_msg["index"] = tran_obj.index
    trans_msg["blk_no"] = tran_obj.blk_no 
    trans_msg["press3"] = tran_obj.press3 
    trans_msg["calc_press2"] = tran_obj.calc_press2 
    trans_msg["press4"] = tran_obj.press4 
    trans_msg["calc_press1"] = tran_obj.calc_press1 
    trans_msg["calc_press4"] = tran_obj.calc_press4 
    trans_msg["calc_press3"] = tran_obj.calc_press3
    trans_msg["bf_gps_lon"] = tran_obj.bf_gps_lon
    trans_msg["gps_lat"] = tran_obj.gps_lat
    trans_msg["speed"] = tran_obj.speed
    trans_msg["in_dt"] = tran_obj.in_dt
    trans_msg["move_time"] = tran_obj.move_time
    trans_msg["dvc_id"] = tran_obj.dvc_id
    trans_msg["dsme_lat"] = tran_obj.dsme_lat
    trans_msg["press1"] = tran_obj.press1
    trans_msg["press2"] = tran_obj.press2
    trans_msg["work_status"] = tran_obj.work_status
    trans_msg["timestamp"] = tran_obj.timestamp
    trans_msg["is_adjust"] = tran_obj.is_adjust
    trans_msg["move_distance"] = tran_obj.move_distance
    trans_msg["weight"] = tran_obj.weight
    trans_msg["dsme_lon"] = tran_obj.dsme_lon
    trans_msg["in_user"] = tran_obj.in_user
    trans_msg["eqp_id"] = tran_obj.eqp_id
    trans_msg["blk_get_seq_id"] = tran_obj.blk_get_seq_id
    trans_msg["lot_no"] = tran_obj.lot_no
    trans_msg["proj_no"] = tran_obj.proj_no
    trans_msg["gps_lon"] = tran_obj.gps_lon
    trans_msg["seq_id"] = tran_obj.seq_id
    trans_msg["bf_gps_lat"] = tran_obj.bf_gps_lat
    trans_msg["blk_dvc_id"] = tran_obj.blk_dvc_id

    return trans_msg

def getTransportObj(file_paths):
    trans_obj = hobit_pb2.Transport()
    with open(file_paths, "rb") as f:
        trans_obj.ParseFromString(f.read())
    return trans_obj


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 consumer.py PROTOBUF_BIN_FILE")
        sys.exit(-1)
    
    rawfile_path = sys.argv[1]
    transport_obj = getTransportObj(rawfile_path)
    transport_msg = getTransMsg(transport_obj)
    # for debug
    printMsg(transport_msg)
    


    
