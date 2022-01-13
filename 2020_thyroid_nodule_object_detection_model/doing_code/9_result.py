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

tb_path=test_result_image_path+"/tb/"
tm_path=test_result_image_path+"/tm/"
fm_path=test_result_image_path+"/fm/"
fb_path=test_result_image_path+"/fb/"
ob_path=test_result_image_path+"/ob/"
om_path=test_result_image_path+"/om/"

createFolder(test_result_image_path)
createFolder(compare_image_path)
createFolder(tb_path)
createFolder(fm_path)
createFolder(ob_path)
createFolder(tm_path)
createFolder(fb_path)
createFolder(om_path)

#색 지정

blue_color = (255, 0, 0) #BGR
red_color = (0, 0, 255)
benign_color=(0,255,0)#녹색
malign_color=(255,0,255)# 자주,보라
white_color = (255, 255, 255)


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

data ={"file_name":[],"img_label":[],"nodule":[],"maker":[],"label_predict":[],"prob_predict":[]}
df2 = pd.DataFrame(data)
        
        
with open(f"{file_path}/outfile.json","r") as file:
    test_result = json.load(file)#test 돌린 뒤 결과값

df = pd.DataFrame(test_result)
df.to_csv(f"{file_path}test.csv")#test 실행 값을 csv로 저장

with open(f"{test_json_path}/test.json","r") as file:#의사분들이 체크해준 값
    json_data = json.load(file)    

print("len(json_data['images'])")
print(len(json_data['images']))

json_image_data = json_data["images"]#의사 분들이 주신 값 중에서 images 파트만 분리

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

def result(i,v,count_values,basis,threshold,df2):#basis <- 양성, 악성에 대한 확률 기준값
    global dict_makers
    global dict_nodules
    # print()
    # print(f"--{i+1}--")
    file_name=json_image_data[i]["file_name"]#파일 이름 분리
    print(f"{i}, file_name:{file_name}")



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
            img_info={"file_name":file_name,"label":thyroid_type-1,"nodule":nodule,"maker":maker_id}
            
            # if img_info["label"]==1:
            #     pass
            # else:    
            #     img_info={"file_name":file_name,"label":thyroid_type-1,"nodule":nodule,"maker":maker_id}
            
            values=anno["bbox"]
            if thyroid_type==1:#benign
                predict_list=[]
                precision_max=0
                iou=0
                predict=0
                true=0
                # print("case1,benign")
                color = blue_color
                box1 = ((values[0], values[1]),(values[0]+values[2], values[1]+values[3]))

                if len(v[0])!=0:#benign 남아 있다면
                    color = benign_color
                    array = v[0]
                    for values in array:
                        values[:4] = list(map(int, values))[:4]
                        precision=values[4]
                        if precision>basis:
                            box2= ((values[0],values[1]),(values[2],values[3]))

                            iou=intersection_over_union(box1, box2)
                            if iou>threshold:
                                predict_list.append((precision,iou,1,1))
                if len(v[1])!=0:#malign 남아 있다면
                    color = malign_color
                    array = v[1]
                    for values in array:
                        values[:4] = list(map(int, values))[:4]
                        precision=values[4]
                        if precision>basis:
                            box2= ((values[0],values[1]),(values[2],values[3]))
                            iou=intersection_over_union(box1, box2)

                            if iou>threshold:
                                predict_list.append((precision,iou,2,1))

                if len(predict_list)>=1:
                    for precision_p,iou_p,predict_p,true_p in predict_list:
                        if precision_max<precision_p:
                            precision_max=precision_p
                            iou=iou_p
                            predict=predict_p
                            true = true_p
                # print(f"predict_value:{precision_max,iou,predict}")
                if predict==0:# Zero Benign
                    predict_info={"file_name_predict":file_name,"label_predict":-1,"prob_predict":-1}
                elif predict==1:#True Benign
                    predict_info={"file_name_predict":file_name,"label_predict":predict-1,"prob_predict":precision_max}
                elif predict==2:#False Malign
                    predict_info={"file_name_predict":file_name,"label_predict":predict-1,"prob_predict":precision_max}
                

            # print("predict_list")           
            # print(predict_list)           
            
            
            if thyroid_type==2:#malign
                predict_list=[]
                precision_max=0
                iou=0
                predict=0
                true=0
                # print("case2,malign")
                color = red_color
                box1 = ((values[0], values[1]),(values[0]+values[2], values[1]+values[3]))
                if len(v[0])!=0:
                    color = benign_color
                    array = v[0]
                    for values in array:
                        values[:4] = list(map(int, values))[:4]
                        precision=values[4]
                        if precision>basis:
                            box2= ((values[0],values[1]),(values[2],values[3]))
                            iou=intersection_over_union(box1, box2)
                            if iou>threshold:
                                predict_list.append((precision,iou,1,2))
                if len(v[1])!=0:
                    color = malign_color
                    array = v[1]
                    for values in array:
                        values[:4] = list(map(int, values))[:4]
                        precision=values[4]
                        if precision>basis:
                            box2= ((values[0],values[1]),(values[2],values[3]))
                            iou=intersection_over_union(box1, box2)

                            if iou>threshold:
                                predict_list.append((precision,iou,2,2))

                if len(predict_list)>=1:
                    for precision_p,iou_p,predict_p,true_p in predict_list:
                        if precision_max<precision_p:
                            precision_max=precision_p
                            iou=iou_p
                            predict=predict_p
                            true = true_p
                # print(f"predict_value:{precision_max,iou,predict}")
                if predict==0:#Zero malign
                    predict_info={"file_name_predict":file_name,"label_predict":-1,"prob_predict":-1}

                elif predict==1:#False Benign
                    predict_info={"file_name_predict":file_name,"label_predict":predict-1,"prob_predict":precision_max}

                elif predict==2:#True malign
                    predict_info={"file_name_predict":file_name,"label_predict":predict-1,"prob_predict":precision_max}
                    
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

    series = pd.Series([img_info["file_name"],str(img_info["label"]),str(img_info["nodule"]),str(img_info["maker"]),str(predict_info["label_predict"]),predict_info["prob_predict"]],index=["file_name","img_label","nodule","maker","label_predict","prob_predict"])
    
    df2=df2.append(series,ignore_index=True)
                       

    return df2,check_count

check_count = [0,0]

# print("test_result")
# print(len(test_result))#305

for i,v in enumerate(test_result[:]): #모든 예측값에 대해서 가져온다.
    # print(i,len(v[0]),len(v[1]))
    
    df2,check_count=result(i,v,check_count,0.5,0.3,df2)
    print(f"check_count:{check_count}")


print(df2)
save_csv="/home/con/mmdetection/data/thyroid/result_csv/"#db데이터 가져온 정보, csv로 저장되는 폴더(6번은 제외한다.)

num=input("몇번 testset인가??")
df2.to_csv(f"{save_csv}df{num}.csv")