import requests
import os

img_path = '/home/ubuntu/con/test/'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createFolder(img_path)
# createFolder(img_path+"/result/")

# result=[]

filelist = os.listdir(img_path)
filelist.sort()

print(filelist)
for i,file in enumerate(filelist[:-1]):
    
    # resp = requests.post("http://localhost:8557/predict",
    #                  files={"file": open(img_path+file,'rb')})    
    resp = requests.post("http://localhost:8557/predict", 
                     files={"file": open(img_path+file,'rb')})

    print("resp")
    print(resp)
    print()
    res = resp.json()
    print("res")
    print(res)