import json
from sklearn.model_selection import train_test_split
# import sklearn
json1 = "from_xml.json"
json2 = "from_db.json"
json3 = "concat.json"
json4 = "train.json"
json5 = "val.json"
json6 = "test.json"

path = "/home/con/mmdetection/data/thyroid/annotations/"
with open(path+json1,"r") as file1, open(path+json2,"r") as file2 :
    data_xml= json.load(file1)
    data_db= json.load(file2)


data_xml["images"].extend(data_db["images"])
# data_xml["images"]=data_xml["images"]+data_db["images"]
data_xml["annotations"].extend(data_db["annotations"])

with open(path+json3,"w") as file_w:
    json.dump(data_xml,file_w)
        
copy_data1 = data_xml.copy()
copy_data2 = data_xml.copy()
copy_data3 = data_xml.copy()

c1,c2 = train_test_split(data_xml["images"],train_size=0.8,random_state=1)
c2_1,c2_2 = train_test_split(c2,train_size=0.6,random_state=1)

copy_data1["images"]=c1
copy_data2["images"]=c2_1
copy_data3["images"]=c2_2


print(f'total_size :{len(data_xml["images"])}')
print(f"train_size :{len(c1)}")
print(f"val_size :{len(c2_1)}")
print(f"test_size :{len(c2_2)}")

with open(path+json4,"w") as file_w:
    json.dump(copy_data1,file_w)
    

with open(path+json5,"w") as file_w:
    json.dump(copy_data2,file_w)


with open(path+json6,"w") as file_w:
    json.dump(copy_data3,file_w)

