import numpy as np
from sklearn.model_selection import KFold
import pandas as pd
from sklearn.model_selection import train_test_split


print("data")
data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/data_selected.csv")

kfold = KFold(n_splits=5,random_state=42,shuffle=True)

for i,(train_index, test_index) in enumerate(kfold.split(data)):
    # print("train_index, test_index")
    # print(train_index, test_index)
    # print("train, valid")
    
    train_unsplited,test = data.iloc[train_index], data.iloc[test_index]
    train,val = train_test_split(train_unsplited,test_size=0.125,random_state=42)
    
    train.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/train_{i}.csv",index=0)
    data_2 = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/train_{i}.csv")
    print(data_2)

    val.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/val_{i}.csv",index=0)
    data_2 = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/val_{i}.csv")
    print(data_2)

    test.to_csv(f"/home/ubuntu/con/code/BiT/data/labels/test_{i}.csv",index=0)
    data_2 = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/test_{i}.csv")
    print(data_2)
