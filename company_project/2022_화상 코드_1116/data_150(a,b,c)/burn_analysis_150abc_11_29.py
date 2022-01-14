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
from src import lbtoolbox as lb # Uninterrupt -> ?쒓렇??而⑦듃濡?(INT, TERM ??, Timer, Chrono, create_dat, load_dat 

import argparse

import cv2

import torch.nn.functional as F


path_burn_image = "/home/lab/burn/data/data/data_con/con_150abc_211112/"
# path_burn_image = "C://Users/Acryl/Desktop/burn_image/"

today=datetime.today().strftime("%y%m%d")


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


######################
# 2-3 result ? test瑜??⑹튂怨?
######################

def result(data_name):
    df_result=pd.read_csv(f"{path_burn_image}result_bit_{data_name}.csv")
    df_result=df_result.sort_values("file_name_r")
    df_result=df_result.reset_index(drop=True)
    
    df_test=pd.read_csv(f"{path_burn_image}part_{data_name}_trans_test.csv")
    mask = (df_test["class"] !="1st")
    df_test=df_test[mask]
    df_test=df_test.sort_values("file_name")
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
    df_plus.to_csv(f"{path_burn_image}result_calc_{data_name}.csv",index=0)

    df_plus_convert=pd.read_csv(f"{path_burn_image}result_calc_{data_name}.csv")
    print(df_plus_convert)

    load_path = f"{path_burn_image}image_before/"
    save_path = f"{path_burn_image}/record/img_{today[2:]}/"


    def pil_draw_rect(image, x1, y1, x2, y2,true,predict,rate):
        if true == predict:
            cv2.rectangle(image,(x1, y1), (x2, y2),(255, 0, 0), 4)
        else:
            cv2.rectangle(image,(x1, y1), (x2, y2),(0, 0, 255), 4)
            
        # font = ImageFont.truetype('msyhbd.ttf',size=30)
        if true == predict:
            txt = f"true : {true[:5]}"
        else:
            txt = f"true : {true[:5]}, predict :{predict[:5]}"
        if x1<x2:   
            cv2.putText(image,txt,(x1,(y1+y2)//2),3, 1 ,(0,0,0),3)
        else:
            cv2.putText(image,txt,(x2,(y1+y2)//2),3, 1 ,(0,0,0),3)

        return image

    check_set = set()
    class_name_list = ['above_3rd', 'deep_2nd', 'normal', 'not_sure', 'superficial_2nd']
    for i in class_name_list:
        for j in class_name_list:
            createFolder(f"{save_path}/{i}/{j}")
    for i in tqdm(range(len(df_plus_convert))):

        file=df_plus_convert.iloc[i]['file_name']
        origin_file_name = df_plus_convert.iloc[i]['origin_file_name']
        cls_name=df_plus_convert.iloc[i]["test"]
        predict=df_plus_convert.iloc[i]["predict"]
        x1=df_plus_convert.iloc[i]['x1']
        y1=df_plus_convert.iloc[i]['y1']
        x2=df_plus_convert.iloc[i]['x2']
        y2=df_plus_convert.iloc[i]['y2']
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
        load_path = f"{path_burn_image}image_before/"

        

# result("a")

result("b")
result("c")