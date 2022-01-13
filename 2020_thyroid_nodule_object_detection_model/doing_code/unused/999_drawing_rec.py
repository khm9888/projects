import numpy as np
import cv2
import json

blue_color = (255, 0, 0)
# green_color = (0, 255, 0)
red_color = (0, 0, 255)
white_color = (255, 255, 255)

path = "/home/con/mmdetection/data/thyroid/annotations/"
img_path = "/mnt/sdb/AI/work/preprocess/"
# img_path = "/mnt/sdb/AI/data/"
img_save_path = "/mnt/sdb/AI/work/save_img/"

# save={}

# with open(img_save_path+"savefile.json","w") as jsonfile:
#     json.dump(save,jsonfile)

with open(img_save_path+"savefile.json","r") as jsonfile:#bbox 작업 기록이 있는 json파일을 불러옵니다.
    save=json.load(jsonfile) 

with open(path+"from_db.json") as file:#당일까지 업로드 된 데이터, json을 가져옵니다.
    data=json.load(file)
dict_image = data["images"]

def draw_rectangle(image,cnt):
    file_name = image["file_name"]
    img_id = image["id"]
    user_id = image["user_id"]
    split_values=file_name.split(".")
    name,format0=file_name[:-(len(split_values[-1])+1)],split_values[-1]
    
    if file_name not in save:
        
    # print(dict_image)

        # img = np.zeros((384, 384, 3), np.uint8)
        img = cv2.imread(img_path+file_name)
        for anno in data["annotations"]:
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
        print(f"{img_save_path}{name}_{user_id}{format0}")
        cv2.imwrite(f"{img_save_path}{name}_userid_{user_id}_.{format0}",img)#id까지 표시했습니다.
        save[file_name]=[img_id,user_id]
        # print(file_name)
        cv2.imshow(file_name,img)
        
        # img = cv2.imread(img_save_path+name+"_annotation."+format0)
        # cv2.imshow(img_save_path+name+"_annotation."+format0,img)
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    
    return cnt




print(f"cnt:{cnt}")
print(f"cnt_total:{len(dict_image)}")

with open(img_save_path+"savefile.json","w") as jsonfile:
    json.dump(save,jsonfile)

cnt=0
for image in dict_image:
    cnt=draw_rectangle(image,cnt)

print(f"cnt:{cnt}")
print(f"cnt_total:{len(dict_image)}")
    