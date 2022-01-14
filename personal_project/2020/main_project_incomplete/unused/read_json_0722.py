import json

with open("D:\private\project\main_project\kenya.json", "r",encoding="utf-8") as read_file:
    data = json.load(read_file)
    # for key,value in data.items():
    #     print(key,value)
    result=[]
    json_sentence = data['sentence']#['text']
    for sentence in json_sentence:
        s=sentence["text"]
        result+=s
        print(s)

# import json5
# result=[]
# with open('D://Project//data//edited_[A1] 0002431_케냐(본문).json','r',encoding='utf-8') as json_file:
#     json_data = json5.load(json_file)
#     # print(json_data)
#     json_sentence = json_data['sentence']#['text']
#     for sentence in json_sentence:
#         result+=sentence["text"]
# with open("D://Project//data//"+'케냐'+".txt",'w',encoding='utf-8') as f:
#     f.write(result)