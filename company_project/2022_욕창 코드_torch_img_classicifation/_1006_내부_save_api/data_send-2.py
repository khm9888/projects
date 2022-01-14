import requests

    # files={"file": open(img_path+file,'rb')}
datas={"infection":1, #1-있음/0-없음
    "sagang":1, #1-있음/0-없음
    "skin_state":0, #1- 건강하지 않음/0-건강함
    "exudate_amount":2, #0~4 소량~다량
    "stage":3 }
# dict_list={}

# coordinates =json.dumps(coordinates)
resp = requests.post("http://seven.iacryl.com:65282/dressing",
                    data=datas)
# resp = requests.post("http://localhost:8557/predict/", files={"file": open(img_path+file,'rb')})

print("resp")
print(resp)
print()
res = resp.json()
print("res")
print(res)