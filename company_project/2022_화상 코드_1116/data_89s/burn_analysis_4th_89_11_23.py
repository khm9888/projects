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


path_burn_image = "/home/lab/burn/data/data/data_con/4th_89_211123/"
# test_file_path = "/home/lab/burn/data/data/createdata_cls/labels_2del/"
load_image_path = "/home/lab/burn/data/data/test_210914/"
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


    df_plus_convert=pd.read_csv(f"{path_burn_image}result_bit.csv")
    print(df_plus_convert)

    load_path = load_image_path
    save_path = f"{path_burn_image}/record/img_{today[2:]}_89s/"


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

        file=df_plus_convert.iloc[i]['file_name_r']
        cls_name=df_plus_convert.iloc[i]["test"]
        predict=df_plus_convert.iloc[i]["predict"]

        rate = df_plus_convert.iloc[i]['prob']
        

        print(file)
        print(f"{load_path}{cls_name}/{file}")
        image1 = cv2.imread(f"{load_path}{cls_name}/{file}")
        h,w,c = image1.shape
        
        cv2.putText(image1,f"true : {cls_name}, predict :{predict}, rate: {rate:.3f}",(10,(h)//2),3, 1 ,(0,0,0),3)
        # convert_image=convert_image.convert('RGB')
        
        cv2.imwrite(f"{save_path}{cls_name}/{predict}/{file}",image1)

        

result()

# result("b")
# result("c")