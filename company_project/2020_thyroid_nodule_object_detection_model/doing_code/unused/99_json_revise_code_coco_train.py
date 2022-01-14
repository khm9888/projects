import json


path = "/home/con/mmdetection/data/coco/annotations/"


with open(f"{path}instances_train2017.json","r") as file:
    data_coco= json.load(file)

# print(type(data_coco))
#<class 'dict'>

base_dict=dict()

for key,value in data_coco.items():
    # print(key)
    # info
    # licenses
    # images
    # annotations
    # categories
    # if key in ["images","annotations","categories"]
    # base_dict[key]=value
    candidate_keys=["images","annotations","categories"]
    value_list= []
    if key in candidate_keys: # 3개의 key만 선정
        print(key,len(value))
        # images 5000
        # annotations 36781
        # categories 80
        # print(key,"//",value[0].keys())
        print(f"----{key}----")
        for i ,under_key in enumerate(value[0].keys()):
            if i == len(value[0].keys())-1:
                print(under_key)
            else:
                print(under_key,end=",")
        # if key == "categories":
        #     for i,v in enumerate(value):
        #         print(i+1,v)
            # ----images----
            # license,file_name,coco_url,height,width,date_captured,flickr_url,id
            # ----annotations----
            # segmentation,area,iscrowd,image_id,bbox,category_id,id
            # ----categories----
            # supercategory,id,name
    if key in ["images"]: # images
        for v in value: #images 5000
            under_dict=dict()
            under_key_list=["file_name","height","width","id"]
            for under_key in under_key_list:
                under_dict[under_key]=v[under_key]
            value_list.append(under_dict)
        base_dict["images"]=value_list
    elif key in ["annotations"]: # images
        for v in value: #images 5000
            under_dict=dict()
            under_key_list=["area","iscrowd","image_id","bbox","category_id","id"]
            for under_key in under_key_list:
                under_dict[under_key]=v[under_key]
            value_list.append(under_dict)
        base_dict["annotations"]=value_list        
    elif key in ["categories"]: # images
        for v in value: #images 5000
            under_dict=dict()
            under_key_list=["id","name"]
            for under_key in under_key_list:
                under_dict[under_key]=v[under_key]
            value_list.append(under_dict)
        base_dict["categories"]=value_list


                        

with open(f"{path}instances_train2017_2.json","w") as file:
    json.dump(base_dict,file)

