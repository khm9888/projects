import json

with open("D:\private\project\main_project\ko_wiki.json", "r",encoding="utf-8") as read_file:
    data = json.load(read_file)
    print(len(data.keys()))
    # print(data.keys())
    # result=[]
    # for key,value in data.items():
    #     result.append(key)
    keys_list = [i for i in data.keys()]
    # print(keys_list)#['creator', 'version', 'data']
    keys_list=data['data']#list
    # print(len(keys_list))#68538
    # print(keys_list[1])
    keys_list=keys_list[1]#dic
    # print(keys_list.keys())#'paragraphs', 'title'
    # # print(keys_list['paragraphs'][0])#dict 
    keys_list=keys_list['paragraphs'][0]
    # print(keys_list)#dict_keys(['qas', 'context'])
    print(keys_list['context'])
    print(type(keys_list['context']))




    # print(keys_list)
    # json_sentence = data['sentence']#['text']
    # for sentence in json_sentence:
    #     s=sentence["text"]
    #     result+=s
    #     print(s)

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