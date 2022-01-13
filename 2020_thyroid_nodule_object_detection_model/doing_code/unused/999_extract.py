import json
import random

load_json_path = "/home/con/mmdetection/"

with open(load_json_path+"filter.json","r") as file:
    data_db = json.load(file)

dict_data=data_db["response"]
    
# print(len(images_info))

values = [v for v in dict_data.values()]

print(values)


