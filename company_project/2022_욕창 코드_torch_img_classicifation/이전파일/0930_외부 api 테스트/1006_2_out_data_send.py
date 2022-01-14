import requests

    # files={"file": open(img_path+file,'rb')}
datas={"infection":1, #1-있음/0-없음
    "sagang":1, #1-있음/0-없음
    "skin_state":1, #1- 건강하지 않음/0-건강함
    "exudate_amount":3, #0~4 소량~다량
    "stage":3 }
# dict_list={}

# coordinates =json.dumps(coordinates)
resp = requests.post("http://seven.iacryl.com:65282/dressing",data=datas)
# resp = requests.post("http://192.168.0.241:9001/dressing",data=datas)

print("resp")
print(resp)
print()
res = resp.json()
print("res")
print(res)