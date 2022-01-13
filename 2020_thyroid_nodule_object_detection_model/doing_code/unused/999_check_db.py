import pandas as pd
import pymysql
import json
import cv2
import datetime

# print(pymysql.__version__)

ip = "192.168.1.17"
port = 13307
user = "acryl"
pw = "acryl00"
db = "MARKER"
tablename = 'THANQ'
charset="utf8"

mmdetection_path="/home/con/"
path="/mnt/sdb/AI/data/"
# path="/mnt/sdb/AI/work/preprocess/"
save_json="/mnt/sdb/AI/work/save_json/"
result_json_path="/mnt/sdb/AI/work/working_result/"
save_txt_path = "/mnt/sdb/AI/work/record_txt/"
result_csv_path=result_json_path

save_csv="/home/con/mmdetection/data/thyroid/"

date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#
year_month_day,times=date[:8],date[8:]

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
# print(origin_data.keys()) #Index(['id', 'file_name', 'x1', 'x2', 'y1', 'y2', 'type', 'user_id'], dtype='object')

def divide(origin_data):
    copy_data_2=origin_data.copy()
    copy_data_2["date_encrypt"]=copy_data_2["createdAt"].str[:10]+"-----"+copy_data_2["encrypt_id"]
    copy_data_2=copy_data_2.drop_duplicates(["date_encrypt"],keep="first")#중복 이미지 제거
    filter_csv=copy_data_2.groupby("encrypt_id").count()
    indexes = filter_csv.index
    # print(indexes)
    count_dict=dict()
    for index_o in indexes[:]:
        v=filter_csv.loc[index_o]
        cnt=v["id"]
        if cnt in count_dict:
            print("case1")
            print(cnt)
            print(index_o)
            count_dict[cnt].append(index_o)
        else:
            print("case2")
            print(cnt)
            print(index_o)
            count_dict[cnt]=[index_o]
    # print(count_dict)
    # print(len(count_dict[1]))
    # print(len(count_dict[2]))
    # print(len(count_dict[3]))
    # 263
    # 58
    # 2
    return count_dict

count_dict_1 = divide(origin_data)[1]

origin_data.to_csv(f"{save_csv}/filter/{year_month_day}_{times}.csv") #"/mnt/sdb/AI/save_csv/" 에 저장됩니다.
