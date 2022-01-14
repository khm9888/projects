import pandas as pd
from collections import defaultdict
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from datetime import datetime
import os


data = pd.read_excel("/home/ubuntu/Data/uploud_20210707.xlsx")#origin xlsx file
# print(data.head)

# print(f"data 길이 : {len(data)}")#10983

# copy_data=data.drop_duplicates(["파일명"],keep="first")#중복 이미지 제거
# print(f"data 길이 : {len(copy_data)}")

#키를 파악하고,
base=pd.DataFrame()
# print(data.keys())

#키에서 파일명과 cordinate 값만 가져온다.
data_keys=list(data.keys())
# print(data_keys)#['파일명', '욕창단계', '조직유형', '사진 코멘트', '욕창부위', '욕창크기_최대길이_cm', '욕창크기_최대폭_cm', '삼출물', 'dressing', 'x1', 'y1', 'x2', 'y2', '상태', '최종단계']

data_used_keys = data_keys[0:2]+data_keys[-6:-2]
# print(data_used_keys)#['파일명', '욕창단계', 'x1', 'y1', 'x2', 'y2']
base_keys =["file_names","cls", 'x1', 'y1', 'x2', 'y2']

print(type(data))#df 추측

copy_data = data.copy()
# print(copy_data.head())
copy_data = copy_data.iloc[:,[0,1,-6,-5,-4,-3]]#활용하는 6개의 값만 가져옴.
copy_data.columns= base_keys#column명 변경.
# print()
# print(copy_data.head())

# base["img_path"]=copy_data["file_names"].replace(copy_data["file_names"][1][-4:],"_rename.png")

# print(set(copy_data["cls"]))#{'4단계', '심부조직손상', '1단계', '미분류', '2단계', '3단계'}
change_value_dict = {'4단계':4, '심부조직손상':5, '1단계':1, '미분류':0, '2단계':2, '3단계':3}

copy_data=copy_data.replace({"cls":change_value_dict})
# print()
# print(copy_data.head())

# print(copy_data.keys())
# base[base_keys[1]]=
names = list()
for name in copy_data["file_names"]:
    names.append(name.rsplit(".")[0]+"_rename.png")
base["img_path"]=names
base["cls"]=copy_data["cls"]

# print(base.head())

base.to_csv("/home/ubuntu/con/code/BiT/data/labels/data.csv",index=0)

##############################step 1 data.csv 생산 완료###########################


##############################step 2 divide 생산 시작###########################

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
    for i in keys:
        print(f"{i}  {cnt_dict[i]}")
        
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

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
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
    val=val.sample(frac=1).reset_index(drop=True)
    val.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/val_{i}.csv",index=0)
    test=test.sample(frac=1).reset_index(drop=True)
    test.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/test_{i}.csv",index=0)
    
merge_data(0,dir_path)
merge_data(1,dir_path)
merge_data(2,dir_path)
merge_data(3,dir_path)
merge_data(4,dir_path)

###################### 분리 후, data 비율 확인 ####################

# train=pd.read_csv(f"{dir_path}/train.csv")
for i in range(5):
    cnt_data(f"train_{i}")
    cnt_data(f"val_{i}")
    cnt_data(f"test_{i}")
# cnt_data("train_1")
# cnt_data("val_1")
# cnt_data("test_1")
# cnt_data("train_2")
# cnt_data("val_2")
# cnt_data("test_2")

print()