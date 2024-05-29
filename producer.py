import hobit_pb2
import sys
from configs.config_producer import type_dict, test_dict, swapkeys


def typeConverter(value, dtype):
    return value if type(value) == dtype else dtype(value)

def swapDictionaryKey(key,swapkeys):
    return swapkeys[key] if key in list(swapkeys.keys()) else key
    
def dictToTransport(rawdict, tofile=None, tostream=None):
    transport_msg = hobit_pb2.Transport()
    for k, v in rawdict.items():
        key = swapDictionaryKey(k,swapkeys)
        value = typeConverter(v,type_dict[key])
        setattr(transport_msg, key, value) 
    if tofile:
        with open(tofile, "wb") as f:
            f.write(transport_msg.SerializeToString())
    if tostream:
        return transport_msg.SerializeToString()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 producer.py PROTOBUF_BIN_FILE")
        sys.exit(-1)

    save_path = sys.argv[1]
    dictToTransport(test_dict, save_path)