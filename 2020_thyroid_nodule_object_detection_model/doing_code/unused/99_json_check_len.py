import json


# path = "/home/con/mmdetection/data/coco/annotations/"
path = "/mnt/sdb/AI//work/save_img/"

with open(f"{path}savefile.json","r") as file:
    data_coco= json.load(file)

#<class 'dict'>
dict_count=dict()

for d in data_coco:
    if d[8:10] in dict_count:
        dict_count[d[8:10]]+=1
    else:
        dict_count[d[8:10]]=1
print(dict_count)