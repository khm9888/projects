# # #############################################################

from collections import defaultdict

import pandas as pd


def cnt(num):
    cnt_dict=defaultdict(int)
    print("train")
    train = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/train_{num}.csv")
    print("val")
    val = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/val_{num}.csv")
    for c in train["cls"]:
        cnt_dict[c]+=1
        
    for c in val["cls"]:
        cnt_dict[c]+=1
    print("총개수",sum(cnt_dict.values()))
    return cnt_dict

def cnt_2(num):
    cnt_dict=defaultdict(int)
    print("test")
    test = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/test_{num}.csv")

    for c in test["cls"]:
        cnt_dict[c]+=1

    print("총개수",sum(cnt_dict.values()))
    return cnt_dict


cnt_dict=defaultdict(int)
train = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/train.csv")
for c in train["cls"]:
    cnt_dict[c]+=1
for c in range(6):
    print(c,cnt_dict[c])
    
cnt_dict=defaultdict(int)
test = pd.read_csv(f"/home/ubuntu/con/code/BiT/data/labels/test.csv")
for c in test["cls"]:
    cnt_dict[c]+=1
for c in range(6):
    print(c,cnt_dict[c])
    
#######################

for i in range(5):
    print("#"*50)
    cnt_dict=cnt(i)
    for j in range(6):
        print(f"cnt_dict_{i}")
        print(f"{j}:{cnt_dict[j]}")
    print("#"*50)


#######################
    ##############################
for i in range(5):
    print("#"*50)
    cnt_dict=cnt_2(i)
    for j in range(6):
        print(f"cnt_dict_{i}")
        print(f"{j}:{cnt_dict[j]}")
    print("#"*50)
    ##############################