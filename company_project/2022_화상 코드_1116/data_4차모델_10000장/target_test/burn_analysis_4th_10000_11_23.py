import torch
import pandas as pd
import numpy as np
import torchvision as tv
import os

from tqdm import tqdm
from datetime import datetime
from sklearn.metrics import confusion_matrix, classification_report


from src import cus_dataset 
from src import models as models  
from src import bit_hyperrule # get resolution -> 480,  get_mixup -> 0.0 (db size < 20000),  get_schedule -> [100, 200, 300, 400, 500] (db_size < 20000), get_lr
from src import lbtoolbox as lb # Uninterrupt -> 시그널 컨트롤 (INT, TERM 등), Timer, Chrono, create_dat, load_dat 

import argparse

import cv2

import torch.nn.functional as F


path_burn_image = "/home/lab/burn/data/data/data_con/con_10000_211124/"
test_file_path = f"{path_burn_image}/csv_data/labels_2del/"
load_image_path = f"{path_burn_image}/before_crop_data/images/"
# save_image_path = "/home/lab/burn/data/data/con_test_211112/"
# path_burn_image = "C://Users/Acryl/Desktop/burn_image/"

today=datetime.today().strftime("%y%m%d")


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


######################
# 2-3 result 와 test를 합치고.
######################

def result():
    df_result=pd.read_csv(f"{path_burn_image}result_bit.csv")
    df_result=df_result.sort_values("file_name_r")
    df_result=df_result.reset_index(drop=True)
    
    df_test=pd.read_csv(f"{test_file_path}test.csv")
    # mask = (df_test["cls"] !="1st")
    # df_test=df_test[mask]
    df_test=df_test.sort_values("img_path")
    df_test=df_test.reset_index(drop=True)
    # df_result.sort_values("file_name")
    
    print("df_result")
    print(df_result)
    print("df_test")
    print(df_test)
    
    # input()
    
    df_plus = pd.concat([df_result,df_test],axis=1)
    print("df_plus")
    print(df_plus)
    # input()
    df_plus.to_csv(f"{path_burn_image}result_calc.csv",index=0)

    df_plus_convert=pd.read_csv(f"{path_burn_image}result_calc.csv")
    print(df_plus_convert)

    load_path = load_image_path
    os.makedirs("{path_burn_image}/record/img_{today[2:]}",exist_ok=True)
    save_path = f"{path_burn_image}/record/img_{today[2:]}/"


    def pil_draw_rect(image, x1, y1, x2, y2,true,predict,rate):

        cv2.rectangle(image,(x1, y1), (x2, y2),(255, 0, 0), 4)
        # font = ImageFont.truetype('msyhbd.ttf',size=30)
        
        cv2.putText(image,f"true : {true}, predict :{predict}, rate: {rate:.3f}",((x1+x2)//2,(y1+y2)//2),3, 1 ,(0,0,0),3)

        return image

    check_set = set()
    class_name_list = ['above_3rd', 'deep_2nd', 'normal', 'not_sure', 'superficial_2nd']
    for i in class_name_list:
        for j in class_name_list:
            createFolder(f"{save_path}/{i}/{j}")
    for i in tqdm(range(len(df_plus_convert))):
        # print("df_plus_convert.keys()")
        # print(df_plus_convert.keys())
        # input()
        file=df_plus_convert.iloc[i]['file_name_r']
        origin_file_name = df_plus_convert.iloc[i]['origin']
        cls_name=df_plus_convert.iloc[i]["test"]
        predict=df_plus_convert.iloc[i]["predict"]
        loc_str = df_plus_convert.iloc[i]['loc'][1:-1]
        loc_list =loc_str.split(",")
        loc_list = list(map(int,loc_list))
        x1,y1,x2,y2 = loc_list
        if x2<x1:
            x1,x2=x2,x1
        if y2<y1:
            y1,x2=y2,y1

        rate = df_plus_convert.iloc[i]['prob']
        
        if origin_file_name not in check_set:
            check_set.add(origin_file_name)
        else:
            load_path=save_path
        print(origin_file_name)
        print(load_path+file)
        image1 = cv2.imread(load_path+origin_file_name)
        print(x1,x2,y1,y2)
        convert_image = pil_draw_rect(image1, x1, y1, x2, y2,cls_name,predict,rate)
        # convert_image=convert_image.convert('RGB')
        
        cv2.imwrite(f"{save_path}{cls_name}/{predict}/{origin_file_name}",convert_image)
        cv2.imwrite(f"{save_path}/{origin_file_name}",convert_image)
        load_path = f"{path_burn_image}/before_crop_data/images/"

        

result()

# result("b")
# result("c")