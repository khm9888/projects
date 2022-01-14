import pandas as pd
import pymysql
import json
import cv2
import datetime
import math
import numpy as np

# choice = input("전체 모두 검색하시겠습니까?(y or yes/n)")
# print(pymysql.__version__)

ip = "192.168.1.17"
port = 13307
user = "acryl"
pw = "acryl00"
db = "MARKER"
tablename = 'THANQ'
charset="utf8"

# code_data_path=__file__[:len(__file__)-len(__file__.split("/")[-1])] #현재 파일의 폴더 위치
choice = input("전체 모두 검색하시겠습니까?(y or yes/n)")


path="/mnt/sdb/AI/data/"
# path="/mnt/sdb/AI/work/preprocess/"
save_csv="/mnt/sdb/AI/work/save_csv/"#db데이터 가져온 정보, csv로 저장되는 폴더(6번은 제외한다.)
save_json="/mnt/sdb/AI/work/save_json/"
save_txt_path = "/mnt/sdb/AI/work/record_txt/"
result_json_path="/mnt/sdb/AI/work/working_result/"
result_csv_path=result_json_path

date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#
year_month_day,times=date[:8],date[8:]

def select_data(tablename): #DB 통해서, 값을 가져오는 함수
    conn = pymysql.connect(host=ip, user=user, passwd=pw,db=db,charset=charset,port=port)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # sql = f'SELECT * FROM {tablename} where user_id !=6;' #6번 아이디는 제외한다.        
    sql = f'SELECT * FROM {tablename} where user_id !=6 and maker_id in (0,1,2,5,6,8,9);'      
    cursor.execute(sql)
    # rows = list()
    rows = cursor.fetchall()
    # rows.append(row)
    result = pd.DataFrame(rows)
    return result

origin_data = select_data(tablename)
# print(origin_data.keys()) #Index(['id', 'file_name', 'x1', 'x2', 'y1', 'y2', 'type', 'user_id'], dtype='object')

origin_data.to_csv(f"{save_csv}{year_month_day}_{times}.csv") #"/mnt/sdb/AI/save_csv/" 에 저장됩니다.

origin_data.to_csv(f"{save_csv}from_db.csv") #"/mnt/sdb/AI/save_csv/" 에 저장됩니다.


copy_data=origin_data.copy()
copy_data=copy_data.drop_duplicates(["file_name"],keep="first")#중복 이미지 제거

dict_type=dict() #타입별 개수 거르기
dict_id=dict() #아이디별, 사용자 
dict_date=dict()
dict_maker=dict()
list_maker_names = ["no_name","Samsung-RS80A","Samsung-RS85","Alpinion-Diamond","Alpinion-platinum","Samsung-60","Philips","GE","etc","Siemens"]

for i in range(10):
    dict_maker[i]=0
 
base=dict() #json 만들기 위한 기본 딕셔너리 구조
base["images"]=list()
base["annotations"]=list()
base["categories"]=list()

rm_nums=list()

for n in range(0,len(copy_data)):
    dict_images=dict()
    order =copy_data.iloc[n]['id']#38
    file_name =copy_data.iloc[n]["file_name"] #1.png
    bbox =[int(copy_data.iloc[n]["x1"]), int(origin_data.iloc[n]["y1"]),int(origin_data.iloc[n]["x2"])-int(origin_data.iloc[n]["x1"]),int(origin_data.iloc[n]["y2"])-int(origin_data.iloc[n]["y1"])]
    thyroid_type=int(copy_data.iloc[n]["type"])
    user_id=int(copy_data.iloc[n]["user_id"])
    encrypt_id=copy_data.iloc[n]["encrypt_id"]
    createdat=copy_data.iloc[n]["createdAt"]
    maker_id=copy_data.iloc[n]["maker_id"]

    image =cv2.imread(f"{path}{file_name}")
    try:
        height,width,_ = image.shape
    except:
        print(file_name)
    dict_images["file_name"]=file_name
    dict_images["height"]=height
    dict_images["width"]=width
    dict_images["user_id"]=user_id
    dict_images["encrypt_id"]=encrypt_id
    dict_images["createdat"]=createdat
    dict_images["maker_id"]=int(maker_id)
    
    # for d in dict_images.values():
    #     print(d)
    #     print(type(d))

    is_filter_name = copy_data["file_name"]==dict_images["file_name"]
    img_id=int(copy_data[is_filter_name]["id"])
    dict_images["id"]=img_id
    

    dict_maker[maker_id]+=1

    base["images"].append(dict_images.copy())
