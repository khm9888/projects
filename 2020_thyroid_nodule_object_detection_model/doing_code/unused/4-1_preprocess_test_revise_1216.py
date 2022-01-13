import cv2
import numpy as np
import json
import os
# preprocess_img_path="/home/con/mmdetection/data/thyroid/preprocess/"

# preprocess_img_path="/mnt/sdb/AI/work/prepro_img/"
original_img_path = "/home/con/mmdetection/data/thyroid/data/"
json_path = "/home/con/mmdetection/data/thyroid/annotations/"
# img_save_path = "/mnt/sdb/AI/work/save_img/"
img_save_path = "/mnt/sdb/AI/work/test_img/"

blue_color = (255, 0, 0)
red_color = (0, 0, 255)

def createFolder(directory):#폴더 생성 함수
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


with open(img_save_path+"savefile2.json","r") as jsonfile:#bbox 작업 기록이 있는 json파일을 불러옵니다.
    save=json.load(jsonfile) 


with open(f"{json_path}from_db.json","r") as jsonfile:#bbox 작업 기록이 있는 json파일을 불러옵니다.
    json_data=json.load(jsonfile) 

image_data = json_data["images"]

def module_1(image,threshold,cnt):
    
    print("type(cnt)")    
    print(type(cnt))    

    # threshold = int(input("threshold 몇?"))
    print("image")
    print(image)
    file_name = image["file_name"]
    user_id = image["user_id"]
    maker_id = image["maker_id"]
    img_id = image["id"]
    print("maker_id")
    print(maker_id)
    if file_name not in save:
        cnt+=1
        print("module1")
        img = cv2.imread(f'{original_img_path}{file_name}')
        height = img.shape[0]
        width = img.shape[1]
        print(img.shape[0])#height
        print(img.shape[1])#width
        
        img = img.astype(int)
        
        origin_img = img.copy()

        img_r, img_g, img_b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        img_rg, img_gb, img_br = np.abs(img_r - img_g), np.abs(img_g - img_b), np.abs(img_b - img_r)
        img_d = img_rg + img_gb + img_br
        # print(img)
        print("img_rg, img_gb, img_br")
        print(img_rg, img_gb, img_br)
        print("img_d")
        print(img_d)
        edit_list = []
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img_d[i, j] > threshold :
                    edit_list.append([i, j])

        for e in edit_list:
            y, x = e
            for i in range(y - 1, y + 2):
                for j in range(x - 1, x + 2):
                    random_choice = []
                    try:
                        for ii in range(-10, 11, 1):
                            random_choice.append(img[i + ii, j - 20, :])
                            try:
                                random_choice.append(img[i + ii, j + 20, :])
                            except:
                                pass
                        for jj in range(-10, 11, 1):
                            random_choice.append(img[i - 20, j + jj, :])
                            try:
                                random_choice.append(img[i + 20, j + jj, :])
                            except:
                                pass
                        sel = np.random.randint(0, 83)
                        img[i, j, :] = random_choice[sel]
                    except:
                        pass
                    
        # as gray
        img = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3
        # img = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2])
        img = img.astype(int)

        newimg = np.copy(img)
        for e in edit_list:
            y, x = e
            try:
                for i in range(y - 1, y + 2):
                    for j in range(x - 1, x + 2):
                        if i<height and j<width:
                            avg = np.average(img[i - 1:i + 2, j - 1:j + 2])
                            newimg[i, j] = avg
            except:
                pass
        newimg= newimg.astype(np.uint8)
        cv2.imwrite(f"{preprocess_img_path}/{maker_id}/{file_name}",origin_img)

        cv2.imwrite(f"{preprocess_img_path}/{maker_id}/{file_name.split('.')[0]}_{maker_id}_.{file_name.split('.')[1]}",newimg)
        cv2.imwrite(f"{preprocess_img_path}//{file_name}",newimg)
        
        save[file_name]=[img_id,user_id,maker_id]
    return cnt
  
def draw_rectangle(image,cnt):

    file_name = image["file_name"]
    img_id = image["id"]
    maker_id = image["maker_id"]
    user_id = image["user_id"]
    split_values=file_name.split(".")
    name,format0=file_name[:-(len(split_values[-1])+1)],split_values[-1]
    
    if file_name not in save:
        
    # print(dict_image)
        
        # img = np.zeros((384, 384, 3), np.uint8)
        # img = cv2.imread(preprocess_img_path+file_name)
        img = cv2.imread(original_img_path+file_name)
        # cv2.imwrite(f"{preprocess_img_path}{file_name}",img) # 전처리하기 전에 넣음
        for anno in json_data["annotations"]:
            if anno["image_id"]==img_id:
                thyroid_type=anno["category_id"]#1 or 2
                values=anno["bbox"]
                if thyroid_type==1:
                    color = blue_color
                elif thyroid_type==2:
                    color = red_color
                img = cv2.rectangle(img, (values[0], values[1]), (values[0]+values[2], values[1]+values[3]), color, 1)
        
        cnt+=1
        print(f"{img_save_path}{name}_maker_id_{maker_id}.{format0}")
        # cv2.imshow(name,img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        cv2.imwrite(f"{img_save_path}{name}_maker_id_{maker_id}_.{format0}",img)#id까지 표시했습니다.

    return cnt
 
cnt=0

# thresholds = [15,35,50]
# thresholds = [60,70,80,90,100,110]
thresholds = [110]
for threshold in thresholds:
    # preprocess_img_path=f"/mnt/sdb/AI/work/preprocess_{threshold}/"
    preprocess_img_path="/home/con/mmdetection/data/thyroid/preprocess/"
    
    for j in range(10):
        createFolder(preprocess_img_path+f"{j}")
    for i,image in enumerate(image_data[3000:3001]):
        # print(f"--{i}--")
        print(i)
        cnt=module_1(image,threshold,cnt)
            # cnt=draw_rectangle(image,cnt)

print(f"cnt:{cnt}")
print(f"cnt_total:{len(image_data)}")

with open(img_save_path+"savefile.json","w") as jsonfile:
    json.dump(save,jsonfile)