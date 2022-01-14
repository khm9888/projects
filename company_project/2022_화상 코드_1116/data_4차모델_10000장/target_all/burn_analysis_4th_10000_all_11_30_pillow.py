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

# import cv2
from PIL import Image, ImageDraw, ImageFont

import time

import torch.nn.functional as F


path_burn_image = "/home/lab/burn/data/data/data_con/con_10000_211124/"
test_file_path = f"{path_burn_image}/csv_data/"
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
broken_count = 0
broken_set = set()

def result():
    
    #############################################
    # df_result=pd.read_csv(f"{path_burn_image}result_bit.csv")
    # df_result=df_result.sort_values("file_name_r")
    # df_result=df_result.reset_index(drop=True)
    #############################################
    
   
    df_test=pd.read_csv(f"{test_file_path}merged.csv")
    # print(df_test["cls"])
    print(df_test)
    print(set(df_test["class"]))
    
    #############################################
    # mask = (df_test["cls"] !="1st") & (df_test["cls"] !="intermediate_2nd")
    # df_test=df_test[mask]
    #############################################
    
    # df_test=df_test.sort_values("img_path")
    # df_test=df_test.reset_index(drop=True)
    # df_result.sort_values("file_name")
    
    #############################################
    # print("df_result")
    # print(df_result)
    #############################################
    
    print("df_test")
    print(df_test)
    
    print("class")
    print(set(df_test["class"]))
    # input()
    
    # input()
    
    # input()


    load_path = load_image_path
    os.makedirs(f"{path_burn_image}/record/img_{today[2:]}_1",exist_ok=True)
    save_path = f"{path_burn_image}/record/img_{today[2:]}_1/"


    def pil_draw_rect(image, point1, point2,true):

        draw = ImageDraw.Draw(image)
        draw.rectangle((point1, point2), outline=(0, 0, 255), width=3)
        draw.text((x1,(y1+y2)//2),f"true : {true[:5]}")


        
        return image

    check_set = set()
    class_name_list = ['burn', 'above_3rd', 'not_sure', 'deep_2nd', 'intermediate_2nd', 'normal', 'superficial_2nd', '1st']
    print(df_test)
    for i in class_name_list:
        createFolder(f"{save_path}/{i}")
    for i in tqdm(range(len(df_test))):
        print("df_test.keys()")
        print(df_test.keys())
        # input()
        file=df_test.iloc[i]['img_path']
        cls_name=df_test.iloc[i]["class"]
        loc_list = df_test.iloc[i]["x1"],df_test.iloc[i]["y1"],df_test.iloc[i]["x2"],df_test.iloc[i]["y2"]
        x1,y1,x2,y2 = loc_list
        if x2<x1:
            x1,x2=x2,x1
            print("x_true")
        if y2<y1:
            y1,y2=y2,y1
            print("y_true")
        try:
        
            if file not in check_set:
                check_set.add(file)
            else:
                load_path=save_path
            print(file)
            print(load_path+file)
            print(cls_name)
            print()
            # input()
            image1 =Image.open(load_path+file)
            
            # cv2.imwrite(f"{save_path}/{origin_file_name.split('.')[0]}_0.jpg",image1)
            print(x1,y1,x2,y2)

            convert_image = pil_draw_rect(image1, (x1, y1), (x2, y2),cls_name)
            convert_image=convert_image.convert('RGB')

            
            convert_image.save(f"{save_path}{cls_name}/{file}")
            convert_image.save(f"{save_path}/{file}")
        # input()
        except:
            global broken_count
            broken_count += 1
            time.sleep(3)
            print(broken_count)
            broken_set.add(file)
            
        load_path = f"{path_burn_image}/before_crop_data/images/"

        

result()
print()
print("total broken_count")
print(broken_count)
print(broken_set)
print()
# result("b")
# result("c")