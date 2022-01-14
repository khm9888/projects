import pandas as pd

print("data")
data = pd.read_csv("/home/ubuntu/con/code/BiT/data/labels/data.csv")
print(data)

from collections import defaultdict

dict = defaultdict(int)

# print(data.keys())
for file_name in data["img_path"]:
    dict[file_name.split("_")[0]]+=1
    
# print(dict)

dict2=defaultdict(list)
for value,key in dict.items():
    # print(type(key[0]))
    # print(type(value))
    dict2[key].append(value)
    
sorted_keys=sorted(list(dict2.keys()))
print(f"len : {sorted_keys}")
print(sorted_keys)
for key in sorted_keys:
    print(f"{key}:{len(dict2[key])}")

x=int(input("could you select one key?"))
while x:
   print(dict2[x])
   x=int(input("could you select one key?"))