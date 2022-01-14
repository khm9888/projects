from datetime import datetime
import pandas as pd
import json
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from collections import defaultdict
from tqdm import tqdm

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from PIL import Image

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# choice = ["0-1","0-2"]
# choice = ["0-1","0-2","0-3","0-4","0-5"]
choice = ["0-5"]


###########################
# 0-1. upload.csv 를 가져와서 원하는 값으로 변환 하여 data_uncut.csv 만드는 과정
###########################

#1_data_2_divide_0817

if "0-1" in choice:
    data = pd.read_csv("/home/ubuntu/Data/upload_uncut.csv")#origin xlsx file

    ####### data 2가 추가 됐으니. 코드 추가하도록 해야함. ########

    # print(data.head)

    # print(f"data 길이 : {len(data)}")#10983

    #키를 파악하고,
    base=pd.DataFrame()
    # print(data.keys())

    #키에서 파일명과 cordinate 값만 가져온다.
    data_keys=list(data.keys())
    # print(data_keys)#['파일명', '욕창단계', '조직유형', '사진 코멘트', '욕창부위', '욕창크기_최대길이_cm', '욕창크기_최대폭_cm', '삼출물', 'dressing', 'x1', 'y1', 'x2', 'y2', '상태', '최종단계']

    data_used_keys = data_keys[0:2]+data_keys[-6:-2]
    # print(data_used_keys)#['파일명', '욕창단계', 'x1', 'y1', 'x2', 'y2']
    base_keys =["img_path","cls", 'x1', 'y1', 'x2', 'y2']

    print(type(data))#df 추측


    copy_data = data.copy()
    # print(copy_data.head())
    copy_data = copy_data.iloc[:,[0,1,-6,-5,-4,-3]]#활용하는 6개의 값만 가져옴.
    copy_data.columns= base_keys#column명 변경.

    # base["img_path"]=copy_data["img_path"].replace(copy_data["img_path"][1][-4:],"_rename.png")

    change_value_dict = {'4단계':4, '심부조직손상':5, '1단계':1, '미분류':0, '2단계':2, '3단계':3}

    copy_data=copy_data.replace({"cls":change_value_dict})
    # print()

    names = list()
    # for name in copy_data["img_path"]:
    #     names.append(name.rsplit(".")[0]+"_rename.png")#짤라낸 사진으로 따로 전처리.

    base["img_path"]=copy_data["img_path"]
    base["cls"]=copy_data["cls"]
    base["x1"]=copy_data["x1"]
    base["y1"]=copy_data["y1"]
    base["x2"]=copy_data["x2"]
    base["y2"]=copy_data["y2"]

    print(base.head())

    base.to_csv("/home/ubuntu/con/code/BiT/data/labels/data_uncut.csv",index=0)


###########################
# 0-1번 완료
###########################

###########################
# 0-2. 만들어진 data.csv를 train/valid/test 데이터로 5-fold 하여, 각 비율까지 그대로 맞춰 가져오고
#      각 가져온 파일의 개수를 출력해주는 코드
###########################
#1_data_2_divide_0817

