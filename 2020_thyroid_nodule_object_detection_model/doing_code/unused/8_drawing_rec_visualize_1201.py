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

createFolder(test_result_image_path)
createFolder(compare_image_path)

#색 지정

blue_color = (255, 0, 0) #BGR
red_color = (0, 0, 255)
benign_color=(0,255,0)#녹색
malign_color=(255,0,255)# 자주,보라
white_color = (255, 255, 255)


dict_makers  = dict()
for i in range(10):
    dict_makers[i]=[[0,0],[0,0],[0,0]]

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

def drawing_rec(i,v,count_values,basis=0.5,threshold=0.5):#basis <- 양성, 악성에 대한 확률 기준값
    global dict_makers
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
    if math.isnan(maker_id):
        maker_id=0
    # print(img_path+file_name)
    img = cv2.imread(img_path+file_name)
    copy_img = copy.copy(img)
    for anno in json_data["annotations"]:#실제 데이터의 어노테이션 데이터 가져옴
        if anno["image_id"]==img_id:

            thyroid_type=anno["category_id"]#1 or 2
            values=anno["bbox"]
            if thyroid_type==1:
                predict_list=[]
                precision_max=0
                iou=0
                predict=0
                true=0
                # print("case1,benign")
                color = blue_color
                box1 = ((values[0], values[1]),(values[0]+values[2], values[1]+values[3]))
                img = cv2.rectangle(img, box1[0],box1[1], color,3)
                copy_img = cv2.rectangle(copy_img, box1[0],box1[1], color,3)
                if len(v[0])!=0:
                    color = benign_color
                    array = v[0]
                    for values in array:
                        values[:4] = list(map(int, values))[:4]
                        precision=values[4]
                        if precision>basis:
                            box2= ((values[0],values[1]),(values[2],values[3]))
                            img = cv2.rectangle(img, box2[0], box2[1], color,3 )
                            text=str(values[4])[:6]
                            x,y = int((values[0]+values[2])//2),int((values[1]+values[3])//2+20)
                            cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,color,1,cv2.LINE_AA)
                            iou=intersection_over_union(box1, box2)
                            if iou>threshold:
                                predict_list.append((precision,iou,1,1))
                if len(v[1])!=0:
                    color = malign_color
                    array = v[1]
                    for values in array:
                        values[:4] = list(map(int, values))[:4]
                        precision=values[4]
                        if precision>basis:
                            box2= ((values[0],values[1]),(values[2],values[3]))
                            img = cv2.rectangle(img, (values[0], values[1]), (values[2],values[3]), color,3 )
                            text=str(values[4])[:6]
                            x,y = int((values[0]+values[2])//2),int((values[1]+values[3])//2-20)
                            cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,color,1,cv2.LINE_AA)
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
                if predict==0:
                    count_values[2][thyroid_type-1]+=1
                    dict_makers[maker_id][2][0]+=1
                elif predict==1:
                    count_values[0][thyroid_type-1]+=1
                    dict_makers[maker_id][0][0]+=1
                elif predict==2:
                    count_values[1][thyroid_type-1]+=1
                    dict_makers[maker_id][1][0]+=1
            # print("predict_list")           
            # print(predict_list)           
            if thyroid_type==2:
                predict_list=[]
                precision_max=0
                iou=0
                predict=0
                true=0
                # print("case2,malign")
                color = red_color
                box1 = ((values[0], values[1]),(values[0]+values[2], values[1]+values[3]))
                img = cv2.rectangle(img, box1[0],box1[1], color,3)
                copy_img = cv2.rectangle(copy_img, box1[0],box1[1], color,3)
                if len(v[0])!=0:
                    color = benign_color
                    array = v[0]
                    for values in array:
                        values[:4] = list(map(int, values))[:4]
                        precision=values[4]
                        if precision>basis:
                            box2= ((values[0],values[1]),(values[2],values[3]))
                            img = cv2.rectangle(img, box2[0], box2[1], color,3 )
                            text=str(values[4])[:6]
                            x,y = int((values[0]+values[2])//2),int((values[1]+values[3])//2+20)
                            cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,color,1,cv2.LINE_AA)
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
                            img = cv2.rectangle(img, (values[0], values[1]), (values[2],values[3]), color,3 )
                            text=str(values[4])[:6]
                            x,y = int((values[0]+values[2])//2),int((values[1]+values[3])//2-20)
                            cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,color,1,cv2.LINE_AA)
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
                if predict==0:
                    count_values[2][thyroid_type-1]+=1
                    dict_makers[maker_id][2][1]+=1
                elif predict==1:
                    count_values[0][thyroid_type-1]+=1
                    dict_makers[maker_id][0][1]+=1
                elif predict==2:
                    count_values[1][thyroid_type-1]+=1  
                    dict_makers[maker_id][1][1]+=1
    
    # print(f"{compare_image_path}{name}_true.{format0}")#id까지 표시했습니다.

    cv2.imwrite(f"{compare_image_path}{name}_true.{format0}",copy_img)#id까지 표시했습니다.


    x,y = map(int,(width-220,height-180))

    text="Benign(T)"
    x,y = map(int,(width-200,height-150))
    cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,blue_color,1,cv2.LINE_AA)
    y = y+40
    text="Malign(T)"
    cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,red_color,1,cv2.LINE_AA)
    y = y+40
    text="Benign(Predict)"
    cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,benign_color,1,cv2.LINE_AA)
    y = y+40
    text="Malign(Predict)"
    cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,malign_color,1,cv2.LINE_AA)
    cv2.imwrite(f"{test_result_image_path}{name}_test.{format0}",img)

    return count_values

