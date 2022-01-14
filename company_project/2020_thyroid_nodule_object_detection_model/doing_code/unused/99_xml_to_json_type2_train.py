import xml.etree.ElementTree as ET
import json
import cv2


base=dict()
# base["info"]=dict()
# base["licenses"]=list()
base["images"]=list()
base["annotations"]=list()
thyroid_dicts = dict()
dict_type = dict()

start_num=1
end_num=400

numbers = list(range(start_num,end_num+1))

rm_nums=list()#[54, 62, 120, 127, 142, 165, 166, 176, 197, 203, 205, 213, 230, 389]

# for n in rm_nums:
#     numbers.remove(n)

for n in numbers:#1
    try:
        print(f"n:{n}")
        dict_images=dict()

        path = f'data/thyroid/xml/{n}.xml'
        try:
            tree = ET.parse(path)
        except:
            continue
        root = tree.getroot()

        tirads=root.find("tirads").text

        mark=root.findall("mark")
        for m in mark:
            min_x=float("inf")
            min_y=float("inf")
            max_x=-float("inf")
            max_y=-float("inf")


            img_num=m.find("image").text
        
            svg=m.find("svg").text.replace('"','\"')#str
            svg=json.loads(svg)[0]['points']

            for v in svg:
                x,y=v["x"],v["y"]
                if min_x>x:
                    min_x=x
                if min_y>y:
                    min_y=y
                if max_x<x:
                    max_x=x
                if max_y<y:
                    max_y=y
                
            bbox = [min_x, min_y, max_x-min_x, max_y-min_y]
            id_str = f"{n}_{img_num}.jpg"
            id_num = -int(n)*10-int(img_num)

            image =cv2.imread(f"data/thyroid/data/{id_str}")
            height,width,_ = image.shape


            if tirads in ["2","3"]:
                tag=1
            elif tirads in ["4a","4b","4c","5"]:
                tag=2
            else:
                continue

            if tirads in dict_type:
                dict_type[tirads]+=1
            else:
                dict_type[tirads]=1

            dict_images["file_name"]=f"{id_str}"
            dict_images["height"]=height
            dict_images["width"]=width
            dict_images["id"]=id_num
            dict_images["user_id"]=0
            
            annotation_dict=dict()
            annotation_dict["area"]=bbox[2]*bbox[3]
            annotation_dict["iscrowd"]=0
            annotation_dict["image_id"]=id_num
            annotation_dict["bbox"]=bbox
            annotation_dict["tirads"]=tirads
            annotation_dict["category_id"]=tag
            annotation_dict["id"]=id_num


            base["images"].append(dict_images.copy())
            base["annotations"].append(annotation_dict)
    except:
        rm_nums.append(n)
        continue
print(rm_nums)
# print(len(base["annotations"]))

base["categories"]=list()

with open("data/thyroid/annotations/tirads_classification.txt","r") as file:
    lines=file.readlines()
    # print(len(lines))#9
    for line in lines:
        line=line.strip().split(":")
        tag=int(line[0].strip())

    #print(line)
        categories_dict=dict()
        categories_dict["id"]=tag
        categories_dict["name"]=line[1].strip()
        base["categories"].append(categories_dict)


with open("data/thyroid/annotations/from_xml.json","w") as json_file:
    json.dump(base,json_file)

# print("dict_type")
# print(dict_type)