import requests
import os
import json
img_path = 'C://Users//Acryl//Desktop//test/'
# img_path = '/home/lab/burn/data/data/data_con/con_10000_211124/before_crop_data/images/'


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createFolder(img_path)
createFolder(img_path+"/result/")

# result=[]

filelist = os.listdir(img_path)[:5]
# filelist = os.listdir(img_path)
filelist.sort()


print(filelist)
for i,file in enumerate(filelist[:-1]):
    files={"image": open(img_path+file,'rb')}
    # coordinates={"coordinate":[524,1138,814,1852]}
    # coordinates={"coordinate":[814,524,1852,1138]}
    
    # coordinates={"coordinate":[1852,1138,814,524]}
    coordinates={"coordinate":[814,524,1852,1138]}
    resp = requests.post("http://192.168.0.241:8556/classify/",files = files,data=coordinates)
    # resp = requests.post("http://seven.iacryl.com:65307/classify/",files = files,data=coordinates)
    # resp = requests.post("http://115.71.28.90:8556/classify/",files = files,data=coordinates)
    
    # resp = requests.post("http://192.168.0.241:8556/classify/", files=files, data=coordinates)

    print("resp")
    print(resp)
    print()
    res = resp.json()
    print("res")
    print(res)