count_values=[[0,0],[0,0],[0,0]]

# print("test_result")
# print(len(test_result))#305

for i,v in enumerate(test_result[:]): #모든 예측값에 대해서 가져온다.
    # print(i,len(v[0]),len(v[1]))
    count_values=drawing_rec(i,v,count_values,threshold=0.5,basis=0.5)
    # print(f"count_values:{count_values}")


def add(values):
    total=0
    for value in values:
        for v in value:
            total+=v
    return total

# createFolder(f"/mnt/sdb/AI/work/result_txt/{year_month_day}")

# TB,TM,FB,FM,OB,OM = count_values[0][0],count_values[1][1],count_values[1][0],count_values[0][1],count_values[2][0],count_values[2][1]
TB,TM,FB,FM,OB,OM = 0,0,0,0,0,0

with open(f"/mnt/sdb/AI/work/result_txt/{year_month_day}.txt","a") as file:
    print()
    file.write("\n")
    record_word = input("기록에 남길 파일명과 epoch")
    print(record_word)
    file.write(record_word+"\n")
    print(date)
    file.write(f"{date}\n")
    
    for i in range(10):
        print(f"{i}번째_{list_maker_names[i]:17s} : {dict_makers[i]},{add(dict_makers[i])}")
        file.write(f"{i}번째_{list_maker_names[i]:17s} : {dict_makers[i]},{add(dict_makers[i])}\n")

# 이 부분은 9,4,3 제품군 제외
    print()
    print("0~9번의 제품군 중 3,4,9번을 제외한 결과입니다.")
    file.write("\n")
    file.write("0~9번의 제품군 중 3,4,9번을 제외한 결과입니다.\n")
    except_maker_ids = [3,4,9]
    for i in range(10):
        if i not in except_maker_ids:
            tb,tm = dict_makers[i][0][0],dict_makers[i][1][1]
            fb,fm = dict_makers[i][1][0],dict_makers[i][0][1]
            ob,om = dict_makers[i][2][0],dict_makers[i][2][1]
            TB +=tb
            TM +=tm
            FB +=fb
            FM +=fm
            OB +=ob
            OM +=om
            
            total = add(dict_makers[i])
            total_b = tb+fb+ob
            total_m = tm+fm+om
            # print(f"tm:{tm}({total_m}개),tb:{tb}({total_b}개),total:{total}")
            # file.write(f"tm:{tm}({total_m}개),tb:{tb}({total_b}개),total:{total}\n")
            if total ==0:
                total+=1
            if total_b == 0:
                total_b+=1
            if total_m == 0:
                total_m+=1
            #분모가 0이 안 되게 해서, 0으로 나누어지는 divide error 발생하지 않게 하기.
            
            # print(f"{i}번째_{list_maker_names[i]:17s} : sensitivity : {(tm)/(total_m)*100:.1f}%, specificity : {(tb)/(total_b)*100:.1f}%, accuracy : {(tm+tb)/total*100:.1f}%")
            # file.write(f"{i}번째_{list_maker_names[i]:17s} : sensitivity : {(tm)/(total_m)*100:.1f}%, specificity : {(tb)/(total_b)*100:.1f}%, accuracy : {(tm+tb)/total*100:.1f}%\n")
            # print()
            # file.write("\n")
            
    if TM!=0:
        sensitivity = TM/(TM+FM+OM)
    else:
        sensitivity=0
    if TB!=0:
        specificity = TB/(TB+FB+OB)
    else:
        specificity=0
    accuracy = (TB+TM)/(TM+FM+OM+TB+FB+OB)

    # print(f"이미지 총 개수는 {len(test_result)}")
    print(f"어노테이션 총 개수는 {TB+TM+FB+FM+OB+OM}")

    print(f"TB:{TB},TM:{TM},FB:{FB},FM:{FM},OB:{OB},OM:{OM}")
    print(f"sensitivity:{round(sensitivity,3)*100}%")#민감도 - 실제 악성 중 예상도 악성으로 나온 케이스
    print(f"specificity:{round(specificity,3)*100}%")#특이도 - 비환자 중에서 예상도 양성으로 나온 케이스
    print(f"  accuracy:{round(accuracy,3)*100}%")#특이도 - 비환자 중에서 예상도 양성으로 나온 케이스

    # file.write(f"이미지 총 개수는 {len(test_result)}\n")
    file.write(f"어노테이션 총 개수는 {TB+TM+FB+FM+OB+OM}\n")

    file.write(f"TB:{TB},TM:{TM},FB:{FB},FM:{FM},OB:{OB},OM:{OM}\n")
    file.write(f"sensitivity:{round(sensitivity,3)*100}%\n")#민감도 - 실제 악성 중 예상도 악성으로 나온 케이스
    file.write(f"specificity:{round(specificity,3)*100}%\n")#특이도 - 비환자 중에서 예상도 양성으로 나온 케이스
    file.write(f"  accuracy:{round(accuracy,3)*100}%\n")#특이도 - 비환자 중에서 예상도 양성으로 나온 케이스
    file.write("\n")
    file.write("-------------------------\n")
    file.write("\n")
    
