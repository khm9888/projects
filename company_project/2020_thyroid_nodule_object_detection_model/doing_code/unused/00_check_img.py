import json
import cv2
import pandas as pd
import datetime


img_path="/mnt/sdb/AI/data/"
load_path="/home/con/mmdetection/data/thyroid/annotations/"
save_path="/mnt/sdb/AI/work/filter_img/"

blue_color = (255, 0, 0)
# green_color = (0, 255, 0)
red_color = (0, 0, 255)
white_color = (255, 255, 255)

date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#
year_month_day,times=date[:8],date[8:]



with open(load_path+"from_db_1016.json","r") as jsonfile:#bbox 작업 기록이 있는 json파일을 불러옵니다.
    load_data=json.load(jsonfile)
    
with open(save_path+"filter.json","r") as jsonfile:
    save_data=json.load(jsonfile)
    
images=load_data["images"]#image만 추출
# print(images)
# print(type(images)) 

def draw_rectangle(image,cnt):
    file_name = image["file_name"]
    img_id = image["id"]
    user_id = image["user_id"]
    split_values=file_name.split(".")
    name,format0=file_name[:-(len(split_values[-1])+1)],split_values[-1]
    
    if file_name not in save_data:
        
    # print(dict_image)

        # img = np.zeros((384, 384, 3), np.uint8)
        img = cv2.imread(img_path+file_name)
        for anno in load_data["annotations"]:
            if anno["image_id"]==img_id:
                thyroid_type=anno["category_id"]#1 or 2
                values=anno["bbox"]
                if thyroid_type==1:
                    color = blue_color
                elif thyroid_type==2:
                    color = red_color
                elif thyroid_type==0:
                    color = white_color
                img = cv2.rectangle(img, (values[0], values[1]), (values[0]+values[2], values[1]+values[3]), color, 1)
        
        cnt+=1
        cv2.imshow(name,img)
        v=cv2.waitKey()
        if v==49:
            print("case1")
            print("-"*30)
            case=1
        elif v==50:
            print("case2")
            print("-"*30)
            case=2
        elif v==51:
            print("case3")
            print("-"*30)
            case=3            
        elif v==52:
            print("case4")
            print("-"*30)
            case=4        
        else:
            print("pass-->case5")
            print("-"*30)
            case=5    
        path = f"{save_path}/type{case}/"
        cv2.destroyAllWindows()
        print(f"cnt:{cnt}")
        cv2.imwrite(f"{path}{name}.{format0}",img)#id까지 표시했습니다.
        save_data[file_name]=[img_id,user_id,case]
    return cnt


cnt=0
for i,image in enumerate(images):
    cnt=draw_rectangle(image,cnt)
    c=1650
    if i==c:
        print(f"현재 {i+1}개 했습니다")
        with open(save_path+"filter.json","w") as jsonfile:
            json.dump(save_data,jsonfile)
        with open(f"{save_path}/filter/{year_month_day}_{times}.json","w") as json_file:
            json.dump(save_data,json_file)   
            
        df = pd.DataFrame(save_data)
        df = df.transpose()
        df.to_csv(f"{save_path}filter.csv")
        # if choice=="1" or choice=="2":
        break            
               
            
with open(save_path+"filter.json","w") as jsonfile:
            json.dump(save_data,jsonfile)
df = pd.DataFrame(save_data)
df = df.transpose()
df.to_csv(f"{save_path}filter.csv")


