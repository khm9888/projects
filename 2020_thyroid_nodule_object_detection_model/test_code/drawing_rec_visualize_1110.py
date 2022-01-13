import numpy as np
import pickle
import json
import cv2
import datetime
import pandas as pd
import copy
import os

classes=["benign","malign"]

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#
year_month_day,times=date[:8],date[8:]


file_path="/home/con/mmdetection/data/thyroid/"
# test_result_image_path=f"/mnt/sdb/AI/work/test_result_image/{year_month_day}/"
test_result_image_path=f"/home/con/mmdetection/data/thyroid/test_result/{year_month_day}/"
test_json_path="/home/con/mmdetection/data/thyroid/annotations/"
img_path="/home/con/mmdetection/data/thyroid/preprocess/"
compare_image_path=test_result_image_path+"/compare_image/"
img_load_path = "/mnt/sdb/AI/work/save_img/"
json_load_path = f"/home/con/mmdetection/data/thyroid/test/{year_month_day}/result/"

createFolder(test_result_image_path)
createFolder(compare_image_path)
#색 지정

blue_color = (255, 0, 0) #BGR
red_color = (0, 0, 255)
benign_color=(0,255,0)#녹색
malign_color=(255,0,255)# 자주,보라
white_color = (255, 255, 255)



with open(f"{json_load_path}/result.json","r") as file:
    data = json.load(file)

# print(len)#401
    
df = pd.DataFrame(data)
df.to_csv(f"{file_path}test.csv")

with open(f"{test_json_path}/from_db.json","r") as file:
    json_data = json.load(file)    

value_array = np.array(data)

image_data = json_data["images"]

benign_count=0
malign_count=0

def intersection_over_union(box1, box2):
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

