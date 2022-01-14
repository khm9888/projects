import requests
import os
import json

# dict_list={}

# coordinates =json.dumps(coordinates)
resp = requests.post("http://localhost:9001/dressing",data={"c1":False,"c2":True,"c3":True,"c4":True,"cls_no":4})
# resp = requests.post("http://localhost:8557/predict/", files={"file": open(img_path+file,'rb')})

print("resp")
print(resp)
print()
res = resp.json()
print("res")
print(res)