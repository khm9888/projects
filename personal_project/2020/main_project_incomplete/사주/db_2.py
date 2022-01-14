from ast import literal_eval
import pandas as pd
import pymssql as ms
import pandas_profiling
from kss import split_sentences
# import konlp

def dbconn(tablename, insert_data):
    conn = ms.connect(server='192.168.0.176', user='bit2', password='1234',database='bitdb')
    # conn = ms.connect(server='127.0.0.1', user='bit2', password='1234',database='bitdb')
    cursor = conn.cursor()
    sql = f'INSERT INTO {tablename} values(%s ,%s ,%s ,%s, %s, %s)'
    # cursor.execute(sql, (insert_data[0], insert_data[1], insert_data[2], insert_data[3],insert_data[4],insert_data[5]))#list
    cursor.execute(sql, (insert_data["question_title"], insert_data["question_context"], insert_data["answer_writer"], insert_data["answer_context"],insert_data["url"],insert_data["index"]))#dic
    conn.commit()
    conn.close()

def create_table(tablename):
    conn = ms.connect(server='192.168.0.176', user='bit2', password='1234',database='bitdb')
    # conn = ms.connect(server='127.0.0.1', user='bit2', password='1234',database='bitdb')
    cursor = conn.cursor()
    sql = f"IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{tablename}' AND xtype='U')\
         CREATE TABLE {tablename} (question_title text null, question_context text null,\
             answer_writer text null, answer_context text null, url text null,idx text null)"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def drop_table(tablename):
    conn = ms.connect(server='192.168.0.176', user='bit2', password='1234',database='bitdb')
    # conn = ms.connect(server='127.0.0.1', user='bit2', password='1234',database='bitdb')
    cursor = conn.cursor()
    sql = f"DROP TABLE {tablename}"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def insert(tablename):
    for i in range(1,51):
        print(f"txt번호 : {i}")
        print()
        with open(f"D:\private\data\crawling_data\\a_{i}.txt",'r',encoding='utf-8') as file:
            lines = file.readlines()
            # print(type(lines))
            for j in range(len(lines)):
                print()
                print(f"라인번호:{j}")
                # try:
                dic=literal_eval(lines[j][:-2])
                # print(dic)
                sentences = dic["answer_context"]
                sentences=sentences.strip()
                sentences=split_sentences(sentences)
                # print(sentences)
                unused_words=["안녕하세요",dic["question_context"],dic["answer_writer"],"네이버 지식iN","blog"]
                # print(unused_words)
                dic["answer_context"]=""
                # print(sentences)
                for unused_word in unused_words:
                    for sentence in sentences:
                        if unused_word in sentence:
                            sentences.remove(sentence)
                cnt=0
                result=""

                for s in sentences:

                    if cnt<=200:
                        cnt+=len(s.strip().replace("?",""))
                        result+=(" "+s.strip())
                    # if result[0]=="?":
                    #     print("?")
                # sentences = " ".join(sentences)
 
                dic["answer_context"]=result
                # print('dic["answer_context"]')
                # print(dic["answer_context"])
                dbconn(tablename, dic)
                # except:
                #     print(dic["index"])

def select_data(tablename, col1, col2, col3, col4, col5, col6,how=5000):
    how=int(input("몇개 가져올래?"))
    conn = ms.connect(server='192.168.0.176', user='bit2', password='1234',database='bitdb')
    # conn = ms.connect(server='127.0.0.1', user='bit2', password='1234',database='bitdb')
    cursor = conn.cursor()
    sql = f'SELECT {col1}, {col2}, {col3}, {col4} , {col5} , {col6} FROM {tablename}'
    cursor.execute(sql)
    rows = list()
    row = cursor.fetchone()
    rows.append(row)
    cnt = 0
    while row :
        if cnt > how :
            break
        row = cursor.fetchone()
        rows.append(row)
        cnt += 1
    conn.close()

    # print(rows)
    # print(len(rows))

    return rows[:-1]


def replace_str(data):
    # data = data.replace('\n',' ')
    data = data.replace('//','')
    data = data.replace('ㅠ','')
    data = data.replace('ㅋ','')
    data = data.replace('?','')
    # data = data.replace('안녕하세요','')
    # data = data.replace('null','')

    return str(data)

def convert_dict(origin_data):
    
    data_dic = dict()
    col1_ls = list()
    col2_ls = list()
    cnt=0
    for data in origin_data:
        # print(data[0])
        t3 = data[4]
        if t3=="null" or t3=="":
            continue
        else:
            t3 = data[4]
            t3 = replace_str(t3)
            col2_ls.append(t3)  
    
        if data[1] != 'null':#제목이 공백인 경우
            t1 = replace_str(data[1])
            col1_ls.append(t1)
        else:
            cnt+=1
            print(data[2])
            # t2 = data[1]+' '+data[2]
            # t2 = replace_str(t2)
            # col1_ls.append(t2[:200])
            t1 = replace_str(data[2].strip())
            col1_ls.append(t1[:200])

    # print(f"cnt :{cnt}")
    data_dic['Q'] = col1_ls
    data_dic['A'] = col2_ls
    data_dic['label'] = [0 for i in range(len(col2_ls))]

    return data_dic

tablename = 'haemin_dream'

choice = input("create,drop,insert,select 중에 선택하세요 1/2/3/4 (기타는 select)\n")

if choice=="drop and create" or choice=="1"or choice=="c":
    # drop_table(tablename)
    create_table(tablename)
elif choice=="drop" or choice=="2"or choice=="d":
    drop_table(tablename)
elif choice=="insert" or choice=="3"or choice=="i":
    insert(tablename)
else:
    # col_ls = ["question_title", "question_context", "answer_writer", "answer_context","url","idx"]
   
    origin_data = select_data(tablename, "idx","question_title", "question_context", "answer_writer", "answer_context","url")
    converted_origin_data = convert_dict(origin_data)

    df = pd.DataFrame(converted_origin_data)
    df.to_csv('D:\private\KoGPT2-chatbot\Chatbot_data/ChatbotData_dream.csv',index=None)

# print(df.info())