import pandas as pd
from collections import defaultdict
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from datetime import datetime
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# 
from PIL import Image

choice = ["0-0","0-1","0-2","0-3","0-4","0-5"]
# choice = ["0-0"]
# choice = ["0-1","0-2","0-4"]
# choice = ["0-3"]
###########################
# 0-0. 두 개의 xlsx 파일 합치는 코드
###########################
if "0-0" in choice:

    # data_1 = pd.read_excel("/home/ubuntu/Data/upload_20211029_1.xlsx",sheet_name=0)#origin xlsx file
    data_1 = pd.read_excel("/home/ubuntu/Data/upload_20211029_1.xlsx",sheet_name=1)#origin xlsx file
    # data_1 = pd.read_excel("/home/ubuntu/Data/upload_20211029_1.xlsx")#origin xlsx file
    data_keys=list(data_1.keys())
    print("data_keys_1")
    print(data_keys)
    
    # data_2 = pd.read_excel("/home/ubuntu/Data/upload_20211029_2.xlsx",sheet_name=0)#origin xlsx file
    data_2 = pd.read_excel("/home/ubuntu/Data/upload_20211029_2.xlsx",sheet_name=1)#origin xlsx file
    data_keys=list(data_2.keys())
    print("data_keys_2")
    print(data_keys)

    mask_1 = (data_1.상태!="제외")
    mask_2 = (data_2.상태!="제외")

    data_1 = data_1.loc[mask_1,:]
    data_2 = data_2.loc[mask_2,:]
    print(data_1)
    # print("len(data_1)")
    # print(len(data_1))
    print(data_2)

    data_df = pd.concat([data_1,data_2])

    data_df.to_csv("/home/ubuntu/Data/upload.csv",index=0)

    data_df_a = pd.read_csv("/home/ubuntu/Data/upload.csv")#origin xlsx file
    print(data_df_a)
###########################
# 0-0 완료
###########################

###########################
# 0-1. upload.csv 를 가져와서 원하는 값으로 변환 하여 data.csv 만드는 과정
###########################

#1_data_2_divide_0817

if "0-1" in choice:
    data = pd.read_csv("/home/ubuntu/Data/upload.csv")#origin xlsx file

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
    for name in copy_data["img_path"]:
        names.append(name.rsplit(".")[0]+"_rename.png")#짤라낸 사진으로 따로 전처리.

    base["img_path"]=names
    base["cls"]=copy_data["cls"]
    base["origin_path"]=copy_data["img_path"]
    base["x1"]=copy_data["x1"]
    base["y1"]=copy_data["y1"]
    base["x2"]=copy_data["x2"]
    base["y2"]=copy_data["y2"]

    print(base.head())

    base.to_csv("/home/ubuntu/con/code/BiT/data/labels/data.csv",index=0)


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
    data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/data.csv")
    # print(data)


    def cnt_data(file,dir_path="/home/ubuntu/con/code/BiT/data/labels"):
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
                
            
    cnt_data("data")
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
    dir_path=f'/home/ubuntu/con/code/BiT/data/labels/{today}'
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
        train.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/train_{i}.csv",index=0)
        print(train)
        val=val.sample(frac=1).reset_index(drop=True)
        val.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/val_{i}.csv",index=0)
        print(val)
        test=test.sample(frac=1).reset_index(drop=True)
        test.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/test_{i}.csv",index=0)
        print(test)
        
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
# 0-3. 원하는 폴더의 파일 개수 파악하는 코드
###########################

 #0_cnt_img_0809


if "0-3" in choice:
        
    def func_full_filenames(data_dir):  
        data_dir=os.path.dirname(os.path.abspath(f"{data_dir}/1.png"))#절대경로 변환
        # path to images
        filenames = os.listdir(data_dir)#해당 디렉토리에 이미지들을 리스트로 넣음
        # get a list of images
        full_filenames = [os.path.join(data_dir, f) for f in filenames]#경로까지 추가하여 모두 각각 저장함.
        # # get the full path to images

        # print(full_filenames)#경로저장
        print(len(full_filenames))#파일 몇개인지 파악
        return full_filenames

    # data_dir ='data/medetec/bedsore_01'

    path1 = "/home/ubuntu/con/code/BiT/data/images/"
    # path1 = "/home/ubuntu/Data/upload_file/"
    print(path1)
    full_filenames=func_full_filenames(path1)
    print()

    path1 = "/home/ubuntu/con/code/BiT/data/images_cut/"
    # path1 = "/home/ubuntu/Data/upload_file/"
    print(path1)
    full_filenames=func_full_filenames(path1)
    print()

    # path1 = "/home/ubuntu/con/code/BiT/data/images_uncut_0820/"
    # # path1 = "/home/ubuntu/Data/upload_file/"
    # print(path1)
    # full_filenames=func_full_filenames(path1)
    # print()

    # path2 = f"/home/ubuntu/con/code/BiT/data/save_img_{today}/"
    # print(path2)
    # full_filenames=func_full_filenames(path2)
    # print()

    # path3 = "/home/ubuntu/con/code/BiT/data/images/"
    # print(path3)
    # full_filenames=func_full_filenames(path3)
    # print()

###########################
# 0-3번 완료 
###########################



###########################
# 0-4. data_set을 기준으로 하여, crop 이미지 생성 코드
###########################


if "0-4" in choice:
        
    #save img loc

    today=datetime.today().date().strftime("%y%m%d")

    load_img_loc = "/home/ubuntu/Data/upload_file/"
    
    save_img_loc = f"/home/ubuntu/con/code/save_img_{today}/"

    data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/data.csv")

    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)
            
    createFolder(save_img_loc)


    # data_dir ='data/medetec/bedsore_01'

    path1 = "/home/ubuntu/con/code/BiT/data/images/"
    # path1 = "/home/ubuntu/Data/upload_file/"
    print(path1)
    filenames=os.listdir(path1)
    print(type(filenames))
    print(filenames)
    print()

    for i in range(len(copy_data)):
        file=data.iloc[i]['img_path']
        cls_name=copy_data.iloc[i]["cls"]
        x1=copy_data.iloc[i]['x1']
        y1=copy_data.iloc[i]['y1']
        x2=copy_data.iloc[i]['x2']
        y2=copy_data.iloc[i]['y2']
        file = file[:-len("_rename.png")]+".JPG"
        rename_file = file.rsplit(".")[0]+"_rename.png"
        if rename_file not in filenames:
            print(f"번호 : {i}")
            print(f"파일명 : {file}")
            image1 = Image.open(load_img_loc+file)
            # image1.show()

            #이미지의 크기 출력
            print(image1.size)
            print(x1,y1,x2,y2)
            # 이미지 자르기 crop함수 이용 ex. crop(left,up, rigth, down)
            croppedImage=image1.crop((x1,y1,x2,y2))
            # croppedImage.show()
            # print("잘려진 사진 크기 :",croppedImage.size)
            
            croppedImage.save(save_img_loc+rename_file)

###########################
# 0-4번 완료 
###########################



###########################
# 0-5. data_set을 기준으로 하여, crop 이미지 생성 코드
###########################

#0-2-revise_name_0817

if "0-5" in choice:
    i = 1

    train = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/train_{i}.csv")
    val = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/val_{i}.csv")
    test = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/test_{i}.csv")


    train.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/train.csv",index=0)
    val.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/val.csv",index=0)
    test.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/test.csv",index=0)

###########################
# 0-5번 완료 
###########################
