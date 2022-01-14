import os
import shutil
from collections import defaultdict,Counter
from numpy.core.fromnumeric import sort
import pandas as pd
import time

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# 
from PIL import Image

path_burn_image = "C://Users/Acryl/Desktop/burn_image/"
path_before = f"{path_burn_image}image_before/"
path_after = f"{path_burn_image}image_after/"
path_crop = f"{path_burn_image}image_crop/"

def fileList(path_before): # a,b,c(set) / a,b,c 별로 나눠서 (dict) 에 넣어서 반환.
    folder_names_set = set()
    folder_images_dict = defaultdict(list)
    file_list = os.listdir(path_before)
    # print(file_list)
    # print(type(folder_names_set))

    for file in file_list:
        add_one = file.split("-")[0]
        folder_names_set.add(add_one)
        folder_images_dict[add_one].append(file)
    # print(folder_names_set)       
    # print(folder_images_dict)       
    return folder_names_set,folder_images_dict

def makeFolder(path_after,folder_names_set): # set에 있는 이름대로 폴더 생성
#폴더가 이미 생성되어있다면 오류가 발생하므로 예외처리 진행 
    for file in folder_names_set: 
        try: 
            os.makedirs(path_after+"/"+file) 
        except: 
            pass

def copyFile(path_before, path_after,folder_images_dict): # before에서 after로 dict에 맞춰서 파일 복사.
    
    #파일명에 대한 폴더명을 딕셔너리로 저장
    for key in folder_images_dict:
        for file in folder_images_dict[key]:
            shutil.copy(f"{path_before}/{file}",f"{path_after}/{key}/{file}")

# def cropImage()


class_korean_list=['1도', '3도 이상', '심재성 2도', '표재성 2도']
class_english_list = ["1st","above_3rd","deep_2nd","superficial_2nd"]#

# print(class_korean_list)
# print(class_english_list)

trans_class_dict = dict()
for i in range(len(class_korean_list)):
    trans_class_dict[class_korean_list[i]]=class_english_list[i]

def trans_key(korean_class):

    return trans_class_dict[korean_class]
   
def step_1(): #a,b,c에 맞춰서 폴더 만들어서 이미지 복사 적용.
    annotation_list = ["1st","above_3rd","deep_2nd","normal","not_sure","superficial_2nd"]
      
    folder_names_set,folder_images_dict = fileList(path_before)

    makeFolder(path_after,folder_names_set)
    makeFolder(path_crop,folder_names_set)
    
    for folder in folder_names_set:#a,b,c별로 class 명으로 폴더 생성
        makeFolder(f"{path_crop}/{folder}/",annotation_list)
        
    copyFile(path_before, path_after,folder_images_dict) #복사를 통해 해당 3개의 값에 대한 결과를 따로 받기 위해 이와 같이 나눈다.

def step_2(part):# 기존의 excel to excel 데이터 변환 
    print()
    print(part)
    time.sleep(1)
    
    df_part_data=pd.read_excel(f"C:/Users/Acryl/Desktop/burn_image/{part}",index_col=0)
    # print(Counter(df_part_data["class"]))
    df_part_data["class"]=list(map(trans_key, df_part_data["class"]))
    # print(Counter(df_part_data["class"]))
    print(df_part_data)
    
    xlsx_name = part.split(".")[0]
    df_part_data.to_excel(f"{path_burn_image}{xlsx_name}_trans.xlsx",index=0)

def step_3(part):#변환된 엑셀 파일을 통해 각 raw 별 값을 폴더에 집어 넣으려고 한다.
    print()
    print(part)
    time.sleep(1)
    
    df_part_data=pd.read_excel(f"{path_burn_image}{part}",index_col=0)
    print()
    register_dict = defaultdict(int)
    
    save_dict = dict()
    save_dict["file_name"]=list()
    save_dict["class"]=list()
        
    for raw_num in range(len(df_part_data)):
        print("="*50)
        # time.sleep(1)
        input()
        print("="*50)
        print(raw_num)
        # print(df_part_data.iloc[raw_num])
        file_name = (df_part_data.iloc[raw_num].name)#a-1830.JPG
        print(file_name)
        split_file_names = file_name.split(".")
        raw_data = tuple(df_part_data.iloc[raw_num])
        # print(raw_data)
        location,class_name = raw_data[:-1],raw_data[-1]
        x1,x2,y1,y2=location
        trans_location = (x1,y1,x2,y2)
        print(trans_location,class_name) 
        
        read_image = cv2.imread(f"{path_before}"+file_name)
        print("read_image.size")
        print(read_image.size)
        # cv2.imshow('original', read_image)
        input()
        croppedImage=read_image.crop(trans_location)
        
        if file_name not in register_dict:
            register_dict[file_name]=1
            rename_file =f"{split_file_names[0]}_0.{split_file_names[1]}"
        else:
            rename_file =f"{split_file_names[0]}_{register_dict[file_name]}.{split_file_names[1]}"
            register_dict[file_name]=+1
            
        save_img_loc = f"{path_crop}{file_name[0]}/{class_name}/"
        croppedImage.save(save_img_loc+rename_file)
        
        save_dict["file_name"].append(rename_file)
        save_dict["class"].append(class_name)
    
    crop_data_df=pd.df(save_dict)
    xlsx_name = part.split(".")[0]
    crop_data_df.to_excel(f"{path_burn_image}{xlsx_name}_result.xlsx",index=0)
        
        # print(t(df_part_data.iloc[raw_num]))


# step_1()
# step_2("part_a.xlsx")
# step_2("part_b.xlsx")
# step_2("part_c.xlsx")   
step_3("part_a_trans.xlsx")
    