TB,TM,FB,FM,OB,OM = count_values[0][0],count_values[1][1],count_values[1][0],count_values[0][1],count_values[2][0],count_values[2][1]
if TM!=0:
    sensitivity = TM/(TM+FM+OM)
else:
    sensitivity=0
if TB!=0:
    specificity = TB/(TB+FB+OB)
else:
    specificity=0
accuracy = (TB+TM)/(TM+FM+OM+TB+FB+OB)

with open(f"/mnt/sdb/AI/work/result_txt/{year_month_day}.txt","a") as file:

#이 부분은 모든 제품군 포함
    
    print()
    print("="*30)
    print("모든 제품군을 포함한 결과입니다.")

    file.write("\n")
    file.write("="*30+"\n")
    file.write("모든 제품군을 포함한 결과입니다.\n")

    for i in range(10):
        tb,tm = dict_makers[i][0][0],dict_makers[i][1][1]
        fb,fm = dict_makers[i][1][0],dict_makers[i][0][1]
        ob,om = dict_makers[i][2][0],dict_makers[i][2][1]
        
        total = add(dict_makers[i])
        total_b = tb+fb+ob
        total_m = tm+fm+om
        print(f"tm:{tm}({total_m}개),tb:{tb}({total_b}개),total:{total}")
        file.write(f"tm:{tm}({total_m}개),tb:{tb}({total_b}개),total:{total}\n")
        if total ==0:
            total+=1
        if total_b == 0:
            total_b+=1
        if total_m == 0:
            total_m+=1
        #분모가 0이 안 되게 해서, 0으로 나누어지는 divide error 발생하지 않게 하기.
        
        print(f"{i}번째_{list_maker_names[i]:17s} : sensitivity : {(tm)/(total_m)*100:.1f}%, specificity : {(tb)/(total_b)*100:.1f}%, accuracy : {(tm+tb)/total*100:.1f}%")
        file.write(f"{i}번째_{list_maker_names[i]:17s} : sensitivity : {(tm)/(total_m)*100:.1f}%, specificity : {(tb)/(total_b)*100:.1f}%, accuracy : {(tm+tb)/total*100:.1f}%\n")
        print()
        file.write("\n")
             
# 총합적인 확인
    print(f"이미지 총 개수는 {len(test_result)}")
    print(f"어노테이션 총 개수는 {TB+TM+FB+FM+OB+OM}")

    print(f"TB:{TB},TM:{TM},FB:{FB},FM:{FM},OB:{OB},OM:{OM}")
    print(f"sensitivity:{round(sensitivity,3)*100}%")#민감도 - 실제 악성 중 예상도 악성으로 나온 케이스
    print(f"specificity:{round(specificity,3)*100}%")#특이도 - 비환자 중에서 예상도 양성으로 나온 케이스
    print(f"   accuracy:{round(accuracy,3)*100}%")#특이도 - 비환자 중에서 예상도 양성으로 나온 케이스

    file.write(f"이미지 총 개수는 {len(test_result)}\n")
    file.write(f"어노테이션 총 개수는 {TB+TM+FB+FM+OB+OM}\n")

    file.write(f"TB:{TB},TM:{TM},FB:{FB},FM:{FM},OB:{OB},OM:{OM}\n")
    file.write(f"sensitivity:{round(sensitivity,3)*100}%\n")#민감도 - 실제 악성 중 예상도 악성으로 나온 케이스
    file.write(f"specificity:{round(specificity,3)*100}%\n")#특이도 - 비환자 중에서 예상도 양성으로 나온 케이스
    file.write(f"   accuracy:{round(accuracy,3)*100}%\n")#특이도 - 비환자 중에서 예상도 양성으로 나온 케이스
    file.write("\n")
    file.write("-------------------------\n")
    file.write("\n")
