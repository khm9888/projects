from datetime import datetime
import pandas as pd
import json
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# 
from PIL import Image

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
###########################
# 0-1. train/val/test.csv를 가져와서 json으로 생성하는 코드
###########################

def csv_to_json(file):
    path=f"/home/ubuntu/con/code/BiT/data/"
    data_path=f"{path}labels/{file}.csv"
    
    save_path=f"{path}json/"
    createFolder(save_path)
    save_json=f"{path}save_json/"
    createFolder(save_json)

    date=datetime.strftime('%Y%m%d%H%M%S')#
    year_month_day,times=date[:8],date[8:]

    data_df=pd.read_csv(data_path)

    print(data_df)

    base=dict() #json 만들기 위한 기본 딕셔너리 구조

    base["images"]=list()
    base["annotations"]=list()
    base["categories"]=list()

    for n in range(len(data_df)):
        print(data_df.iloc[n])
        file_name = data_df.iloc[n]["img_path"]
        # cls = list(map(int,list(data_df.iloc[n]["cls"])))
        cls = int(data_df.iloc[n]["cls"])
        bbox = data_df.iloc[n][-4:]
        image_dict=dict()
        image_dict["id"]=n
        image_dict["img_path"]=file_name
        base["images"].append(image_dict)
        
        annotation_dict=dict()
        annotation_dict["id"]=f"{n}_1"
        annotation_dict["image_id"]=n
        annotation_dict["category_id"]=cls
        annotation_dict["bbox"]=bbox
        for a in annotation_dict.values():
            print(a)
            print(type(a))
            input()
        base["categories"].append(annotation_dict)

    change_value_dict = {'4단계':4, '심부조직손상':5, '1단계':1, '미분류':0, '2단계':2, '3단계':3}
    for key, value in change_value_dict.items():
        category_dict=dict()
        category_dict["category"]=value
        category_dict["grade_name"]=key
        # base["categories"].append(category_dict)
        
    with open(f"{save_path}{file}.json","w") as json_file:
        json.dump(base,json_file)
    with open(f"{save_json}{file}_{year_month_day}_{times}.json","w") as json_file:
        try:
            json.dump(base,json_file)
        except:
            print(json_file)
            
# for num in range(5):
for num in range(1):
    csv_to_json(f"train_{num}")
    csv_to_json(f"test_{num}")
    csv_to_json(f"val_{num}")


###########################
# 0-1 완료
###########################

###########################
# 0-2. 이미지를 가져와서 train/val/test 별로 클래스에 따라 넣는 코드
###########################


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def img_split(file):#train
    path = "/home/ubuntu/con/code/BiT/data/labels/"
    load_img_path = "/home/ubuntu/con/code/BiT/data/images/"
    data_df = pd.read_csv(f"{path}/{file}.csv")
        
    for folder_num in range(5):
        createFolder(f"{path}/{file}/{folder_num}")
        filter_df = [data_df["cls"]==folder_num]
        for file_path in filter_df["img_path"]:
            img1 = Image.open(load_img_path+file_path)
            img1.save(f"{path}/{file}/{folder_num}/{file_path}")
            
img_split("train")
# img_split("val") #val인지 valid 인지
img_split("test")

###########################
# 0-2 완료
###########################
