


import pandas as pd
import os

data = pd.read_excel("/home/ubuntu/Data/uploud_20210707.xlsx")#origin xlsx file
print(data.head)

print(f"data 길이 : {len(data)}")#10983

# copy_data=data.drop_duplicates(["파일명"],keep="first")#중복 이미지 제거
# print(f"data 길이 : {len(copy_data)}")

#키를 파악하고,
print(data.keys())

#키에서 파일명과 cordinate 값만 가져온다.
data_keys=list(data.keys())
print(data_keys)#['파일명', '욕창단계', '조직유형', '사진 코멘트', '욕창부위', '욕창크기_최대길이_cm', '욕창크기_최대폭_cm', '삼출물', 'dressing', 'x1', 'y1', 'x2', 'y2', '상태', '최종단계']

data_used_keys = data_keys[0:2]+data_keys[-6:-2]
print(data_used_keys)#['파일명', '욕창단계', 'x1', 'y1', 'x2', 'y2']
base_keys =["img_path","cls", 'x1', 'y1', 'x2', 'y2']

print(type(data))#df 추측

copy_data = data.copy()
print(copy_data.head())
copy_data = copy_data.iloc[:,[0,1,-6,-5,-4,-3]]#활용하는 6개의 값만 가져옴.
copy_data.columns= base_keys#column명 변경.
print()
print(copy_data.head())

# base["img_path"]=copy_data["file_names"].replace(copy_data["file_names"][1][-4:],"_rename.png")

print(set(copy_data["cls"]))#{'4단계', '심부조직손상', '1단계', '미분류', '2단계', '3단계'}
change_value_dict = {'4단계':4, '심부조직손상':5, '1단계':1, '미분류':0, '2단계':2, '3단계':3}

copy_data=copy_data.replace({"cls":change_value_dict})
print(39,copy_data.head())

# print(copy_data.keys())
# base[base_keys[1]]=
names = list()
for name in copy_data["img_path"]:
    names.append(name.rsplit(".")[0]+"_rename.png")
    
# copy_data.rename(columns={"file_names":"img_path"})
copy_data["img_path"]=names

print()
print(copy_data.head())

copy_data.to_csv("/home/ubuntu/con/code/BiT/data/labels/data.csv",index=0)

print("len(copy_data)")
print(len(copy_data))





# ###################################### # crop 이미지 처리 완료 ##############################
#save img loc
load_img_loc = "/home/ubuntu/Data/upload_file/"
save_img_loc = "/home/ubuntu/con/code/save_img_0817/"



def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createFolder(save_img_loc)


from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# 
from PIL import Image



for i in range(len(copy_data)):
    file=data.iloc[i]['파일명']
    cls_name=copy_data.iloc[i]["cls"]
    x1=copy_data.iloc[i]['x1']
    y1=copy_data.iloc[i]['y1']
    x2=copy_data.iloc[i]['x2']
    y2=copy_data.iloc[i]['y2']
    print(f"번호 : {i}")
    print(f"파일명 : {file}")
    
    image1 = Image.open(load_img_loc+file)
    rename_file = file.rsplit(".")[0]+"_rename.png"
    # image1.show()

    #이미지의 크기 출력
    print(image1.size)
    print(x1,y1,x2,y2)
    # 이미지 자르기 crop함수 이용 ex. crop(left,up, rigth, down)
    croppedImage=image1.crop((x1,y1,x2,y2))
    # croppedImage.show()
    # print("잘려진 사진 크기 :",croppedImage.size)
    
    croppedImage.save(save_img_loc+rename_file)

# ###################################### # crop 이미지 처리 완료 ##############################