if "0-2" in choice:
    # print("data")
    data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/data_uncut.csv")
    # print(data)


    def cnt_data(file,dir_path="/home/ubuntu/con/code/BiT/data_uncut/labels"):
        cnt_dict=defaultdict(int)
        print(f"{file}")
        data = pd.read_csv(f"{dir_path}/{file}.csv")
        # print(data)
        for c in data["cls"]:
            cnt_dict[c]+=1
        keys=list(cnt_dict.keys())
        keys.sort()
        max_i=-1
        max_value = 0
        for i in keys:
            print(f"{i}  {cnt_dict[i]}")
            if max_value<=cnt_dict[i]:
                max_i=i
                max_value=cnt_dict[i]
        return max_i,max_value
                
            
    cnt_data("data_uncut")
    # 0:886
    # 1:1055
    # 2:4103
    # 3:1966
    # 4:360
    # 5:2613

    data_0=data[data["cls"]==0]
    data_1=data[data["cls"]==1]
    data_2=data[data["cls"]==2]
    data_3=data[data["cls"]==3]
    data_4=data[data["cls"]==4]
    data_5=data[data["cls"]==5]
    # print(data_0)

    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)

    def divide_kfold(data,num,dir_path):
        kfold = KFold(n_splits=5,random_state=42,shuffle=True)
        for i,(train_index, test_index) in enumerate(kfold.split(data)):
            train_unsplited,test = data.iloc[train_index], data.iloc[test_index]
            train,val = train_test_split(train_unsplited,test_size=0.125,random_state=42)
            
            train.to_csv(f"{dir_path}/train_{num}_{i}.csv",index=0)
            train = pd.read_csv(f"{dir_path}/train_{num}_{i}.csv")
            # print(train)

            val.to_csv(f"{dir_path}/val_{num}_{i}.csv",index=0)
            val = pd.read_csv(f"{dir_path}/val_{num}_{i}.csv")
            # print(val)

            test.to_csv(f"{dir_path}/test_{num}_{i}.csv",index=0)
            test = pd.read_csv(f"{dir_path}/test_{num}_{i}.csv")
            # print(test)
        # return train,val,test

    # from time import strftime

    today=datetime.today().date().strftime("%y%m%d")
    dir_path=f'/home/ubuntu/con/code/BiT/data_uncut/labels/{today}'
    createFolder(dir_path)

    divide_kfold(data_0,0,dir_path)
    divide_kfold(data_1,1,dir_path)
    divide_kfold(data_2,2,dir_path)
    divide_kfold(data_3,3,dir_path)
    divide_kfold(data_4,4,dir_path)
    divide_kfold(data_5,5,dir_path)


    def merge_data(i,dir_path):
        train = pd.DataFrame()
        val = pd.DataFrame()
        test = pd.DataFrame()
        for num in range(6):
            add_train=pd.read_csv(f"{dir_path}/train_{num}_{i}.csv")
            train = pd.concat([train,add_train])
            add_val=pd.read_csv(f"{dir_path}/val_{num}_{i}.csv")
            val = pd.concat([val,add_val])
            add_test=pd.read_csv(f"{dir_path}/test_{num}_{i}.csv")
            test = pd.concat([test,add_test])
        train=train.sample(frac=1).reset_index(drop=True)
        train.to_csv(f"/home/ubuntu/con/code/BiT/data_uncut/labels/train_{i}.csv",index=0)
        val=val.sample(frac=1).reset_index(drop=True)
        val.to_csv(f"/home/ubuntu/con/code/BiT/data_uncut/labels/val_{i}.csv",index=0)
        test=test.sample(frac=1).reset_index(drop=True)
        test.to_csv(f"/home/ubuntu/con/code/BiT/data_uncut/labels/test_{i}.csv",index=0)
        
    merge_data(0,dir_path)
    merge_data(1,dir_path)
    merge_data(2,dir_path)
    merge_data(3,dir_path)
    merge_data(4,dir_path)

    ###################### 분리 후, data 비율 확인 ####################

    # train=pd.read_csv(f"{dir_path}/train.csv")
    for i in range(5):
        max_i,max_v=cnt_data(f"train_{i}")
        cnt_data(f"val_{i}")
        cnt_data(f"test_{i}")
    # cnt_data("train_1")
    # cnt_data("val_1")
    # cnt_data("test_1")
    # cnt_data("train_2")
    # cnt_data("val_2")
    # cnt_data("test_2")


###########################
# 0-2번 완료 
###########################

###########################
# 0-3. data_set을 기준으로 하여, crop 이미지 생성 코드
###########################

#0-2-revise_name_0817

if "0-3" in choice:
    i = 0

    train = pd.read_csv(f"/home/ubuntu/con/code/BiT/data_uncut/labels/train_{i}.csv")
    val = pd.read_csv(f"/home/ubuntu/con/code/BiT/data_uncut/labels/val_{i}.csv")
    test = pd.read_csv(f"/home/ubuntu/con/code/BiT/data_uncut/labels/test_{i}.csv")


    train.to_csv(f"/home/ubuntu/con/code/BiT/data_uncut/labels/train.csv",index=0)
    val.to_csv(f"/home/ubuntu/con/code/BiT/data_uncut/labels/val.csv",index=0)
    test.to_csv(f"/home/ubuntu/con/code/BiT/data_uncut/labels/test.csv",index=0)

###########################
# 0-3번 완료 
###########################
        
