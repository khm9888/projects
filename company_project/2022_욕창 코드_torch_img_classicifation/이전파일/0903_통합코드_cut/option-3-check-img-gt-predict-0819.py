import pandas as pd

# # ################## step1#####################


# #######################################################################

# #######################################################################
print("test")
test = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/test.csv")
print(test)
img_list = list()
for img in test["img_path"]:
    img_list.append(img[:-(len(img.rsplit("_")[-1])+1)]+".JPG")
    
df2=pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/test.csv")

df = pd.DataFrame({"img":img_list,"predict" : df2["predict"],"true":df2["true"]})
# #######################################################################
print(df)

df.to_csv("/home/ubuntu/con/code/check_img_true/check.csv",index=0)

################## step2#####################

# 폴더생성

import os
 
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
directory_path = "/home/ubuntu/con/code/check_img_true/"

for i in range(6):
    for j in range(6):  
        createFolder(f"{directory_path}/{i}/{j}")

################## step3 #####################
## 이미지 생성

df3 = pd.read_csv("/home/ubuntu/con/code/check_img_true/check.csv")
# print(df3)

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

from PIL import Image

load_img_loc = "/home/ubuntu/Data/upload_file/"
save_img_loc = "/home/ubuntu/con/code/check_img_true/"
# print(len(df3))#2197

from tqdm import tqdm

for i in tqdm(range(len(df3))):
    img = df3.iloc[i]["img"]
    predict = df3.iloc[i]["predict"]
    true = df3.iloc[i]["true"]
    # print((load_img_loc+img)[0])
    # input()
    image1 = Image.open(load_img_loc+img)
    img_name = img.rsplit(".")[0]
    image1.save(f"{save_img_loc}/{true}/{predict}/{img_name}_{true}_{predict}.png")
    
################## step4 #####################

