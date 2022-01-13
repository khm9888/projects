import requests
import json
import os
import numpy as np
import pdb
import datetime
import argparse
import cv2 
import jsonpickle
import PIL.Image
import base64

# from flask import make_response

classes = ["benign","malign"]
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#
year_month_day,times=date[:8],date[8:]


# img_path = '/home/con/mmdetection/data/thyroid/test/'+year_month_day+"/"
img_path = '/home/con/mmdetection/data/thyroid/test/test/'
createFolder(img_path)
createFolder(img_path+"/result/")

result=[]

filelist = os.listdir(img_path)
filelist.sort()


body_param=dict()

for i,file in enumerate(filelist[:-1]):
    print("img_path+file")
    print(img_path+file)

    body_param[f'{file}'] = open(img_path+file,"rb")

print(body_param)

print("--request--")
req= requests.post('http://192.168.0.181:5005/', files=body_param) # 68:7879
print(req)

print("--respond--")

res = req.json()
res = json.loads(req.text)

result = list(res.values())
        
result_filter=[]
for r in result:
    print(r.keys())
    print(r["bbox"])
    img = r["bbox_file"]
    name = r["file_name"].rsplit(".")[0]
    print(name)
    ext = r["file_name"].rsplit(".")[1]
    
    d = base64.b64decode(img)

    print("predict_result")
    print(r["predict_result"])

    temp_img = np.asarray(bytearray(d), dtype='uint8')
    temp_img = cv2.imdecode(temp_img, cv2.IMREAD_COLOR)
    cv2.imwrite(img_path+"/result/"+name+"_result"+'.'+ext, temp_img)

    
    print('Done!')
    # cv2.imshow("text",img)
    # cv2.waitKey(0)
    
        # print("r")
        # print(r)
    bbox_filter={classes[0]:[],classes[1]:[]}
    # print(r)
    if len(r["bbox"][classes[0]])!=0:
        for i,v in enumerate(r["bbox"][classes[0]]):
            values=list(map(int,v[0:4]))
            values.append(v[4]) 
            bbox_filter[classes[0]].append(values)

    if len(r["bbox"][classes[1]])!=0:
        for i,v in enumerate(r["bbox"][classes[1]]):
            values=list(map(int,v[0:4]))
            # print("2-v[4]")
            # print(v[4])
            values.append(v[4])
            bbox_filter[classes[1]].append(values)

            r["bbox"]=bbox_filter

    result_filter.append(r) 

# print("result_filter")
# print(result_filter)

with open(img_path+"/result/result.json","w") as jsonfile:
    json.dump(result_filter,jsonfile)
    
    