for n in range(0,len(origin_data)):
# for n in range(0,2):
    # for n in range(1,2+1):
    # try:
    # print(f"order:{order}")

    dict_images=dict()
    order =origin_data.iloc[n]['id']#38
    file_name =origin_data.iloc[n]["file_name"] #1.png
    bbox =[int(origin_data.iloc[n]["x1"]), int(origin_data.iloc[n]["y1"]),int(origin_data.iloc[n]["x2"])-int(origin_data.iloc[n]["x1"]),int(origin_data.iloc[n]["y2"])-int(origin_data.iloc[n]["y1"])]
    thyroid_type=int(origin_data.iloc[n]["type"])
    user_id=int(origin_data.iloc[n]["user_id"])
    seq_no=origin_data.iloc[n]["seq_no"]
    createdat=origin_data.iloc[n]["createdAt"]
    # if len(dict_date)==0:
    #     dict_date[createdat[:10]]":[0,0,0,0,0,0]}

    if thyroid_type in [1,2,5,8]:#양성인 케이스 1,2,5,8번만 tag 1
        tag=1
    elif thyroid_type in map(int,list(range(1,9+1))):#1~9
        tag=2
    else:
        tag=0 #예외의 케이스에 확인하기

    if thyroid_type in dict_type:#thyroid_type
        dict_type[thyroid_type]+=1
    else:
        dict_type[thyroid_type]=1
        
    if user_id in dict_id:
        dict_id[user_id]+=1
    else:
        dict_id[user_id]=1
        
    if createdat[:10] in dict_date:
        dict_date[createdat[:10]][0]+=1
    else:
        dict_date[createdat[:10]]=[1,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10]
    dict_date[createdat[:10]][user_id][thyroid_type]+=1
    
    is_filter_name = copy_data["file_name"]==file_name
    img_id=int(copy_data[is_filter_name]["id"])
    
    annotation_dict=dict()
    annotation_dict["area"]=bbox[2]*bbox[3]
    annotation_dict["iscrowd"]=0

    annotation_dict["image_id"]=img_id
    annotation_dict["bbox"]=bbox
    annotation_dict["tirads"]=thyroid_type
    annotation_dict["category_id"]=tag
    annotation_dict["id"]=int(img_id*10+seq_no)#revise

    base["annotations"].append(annotation_dict)
    # except:
    #     rm_nums.append(order)
    #     continue
    
# print(rm_nums)

# for a in base:
#     for b in base[a]:
#         for c,d in b.items():
#             print(c,d,type(d))


with open("/home/con/mmdetection/data/thyroid/annotations/tirads_classification.txt","r") as file:
    lines=file.readlines()
    for line in lines:
        line=line.strip().split(":")
        tag=int(line[0].strip())
        categories_dict=dict()
        categories_dict["id"]=tag
        categories_dict["name"]=line[1].strip()
        base["categories"].append(categories_dict)


with open("/home/con/mmdetection/data/thyroid/annotations/from_db.json","w") as json_file:
    json.dump(base,json_file)
with open(f"{save_json}{year_month_day}_{times}.json","w") as json_file:
    try:
        json.dump(base,json_file)
    except:
        print(json_file)