def drawing_rec(i,v,count_values,basis,threshold):
    # print("v")
    # v["bbox"]= np.array(v["bbox"])
    

    # print(type(v["bbox"]))
    # print(v["bbox"])#[array([], dtype=int64) array([[546, 140, 633, 219,   0]])]

    
    # print(type(v))
    # print(f"--{i+1}--")
    file_name=v["file_name"]
    
    # print(image_data)
    
    # for image in image_data:
    #     if image["file_name"]==file_name:
    #         input_image_date=image
    # print(f"file_name:{file_name}")

    split_values=file_name.split(".")
    name,format0=file_name[:-(len(split_values[-1])+1)],split_values[-1]   
    # print()
    height=input_image_date["height"]
    width=input_image_date["width"]
    # print(height,width)
    img_id = input_image_date["id"]
    # print(img_path+file_name)
    img = cv2.imread(img_path+file_name)
    copy_img = copy.copy(img)
    for anno in json_data["annotations"]:#어노테이션 데이터 가져옴
        if anno["image_id"]==img_id:
            thyroid_type=anno["category_id"]#1 or 2
            values=anno["bbox"]
            if thyroid_type==1:
                # print("case1,benign")
                color = blue_color
                box1 = ((values[0], values[1]),(values[0]+values[2], values[1]+values[3]))
                img = cv2.rectangle(img, box1[0],box1[1], color,3)
                copy_img = cv2.rectangle(copy_img, box1[0],box1[1], color,3)
                predict_list=[]
                # print(classes[0])
                if len(v["bbox"][classes[0]])!=0:
                    color = benign_color
                    array = v["bbox"][classes[0]]
                    print(array)
                    for values in array:
                        values[:4] = list(map(int, values))[:4]
                        accuracy=values[4]
                        if accuracy>basis:
                            box2= ((values[0],values[1]),(values[2],values[3]))
                            img = cv2.rectangle(img, box2[0], box2[1], color,3 )
                            text=str(values[4])[:6]
                            x,y = int((values[0]+values[2])//2),int((values[1]+values[3])//2+20)
                            cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,color,1,cv2.LINE_AA)
                            iou=intersection_over_union(box1, box2)
                            if iou>threshold:
                                predict_list.append((accuracy,iou,1))
                if len(v["bbox"][classes[1]])!=0:
                    color = malign_color
                    array = v["bbox"][classes[1]]
                    for values in array:
                        values[:4] = list(map(int, values))[:4]
                        accuracy=values[4]
                        if accuracy>basis:
                            box2= ((values[0],values[1]),(values[2],values[3]))
                            img = cv2.rectangle(img, (values[0], values[1]), (values[2],values[3]), color,3 )
                            text=str(values[4])[:6]
                            x,y = int((values[0]+values[2])//2),int((values[1]+values[3])//2-20)
                            cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,color,1,cv2.LINE_AA)
                            iou=intersection_over_union(box1, box2)

                            if iou>threshold:
                                predict_list.append((accuracy,iou,2))
                accuracy_max=0
                iou=0
                category=0
                if len(predict_list)>=1:
                    for accuracy_p,iou_p,category_p in predict_list:
                        if accuracy_max<accuracy_p:
                            accuracy_max=accuracy_p
                            iou=iou_p
                            category=category_p
                # print(f"predict_value:{accuracy_max,iou,category}")
                if category==0:
                    count_values[2][thyroid_type-1]+=1
                elif category==1:
                    count_values[0][thyroid_type-1]+=1
                elif category==2:
                    count_values[1][thyroid_type-1]+=1
                       
            if thyroid_type==2:
                # print("case2,malign")
                color = red_color
                box1 = ((values[0], values[1]),(values[0]+values[2], values[1]+values[3]))
                img = cv2.rectangle(img, box1[0],box1[1], color,3)
                copy_img = cv2.rectangle(copy_img, box1[0],box1[1], color,3)
                predict_list=[]
                if len(v["bbox"][classes[0]])!=0:
                    color = benign_color
                    array = v["bbox"][classes[0]]
                    for values in array:
                        values[:4] = list(map(int, values))[:4]
                        accuracy=values[4]
                        if accuracy>basis:
                            box2= ((values[0],values[1]),(values[2],values[3]))
                            img = cv2.rectangle(img, box2[0], box2[1], color,3 )
                            text=str(values[4])[:6]
                            x,y = int((values[0]+values[2])//2),int((values[1]+values[3])//2+20)
                            cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,color,1,cv2.LINE_AA)
                            iou=intersection_over_union(box1, box2)
                            if iou>threshold:
                                predict_list.append((accuracy,iou,1))
                if len(v["bbox"][classes[1]])!=0:
                    color = malign_color
                    array = v["bbox"][classes[1]]
                    for values in array:
                        values[:4] = list(map(int, values))[:4]
                        accuracy=values[4]
                        if accuracy>basis:
                            box2= ((values[0],values[1]),(values[2],values[3]))
                            
                            img = cv2.rectangle(img, (values[0], values[1]), (values[2],values[3]), color,3 )
                            text=str(values[4])[:6]
                            x,y = int((values[0]+values[2])//2),int((values[1]+values[3])//2-20)
                            cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.7,color,1,cv2.LINE_AA)
                            iou=intersection_over_union(box1, box2)

                            if iou>threshold:
                                predict_list.append((accuracy,iou,2))
                    
                                
                accuracy_max=0
                iou=0
                category=0
                if len(predict_list)>=1:
                    for accuracy_p,iou_p,category_p in predict_list:
                        if accuracy_max<accuracy_p:
                            accuracy_max=accuracy_p
                            iou=iou_p
                            category=category_p                 
                # print(f"predict_value:{accuracy_max,iou,category}")
                if category==0:
                    count_values[2][thyroid_type-1]+=1
                elif category==1:
                    count_values[0][thyroid_type-1]+=1
                elif category==2:
                    count_values[1][thyroid_type-1]+=1
                    
            # img = cv2.rectangle(img, (values[0], values[1]), (values[0]+values[2], values[1]+values[3]), color,1, cv2.FILLED	)
            # print("values")
            # print(values)
            
    
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

v_array=value_array[:]
for i,v in enumerate(v_array):
    count_values=drawing_rec(i,v,count_values,0.5,threshold=0.5)
    # print(f"count_values:{count_values}")

TB,TM,FB,FM,OB,OM = count_values[0][0],count_values[1][1],count_values[1][0],count_values[0][1],count_values[2][0],count_values[2][1]
# print(TM)
# print(TB)
if TM!=0:
    sensitivity = TM/(TM+FM+OM)
else:
    sensitivity=0
if TB!=0:
    specificity = TB/(TB+FB+OB)
else:
    specificity=0

print(f"TB:{TB},TM:{TM},FB:{FB},FM:{FM},OB:{OB},OM:{OM}")
print(f"sensitivity:{round(sensitivity,3)*100}%")#민감도 - 실제 악성 중 예상도 악성으로 나온 케이스
print(f"specificity:{round(specificity,3)*100}%")#특이도 - 비환자 중에서 예상도 양성으로 나온 케이스
