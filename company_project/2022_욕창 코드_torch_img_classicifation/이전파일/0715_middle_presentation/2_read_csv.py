import pandas as pd
from scipy.sparse.construct import random
# from sklearn.model_selection import train_test_split

# # # #######################################################################
# # # #cls

# # data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/cls.csv")
# # print(data)
# # # data["cls"]=['미분류' , '1단계',  '2단계', '3단계', '4단계', '심부조직손상']
# # data["cls"]=[0,1,2,3,4,5]
# # data.to_csv("/home/ubuntu/con/code/BiT/data/labels/cls_2.csv",index=0)
# # data_2 = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/cls_2.csv")
# # print(data_2)

# # #한글로 등급 나눈 것을 0~5로 클래스바꿈

# # #######################################################################

# # #######################################################################
# # #train
# # print("train")
# # data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/train.csv")
# # print(data)

# # #######################################################################

# # #######################################################################
# # #test
# # print("test")
# # data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/test.csv")
# # print(data)

# # #######################################################################

# # #######################################################################
# # #val
# # print("val")
# # data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/val.csv")
# # print(data)

# # #######################################################################
# #######################################################################
# #data
print("data")
data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/data.csv")
print(data)

# train,test=train_test_split(data,test_size=0.2,random_state=42)

# train.to_csv("/home/ubuntu/con/code/BiT/data/labels/train_2.csv",index=0)
# data_2 = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/train_2.csv")
# print(data_2)

# test.to_csv("/home/ubuntu/con/code/BiT/data/labels/test_2.csv",index=0)
# test.to_csv("/home/ubuntu/con/code/BiT/data/labels/val_2.csv",index=0)#test = val 로 우선 저장
# data_2 = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/test_2.csv")
# print(data_2)

# #######################################################################

# #######################################################################
# df2=pd.read_csv("/home/ubuntu/con/code/BiT/test.csv",index_col=0)
# print("df2")
# print(df2)

# #############################################################
# 

# # #############################################################
# # how is many patient in data?

# # #data 개수 파악하는 코드

# import pandas as pd

# print("data")
# data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/data.csv")
# print(data.keys())
# numbers = list()
# for data in data["img_path"]:
#     numbers.append(str(data).split("_")[0])
# print(len(set(numbers)))    

#코드 추가 필요1 - 폴더 안에 데이터 개수는?

#코드 추가 필요2 - 각 환자번호 당 개수는??
    
# # #############################################################