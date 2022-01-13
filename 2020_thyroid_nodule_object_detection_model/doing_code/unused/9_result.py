import numpy as np
import pickle
import json
import cv2
import datetime
import pandas as pd
import copy
import os
import math


list_maker_names = ["no_name","Samsung-RS80A","Samsung-RS85","Alpinion-Diamond","Alpinion-platinum","Samsung-60","Philips","GE","etc","Siemens"]
list_nodule_names = ["none","Benign:양성","FA:여포선종","FTC:여포암","PTC:유두암","Cat2:양성","Cat5:악성의심","Cat6:악성","C_Benign","C_Malign"]

def createFolder(directory):#폴더 생성 함수
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#당일 날짜 시간 추출
year_month_day,times=date[:8],date[8:]

file_path="/home/con/mmdetection/data/thyroid/"#이미지, json 파일 위치
test_result_image_path=f"/mnt/sdb/AI/work/test_result_image/{year_month_day}/"#결과 이미지 파일 저장 위치
test_json_path="/home/con/mmdetection/data/thyroid/annotations/"#어노테이션 저장 위치
img_path="/home/con/mmdetection/data/thyroid/preprocess/"#전처리 파일 위치
compare_image_path=test_result_image_path+"/compare_image/"#진짜 bbox 만 처리된 이미지 위치
img_load_path = "/mnt/sdb/AI/work/save_img/"#

#색 지정

dict_makers  = dict()
for i in range(10):
    dict_makers[i]=[[0,0],[0,0],[0,0]]
    
dict_nodules = dict()
for i in range(10):
    dict_nodules[i]=[[0,0],[0,0],[0,0]]
    
dict_nodule_maker_ids = dict()
for i in range(10):#제품군별
    dict_nodule_maker_ids[i]=dict()
    for j in range(10):##결절별
        dict_nodule_maker_ids[i][j]=[[0,0],[0,0],[0,0]]

        
with open(f"{file_path}/outfile.json","r") as file:
    test_result = json.load(file)#test 돌린 뒤 결과값

df = pd.DataFrame(test_result)
df.to_csv(f"{file_path}test.csv")#test 실행 값을 csv로 저장

with open(f"{test_json_path}/test.json","r") as file:#의사분들이 체크해준 값
    json_data = json.load(file)    

print("len(json_data['images'])")
print(len(json_data['images']))

json_image_data = json_data["images"]#의사 분들이 주신 값 중에서 images 파트만 분리

data ={"file_name":[],"img_label":[],"nodule":[],"maker":[],"label_predict":[],"prob_predict":[]}
df = pd.DataFrame(data)


def intersection_over_union(box1, box2):#IoU 계산하는 함수
    # print(f"box1:{box1},box2:{box2}")
    x1 = max(box1[0][0], box2[0][0])
    y1 = max(box1[0][1], box2[0][1])
    x2 = min(box1[1][0], box2[1][0])
    y2 = min(box1[1][1], box2[1][1])
    
    area_intersection = (x2 - x1) * (y2 - y1)
    area_box1 = (box1[1][0] - box1[0][0]) * (box1[1][1] - box1[0][1])
    area_box2 = (box2[1][0] - box2[0][0]) * (box2[1][1] - box2[0][1])
    area_union = area_box1 + area_box2 - area_intersection    

    iou = area_intersection / area_union
    return iou

# print('json_data["annotations"]')
# print(len(json_data["annotations"]))#5560
# print(json_data["annotations"][0:2])
# print()

def result(i,v,check_count,df):#basis <- 양성, 악성에 대한 확률 기준값
    global dict_makers
    global dict_nodules
    # print()
    # print(f"--{i+1}--")
    file_name=json_image_data[i]["file_name"]#파일 이름 분리
    print(f"{i}, file_name:{file_name}")

    split_values=file_name.split(".")#확장자랑 분류
    name,format0=file_name[:-(len(split_values[-1])+1)],split_values[-1]#파일이름, 확장자
    
    height=json_image_data[i]["height"]#높이
    width=json_image_data[i]["width"]#너비
    # print(height,width)
    img_id = json_image_data[i]["id"]#id 값
    maker_id = json_image_data[i]["maker_id"]

    # print(img_path+file_name)
    img_info={"file_name":file_name,"label":-1,"nodule":-1,"maker":maker_id}
    predict_info={"file_name_predict":file_name,"label_predict":-1,"prob_predict":-1}
    predict_list=[]
    
    for anno in json_data["annotations"]:#실제 데이터의 어노테이션 데이터 가져옴
        if anno["image_id"]==img_id:
            
            nodule = anno["tirads"]
            thyroid_type=anno["category_id"]#1 or 2
            if img_info["label"]==1:
                pass
            else:    
                img_info={"file_name":file_name,"label":thyroid_type-1,"nodule":nodule,"maker":maker_id}
            # print("v")
            # print(v[0])
            # print(v[1])
            max_prob=-1
            if len(v[1])>=1:
                for value in v[1]:
                    if max_prob<value[-1]:
                        max_prob=value[-1]
                if max_prob>0.5:
                    label_predict=1
            if len(v[0])>=1 and max_prob<=0.5:
                for value in v[0]:
                    if max_prob<value[-1]:
                        max_prob=value[-1]
                label_predict=0
            try:
                if max_prob>0.5:
                    predict_info={"file_name_predict":file_name,"label_predict":label_predict,"prob_predict":max_prob}
            except:
                predict_info={"file_name_predict":file_name,"label_predict":-1,"prob_predict":-1}
                
            predict_list.append(predict_info)
    

    if len(predict_list)==0:
        pass
    elif len(predict_list)==1:
        predict_info=predict_list[0]
    else:
        for predict in predict_list:
            if predict["label_predict"]==1:
                predict_info=predict
                break
            elif predict==predict_list[-1]:
                predict_info=predict
                
    if predict_info["label_predict"] !=1 and  predict_info["label_predict"] !=0:
        print(i)
        print("img_info")
        print(img_info)
        print("predict_info")
        print(predict_info)
    
    if img_info["label"]==predict_info["label_predict"]:
        check_count[0]+=1
    else:
        check_count[-1]+=1
    
    # print("df.keys()")
    # print(list(df.keys()))#['index', 'file_name', 'img_label', 'img_nodule', 'file_name_predict', 'label_predict', 'prob_predict']


    # print("df['index']")
    # print(df['index'])
    
    series = pd.Series([img_info["file_name"],str(img_info["label"]),str(img_info["nodule"]),str(img_info["maker"]),str(predict_info["label_predict"]),predict_info["prob_predict"]],index=["file_name","img_label","nodule","maker","label_predict","prob_predict"])
    
    df=df.append(series,ignore_index=True)
    
    # print("series")
    # print(series)
    # print("--df--")
    # print(df)
    
    # df['file_name'].append(img_info["file_name"])
    # df['img_label'].append(img_info["label"])
    # df['img_nodule'].append(img_info["nodule"])
    # df['file_name_predict'].append(i)
    # df['label_predict'].append(i)
    # df['prob_predict'].append(i)

    # for key in df.keys():
    #     df[key]
    return df,check_count


check_count = [0,0]

for i,v in enumerate(test_result[:]): #모든 예측값에 대해서 가져온다.
    # print(i,len(v[0]),len(v[1]))
    df,check_count=result(i,v,check_count,df)
    
    print(f"check_count:{check_count}")

print(df)
save_csv="/home/con/mmdetection/data/thyroid/result_csv/"#db데이터 가져온 정보, csv로 저장되는 폴더(6번은 제외한다.)

num=input("몇번 testset인가??")
df.to_csv(f"{save_csv}df{num}.csv")