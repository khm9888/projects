from os import listdir
from os.path import isfile, join
import numpy
import cv2
import keyboard             # 키보드 입력 
import pandas as pd
import json

checkpath="/mnt/sdb/AI/work/check_img/"
img_save_path ="/mnt/sdb/AI/work/test_img/"
img_load_path = "/home/con/mmdetection/data/thyroid/preprocess"

with open(checkpath+"checkfile.json","r") as jsonfile:#bbox 작업 기록이 있는 json파일을 불러옵니다.
    check=json.load(jsonfile) 
    
with open(img_save_path+"/savefile.json","r") as jsonfile:#bbox 작업 기록이 있는 json파일을 불러옵니다.
    save=json.load(jsonfile) 

cnt=0

check_imgs=[]
for file_name,ids in save.items():
    print(ids)
    split_values=file_name.split(".")
    name,format0=file_name[:-(len(split_values[-1])+1)],split_values[-1]
    img_id,user_id,maker_id=tuple(ids)
    if file_name not in check:
        img = cv2.imread(f"{img_load_path}/{name}.{format0}")
        # img = cv2.imread(f"{img_save_path}{name}.{format0}")
        cv2.imshow(f"{file_name}_maker_id_{maker_id}",img)
        cv2.resizeWindow('Resized Window', img.shape[0], img.shape[1])
        
        v=cv2.waitKey(0)
        if v==32:#space
            pass
            print("--pass--",file_name)
        else:
            check_imgs.append(file_name)
            print(f"--save--img_id:{img_id}_{file_name}")
            cv2.imwrite(f"{checkpath}{name}_userid_{user_id}_.{format0}",img)#id까지 표시했습니다.
        check[file_name]=save[file_name]
        cv2.destroyAllWindows()
    cnt+=1
    if cnt%100==0:
        with open(checkpath+"checkfile.json","w") as jsonfile:
            json.dump(save,jsonfile)
        break
    
    
onlyfiles = [ [f,f[:10],f[11:19]] for f in listdir(checkpath) if isfile(join(checkpath,f)) ]
dict_csv = pd.DataFrame(onlyfiles).sort_values(0).reset_index(drop=True)

print(f"cnt:{cnt}")
with open(checkpath+"checkfile.json","w") as jsonfile:
    json.dump(save,jsonfile)
    
dict_csv.to_csv("/mnt/sdb/AI/work/check.csv")
    
