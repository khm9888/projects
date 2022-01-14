import numpy as np
from sklearn.model_selection import KFold
import pandas as pd
from sklearn.model_selection import train_test_split


print("data_selected")
data_selected = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/data_selected.csv")

kfold = KFold(n_splits=5,random_state=42,shuffle=True)

print("data_ver2")
data_ver2 = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/data_ver2.csv")
print("data_ver2.keys()")
print(data_ver2.keys())

for i,(train_index, test_index) in enumerate(kfold.split(data_selected)):
    # print("train_index, test_index")
    # print(train_index, test_index)
    # print("train, valid")
    
    train_unsplited,test = data_selected.iloc[train_index], data_selected.iloc[test_index]
    pre_train,val = train_test_split(train_unsplited,test_size=0.125,random_state=42)
    
    print("data_ver2")
    data_ver2 = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/data_ver2.csv")
    print("data_ver2.keys()")
    print(data_ver2.keys())
    
    pre_train.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/pre_train/pre_train_{i}.csv",index=0)
    pre_train = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/pre_train/pre_train_{i}.csv")
        
    train=data_ver2[data_ver2["number"].isin(pre_train["number"])]
    print("train")
    # print((train))
    train.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/train_{i}.csv",index=0)

    val.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/val_{i}.csv",index=0)
    val = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/val_{i}.csv")
    # print(val)

    test.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/test_{i}.csv",index=0)
    test = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/test_{i}.csv")
    # print(test)

##############################################################################
##############################################################################
#pretrain 통해서, #data에서 가져와 train으로 변환




