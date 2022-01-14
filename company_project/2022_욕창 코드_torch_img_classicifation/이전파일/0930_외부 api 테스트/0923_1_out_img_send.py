import requests
import os
import json

# img_path = '/home/lab/bedsore-ai/api/test_images/'
img_path = '/home/lab/bedsore-ai/api/test/'
# img_path = 'C://Users/Acryl/Desktop/test/'

# img_path = '/home/con/test/'

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
    # coordinates={"coordinate":[str([100,200,200,300])]}
    coordinates={"coordinate":[100,200,200,300]}
    # dict_list={}
    
    # coordinates =json.dumps(coordinates)
    # resp = requests.post("http://seven.iacryl.com:65281/predict",files = files,data=coordinates)
    # print()
    # resp = requests.post("http://192.168.0.241:8001/predict", files=files,data=coordinates)
    resp = requests.post("http://115.71.28.90:8001/predict", files=files,data=coordinates)

    print("resp")
    print(resp)
    print()
    res = resp.json()
    print("res")
    print(res)