with open(f"{save_txt_path}{year_month_day}_{times}.txt","w") as file:

    print("dict_type")
    print(dict_type)

    print("dict_id")
    print(dict_id)

    print("dict_maker")
    # print(dict_maker)
    sum_maker = 0
    for i in dict_maker.values():
        sum_maker+=i
    for i in range(len(dict_maker)):
        print(f"{i}-{list_maker_names[i]:20s} : {dict_maker[i]:>5d}({dict_maker[i]*100/sum_maker:.2f}%)")

    file.write("dict_type\n")
    file.write(f"{dict_type}\n")
    file.write("dict_id\n")
    file.write(f"{dict_id}\n")
    file.write("dict_maker\n")
    for i in range(len(dict_maker)):
        file.write(f"{i}-{list_maker_names[i]:20s} : {dict_maker[i]:>5d}({dict_maker[i]*100/sum_maker:.2f}%)\n")
    
    days = []
    calendars = dict()

    ###################################### 월마다 작성######################################
    start_day = 23 #데이터 가져오는 첫날
    end_day = 30
    calendars[9]=list(range(start_day,end_day+1))#9월 시작일/끝일
    ###################################### 월마다 작성######################################
    ###################################### 월마다 작성######################################
    start_day = 1 #데이터 가져오는 첫날
    # end_day = 4
    end_day = 31
    calendars[10]=list(range(start_day,end_day+1))#10월 시작일/끝일
    ###################################### 월마다 작성######################################
    ###################################### 월마다 작성######################################
    start_day = 1 #데이터 가져오는 첫날
    end_day = 30
    # end_day = int(year_month_day[-2:])#이미 만들어진 변수로, 당일 날짜 가져올 수 있게 처리했습니다.
    calendars[11]=list(range(start_day,end_day+1))#11월 시작일/끝일
    ###################################### 월마다 작성######################################
    ###################################### 월마다 작성######################################
    start_day = 1 #데이터 가져오는 첫날
    # end_day = 4
    end_day = int(year_month_day[-2:])#이미 만들어진 변수로, 당일 날짜 가져올 수 있게 처리했습니다.
    calendars[12]=list(range(start_day,end_day+1))#12월 시작일/끝일
    ###################################### 월마다 작성######################################

    for month,day_list in calendars.items():
        for day in day_list:
            days.append(f"2020-{month:02d}-{day:02d}")
            
    print(days)
    print("dict_date")

    total=0

    file.write(f"days\n")
    file.write(f"{days}\n")
    file.write(f"dict_date\n")
    
    if choice =="y" or choice == "yes":
        pass
    else:
        days = days[-5:]

    for day in days:
        try:
            total+=dict_date[day][0]
            print("-"*20)
            file.write("-"*20+"\n")
            file.write(f"working for {day} : {dict_date[day][0]}\n")
            
            print(f"working for {day} : {dict_date[day][0]}")
            for number in [1,2,3,5]:
                s = sum(dict_date[day][number][1:])
                if s!=0:
                    print(f"{number}번 : {dict_date[day][number][1:]}, 합: {s}")
                    file.write(f"{number}번 : {dict_date[day][number][1:]}, 합: {s}\n")
            print("-"*20)
            file.write("-"*20+"\n")
        except:
            print("-"*20)
            print(f"{day}은 없습니다!")
            print("-"*20)
            file.write("-"*20+"\n")
            file.write(f"{day}은 없습니다!\n")
            file.write("-"*20+"\n")
    dict_date["total"]=total

    print(f"total count( {days[0]} ~ {days[-1]} ) : {dict_date['total']}")
    print(f"이미지의 개수는 {len(copy_data)}입니다.")
    file.write(f"total count( {days[0]} ~ {days[-1]} ) : {dict_date['total']}\n")
    file.write(f"이미지의 개수는 {len(copy_data)}입니다.\n")
    file.write("-"*20+"\n")

df = pd.DataFrame(dict_date)

df.to_csv(f"{result_csv_path}{date[:8]}_{date[8:10]}.csv")

with open(f"{result_json_path}{date[:8]}_{date[8:10]}.json","w") as file:
    json.dump(dict_date,file)
    
