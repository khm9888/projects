import pandas as pd
from scipy.sparse.construct import random
from sklearn.model_selection import train_test_split

# #######################################################################
# #cls


## description ##

## 전체 데이터에서 7:1:2로 나누어주는 코드 ##

print("data")
data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/data.csv")
print(data)

train,test=train_test_split(data,test_size=0.2,random_state=42)

train,val = train_test_split(train,test_size=0.125,random_state=42)

train.to_csv("/home/ubuntu/con/code/BiT/data/labels/train.csv",index=0)
train = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/train.csv")
print(train)

val.to_csv("/home/ubuntu/con/code/BiT/data/labels/val.csv",index=0)
val = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/val.csv")
print(val)

test.to_csv("/home/ubuntu/con/code/BiT/data/labels/test.csv",index=0)
test = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/test.csv")
print(test)
