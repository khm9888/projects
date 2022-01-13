import json
import random

load_json_path = "/home/con/mmdetection/data/thyroid/annotations/"

with open(load_json_path+"concat.json","r") as file:
    data_db = json.load(file)

images_info=data_db["images"]
    
# print(len(images_info))

values = [v['file_name'] for v in images_info if v['width'] ==1280]


values_extract_10times = [v for i,v in enumerate(values) if i%10==0 ]
random.shuffle(values_extract_10times)
values_extract_10times = values_extract_10times[:20]

print(len(values_extract_10times))
values_extract_10times.sort()
print(values_extract_10times)
with open(load_json_path+"extract.json","w") as file:
    json.dump(values_extract_10times,file)