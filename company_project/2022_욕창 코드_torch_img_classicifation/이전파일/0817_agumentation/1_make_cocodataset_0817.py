import datetime
import pandas as pd
import json
from collections import defaultdict
import os
import numpy as np

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def csv_to_json(file="train"):
    path=f"/home/ubuntu/con/code/BiT/data/"
    data_path=f"{path}labels/{file}.csv"
    save_path=f"{path}json/"
    save_json=f"{path}save_json/"
    createFolder(save_json)
    createFolder(save_path)

    date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#
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
    with open(f"{save_json}{year_month_day}_{times}.json","w") as json_file:
        try:
            json.dump(base,json_file)
        except:
            print(json_file)

csv_to_json("train")
csv_to_json("test")
csv_to_json("val")