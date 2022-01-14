import requests
import json
import os
import numpy as np
import pdb
import datetime

import argparse

classes = ["benign","malign"]

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#
year_month_day,times=date[:8],date[8:]


img_path = '/home/con/mmdetection/data/thyroid/test/'+year_month_day+"/"
createFolder(img_path)
createFolder(img_path+"/result/")

# with open(json_save_path+"result.json","w",encoding="utf-8") as file:
#     json.dump(dict(),file,ensure_ascii=False)

result=[]

filelist = os.listdir(img_path)
filelist.sort()

body_param=dict()
# print(filelist)
for i,file in enumerate(filelist[:-1]):
    print("file_name")
    print(file)
    print()

    body_param[f'file{i}'] =  open(img_path+file, 'rb')
print(body_param)

req = requests.post('http://192.168.0.241:5005/', files=body_param) # 68:7879
print("req")
print(req.text)

res = json.loads(req.text)
print(type(res))

result = list(res.values())

result_filter=[]
for r in result:
    print("r")
    print(r)
    bbox_filter={classes[0]:[],classes[1]:[]}
    # print(r.keys())
    print(r["bbox"][classes[0]])
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


print(result_filter)

with open(img_path+"/result/result.json","w") as jsonfile:
    json.dump(result_filter,jsonfile)
    
    
