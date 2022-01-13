import pandas as pd
import pymysql
import json
import cv2

ip = "192.168.1.17"
port = 13307
user = "acryl"
pw = "acryl00"
db = "MARKER"
tablename = 'THANQ'
charset="utf8"


def select_data(tablename): #DB 통해서, 값을 가져오는 함수
    conn = pymysql.connect(host=ip, user=user, passwd=pw,db=db,charset=charset,port=port)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = f'SELECT * FROM {tablename} where user_id !=6;' #6번 아이디는 제외한다.        
    cursor.execute(sql)
    # rows = list()
    rows = cursor.fetchall()
    # rows.append(row)
    result = pd.DataFrame(rows)
    return result

origin_data = select_data(tablename)

copy_data=origin_data.copy()
copy_data=copy_data.drop_duplicates(["file_name"],keep="first")

print(type(origin_data))
print(origin_data.keys())
#Index(['id', 'file_name', 'x1', 'x2', 'y1', 'y2', 'type', 'createdAt',
#        'encrypt_id', 'maker_id', 'file_id', 'user_id', 'seq_no', 'maker'],
#       dtype='object')

# print(type(list(origin_data["file_name"])))
v=list(origin_data["file_name"])
# print((list(origin_data["file_name"])[:10]))

cnt=0
values = []
for i, file in enumerate(v[:-1]) :#0~ 직전
    if file == v[i+1]:
        values.append(file)
        cnt+=1

p=origin_data["file_name"].isin(values) 

# f=origin_data[p & origin_data["seq_no"].isin([1])]
f=origin_data[p]

print(f)

print(len(f))

f.to_csv(f"/home/con/mmdetection/doing_code/t.csv") #"/mnt/sdb/AI/save_csv/" 에 저장됩니다.


# with open("t.json","w") as file:
#     json.dump(f,file)