###########################
# 0-4. train/val/test.csv를 가져와서 json으로 생성하는 코드
###########################
if "0-4" in choice:
        
    def csv_to_json(file):
        path=f"/home/ubuntu/con/code/BiT/data_uncut/"
        data_path=f"{path}labels/{file}.csv"
        
        save_path=f"{path}json/"
        createFolder(save_path)
        save_json=f"{path}save_json/"
        createFolder(save_json)

        date=datetime.today().strftime('%Y%m%d%H%M%S')#
        year_month_day,times=date[:8],date[8:]

        data_df=pd.read_csv(data_path)

        print(data_df)

        base=dict() #json 만들기 위한 기본 딕셔너리 구조

        base["images"]=list()
        base["annotations"]=list()
        base["categories"]=list()
        for n in tqdm(range(len(data_df))):
            # print(data_df.iloc[n])
            file_name = data_df.iloc[n]["img_path"]
            # print("file_name")
            # print(file_name)
            # print(type(file_name))
            # cls = list(map(int,list(data_df.iloc[n]["cls"])))
            cls = int(data_df.iloc[n]["cls"])
            # print(data_df.keys())
            # print(data_df.iloc[n])
            bbox = [data_df.iloc[n,-4],data_df.iloc[n,-3],data_df.iloc[n,-2],data_df.iloc[n,-1]]
            bbox = list(map(int,bbox))
            image_dict=dict()
            image_dict["id"]=str(n)
            image_dict["img_path"]=file_name
            base["images"].append(image_dict)
            
            annotation_dict=dict()
            annotation_dict["id"]=f"{n}_1"
            annotation_dict["image_id"]=str(n)
            annotation_dict["category_id"]=str(cls)
            annotation_dict["bbox"]=bbox
            # for a in annotation_dict.values():
            #     print(a)
            #     print(type(a))
            #     # input()
            base["annotations"].append(annotation_dict)

        change_value_dict = {'4단계':4, '심부조직손상':5, '1단계':1, '미분류':0, '2단계':2, '3단계':3}
        for key, value in change_value_dict.items():
            category_dict=dict()
            category_dict["category"]=str(value)
            category_dict["grade_name"]=key
            base["categories"].append(category_dict)
            
        # print(base)
        # print(type(base))
        # print(base.keys())
        # print(base["images"])
        # print(len(base["images"]))
        # print('base["images"]')
        # input()
        # print(base["annotations"])
        # print('base["annotations"]')
        # input()
        # print(base["categories"])
        # print('base["categories"]')
        # input()
        
        with open(f"{save_path}{file}.json","w") as json_file:
            json.dump(base,json_file)
        with open(f"{save_json}{file}_{year_month_day}_{times}.json","w") as json_file:
            try:
                json.dump(base,json_file)
            except:
                print(json_file)
                
    # for num in range(5):
    for num in range(5):
        csv_to_json(f"train_{num}")
        csv_to_json(f"test_{num}")
        csv_to_json(f"val_{num}")


###########################
# 0-4. 완료
###########################



###########################
# 0-5. 이미지를 가져와서 train/val/test 별로 클래스에 따라 넣는 코드
###########################

if "0-5" in choice:
        
    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)

    def img_split(file):#train
        path = "/home/ubuntu/con/code/BiT/data_uncut/labels/"
        
        load_img_path = "/home/ubuntu/con/code/BiT/data_uncut/images_uncut/"
        data_df = pd.read_csv(f"{path}/{file}.csv")
        save_path = "/home/ubuntu/con/code/BiT/data_uncut/data/"
            
        # for folder_num in range(5):
            # createFolder(f"{save_path}/{file}/{folder_num}")
            # filter_df = data_df[data_df["cls"]==folder_num]
            # print("filter_df")
            # print(filter_df)
            # print(len(filter_df))
            # print(type(filter_df))
        for file_path in tqdm(data_df["img_path"]):
            img1 = Image.open(load_img_path+file_path)
            img1=img1.convert('RGB')
            createFolder(f"{save_path}/{file}/")
            img1.save(f"{save_path}/{file}/{file_path}")
                
    img_split("train")
    img_split("val") #val인지 valid 인지
    img_split("test")

###########################
# 0-5 완료
###########################
