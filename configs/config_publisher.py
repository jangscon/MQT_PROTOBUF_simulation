from datetime import datetime

broker = '' # string type
port = 0 # integer type
mtype = '' # string type
username = '' # string type
password = '' # string type
reference_timestamp = datetime.strptime("2020-09-01 00:00:00.551000", "%Y-%m-%d %H:%M:%S.%f")
previous_timestamp = datetime.strptime("2020-09-01 00:00:00.551000", "%Y-%m-%d %H:%M:%S.%f")

debugging = False # True일때 publish 안함 (디버깅용)
logging = False # True일때 로그파일로 저장
streaming_protobuf = True # True일때 protobuf 사용