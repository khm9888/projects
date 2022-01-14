import requests
import json
import os
import numpy as np
import pdb

import argparse
import base64 
import cv2


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

img_path = '/home/con/mmdetection/data/thyroid/data/'
json_path = "/home/con/mmdetection/data/thyroid/annotations/"
result_path = "/home/con/mmdetection/data/thyroid/preprocess/"
img_save_path = "/mnt/sdb/AI/work/test_img_2/"

filelist = os.listdir(img_path)
filelist.sort()
len(filelist)

# createFolder(img_path)
createFolder(result_path)

with open(img_save_path+"savefile.json","r") as jsonfile:#bbox 작업 기록이 있는 json파일을 불러옵니다.
    save=json.load(jsonfile) 
    
with open(f"{json_path}from_db.json","r") as jsonfile:#bbox 작업 기록이 있는 json파일을 불러옵니다.
    json_data=json.load(jsonfile) 

image_data = json_data["images"]

for i,file in enumerate(image_data):
    print(f"file {i}")
    file_name = file["file_name"]
    user_id = file["user_id"]
    maker_id = file["maker_id"]
    img_id = file["id"]
    print(file_name)

    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--image', type=str, help='.jpg', default=img_path+file_name)
        args = parser.parse_args()

        # request send 
        body_param = {'image': open(args.image, 'rb')}
        # req = requests.post('http://192.168.0.181:8556/extract_roi', files=body_param) # test extract_roi
        req = requests.post('http://192.168.0.181:8556/remove_marker', files=body_param) # test remove_marker
        # print(req.text)

        # save result 
        img_data = req.text
        im_bytes = base64.b64decode(img_data)
        im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
        img = cv2.imdecode(im_arr, 1)

        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]
        cv2.imwrite(result_path+file_name, img, encode_param)
        save[file_name]=[img_id,user_id,maker_id]
    
    if i%100==0:
        with open(img_save_path+"savefile.json","w") as jsonfile:
            json.dump(save,jsonfile)


with open(img_save_path+"savefile.json","w") as jsonfile:
    json.dump(save,jsonfile)