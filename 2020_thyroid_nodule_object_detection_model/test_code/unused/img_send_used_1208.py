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
from io import BytesIO
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


img_path = '/home/con/mmdetection/data/thyroid/test/'+year_month_day+"/"
img_path = '/home/con/mmdetection/data/thyroid/test/test/'
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
    print("img_path+file")
    print(img_path+file)
    # body_param[f'{img_path+file}'] = cv2.imread(f"{img_path}{file}")
    body_param[f'{file}'] = open(img_path+file,"rb")
    # v=cv2.imread(f"{img_path}{file}")
    # print((v))
    # # v = np.array(v)
    # cv2.imshow("test",v)
print(body_param)


print("--request--")
req= requests.post('http://192.168.0.181:5005/', files=body_param) # 68:7879
print(req)
# print(value)
# req,img = value


# req = jsonpickle.decode(req)
print("--respond--")


# print(req.json())

res = req.json()
res = json.loads(req.text)
# print(type(res))

result = list(res.values())

# print(len(result))


        
result_filter=[]
for r in result:
    print(r.keys())
    print(r["bbox"])
    # print(r)
    # img_file.save(os.path.join(img_path, img_file.filename))
    # img_filepath = os.path.join(img_path, img_file.filename)
            
    # img_t=cv2.imread(img_filepath,cv2.IMREAD_COLOR)
    # print(type(r["bbox_file"]['py/reduce']))
    # print(r["bbox_file"])
    # print(type(r["bbox_file"]['py/b64']))
    # print(type(r["bbox_file"]))
    # img_path=r["bbox_file_path"]
    # params = {"path" :img_path}
    # img = requests.post('http://192.168.0.181:5005/image_load', data=params)
    # print(img)
    
    # decoded = base64.b64decode(img)
    # print(img)
    # img = np.array(cv2.imread(BytesIO(decoded))) 
    # img = np.array(Image.open(BytesIO(img))) 
    # img = make_response(img)
    # img.headers['Content-Type'] = f'image/{ext}'
    # img = r["bbox_file"]['py/reduce']
    img = r["bbox_file"]
    # print(img.keys())
    # print(img)
    # file_like = StringIO(img)
    # img = PIL.Image.open(file_like)
    # img = np.fromstring(img,dtype = np.uint8)
    # img = cv2.imencode(img, cv2.IMREAD_COLOR)
    # print(img)
    
    d = base64.b64decode(img)
    # print(d)
    temp_img = np.asarray(bytearray(d), dtype='uint8')
    temp_img = cv2.imdecode(temp_img, cv2.IMREAD_COLOR)
    cv2.imwrite('temp_img.jpg', temp_img)
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
    
    
