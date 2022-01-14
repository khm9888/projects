import requests
import os
import json

img_path = '/home/con/test/'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createFolder(img_path)
createFolder(img_path+"/result/")

# result=[]

filelist = os.listdir(img_path)
filelist.sort()


print(filelist)
for i,file in enumerate(filelist[:-1]):
    files={"file": open(img_path+file,'rb')}
    coordinates={"coordinate":[527,748,676,892]}
    # dict_list={}
    
    # coordinates =json.dumps(coordinates)
    resp = requests.post("http://localhost:65281/predict",files = files,
                     data=coordinates)
    # resp = requests.post("http://localhost:8557/predict/", files={"file": open(img_path+file,'rb')})

    print("resp")
    print(resp)
    print()
    res = resp.json()
    print("res")
    print(res)