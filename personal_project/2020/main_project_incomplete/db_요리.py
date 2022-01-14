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
    sql = f'INSERT INTO {tablename} values(%s ,%s ,%s ,%s, %s, %s, %s, %s, %s)'
    # cursor.execute(sql, (insert_data[0], insert_data[1], insert_data[2], insert_data[3],insert_data[4],insert_data[5]))#list
    cursor.execute(sql, (insert_data["idx"],insert_data["question"],insert_data["answer"],insert_data["url"],insert_data["question_title"], insert_data["question_context"], insert_data["answer_writer"], insert_data["answer_context"],insert_data["keyword"]))#dic
    conn.commit()
    conn.close()

def create_table(tablename):
    conn = ms.connect(server='192.168.0.176', user='bit2', password='1234',database='bitdb')
    # conn = ms.connect(server='127.0.0.1', user='bit2', password='1234',database='bitdb')
    cursor = conn.cursor()
    sql = f"IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{tablename}' AND xtype='U')\
         CREATE TABLE {tablename} (idx text null, question text null, answer text null,  url text null, question_title text null, question_context text null,\
             answer_writer text null, answer_context text null, keyword text null)"
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

def delete_table(tablename):
    conn = ms.connect(server='192.168.0.176', user='bit2', password='1234',database='bitdb')
    # conn = ms.connect(server='127.0.0.1', user='bit2', password='1234',database='bitdb')
    cursor = conn.cursor()
    sql = f"DELETE From {tablename}"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def insert(tablename):
    # names = ["요리 레시피","음식 레시피","집에서 간단한 요리","요리하는법"]
    names = ["요리하는법"]
    for name in names:
        try:
            for i in range(1,16):
                print(f"txt번호 : {i}")
                print()
                with open(f"D:\private\data\crawling_data\{name}\{name}_{i}.txt",'r',encoding='utf-8') as file:
                    lines = file.readlines()
                    # print(type(lines))
                    for j in range(len(lines)):
                        print()
                        # print(f"라인번호:{j}")

                        dic=literal_eval(lines[j][:-2])
                        #질문처리
                        sentences_0 = dic["question_title"].replace("-","")#제목
                        sentences_0=sentences_0.strip()
                        sentences_0=split_sentences(sentences_0)
                        sentences_1 = dic["question_context"]#질문내용
                        sentences_1=sentences_1.strip()
                        # print(sentences_0)
                        sentences_1=split_sentences(sentences_1)

                        unused_words=["안녕하세요","네이버 지식iN","blog", "내공","null"]
                        # print(unused_words)
                        # print(sentences)
                        for unused_word in unused_words:
                            for sentence in sentences_0:
                                if unused_word in sentence:
                                    sentences_0.remove(sentence)
                        for unused_word in unused_words:
                            for sentence in sentences_1:
                                if unused_word in sentence:
                                    sentences_1.remove(sentence)
                        result=""
                        cnt=0
                        for s in sentences_0:
                            s=s.strip()
                            if cnt+len(s)<100:
                                cnt+=len(s)
                                result+=(" "+s.strip())
                            else:
                                break

                        for s in sentences_1:
                            s=s.strip().replace("?","")
                            if cnt+len(s)<100:
                                cnt+=len(s)
                                result+=(" "+s.strip())
                            else:
                                break
                        dic["question"]=result

                        #답변 처리
                        sentences = dic["answer_context"]
                        sentences=sentences.strip()
                        sentences=split_sentences(sentences)
                        unused_words=["안녕하세요",dic["question_context"],dic["answer_writer"],"네이버 지식iN","blog"]
                        for unused_word in unused_words:
                            for sentence in sentences:
                                if unused_word in sentence:
                                    sentences.remove(sentence)
                        # print(sentences)
                        cnt=0
                        result=""

                        for s in sentences:
                            s=s.strip().replace("?","")
                            if cnt+len(s)<200:
                                cnt+=len(s)
                                result+=(" "+s.strip())
                            else:
                                break
                    
                        dic["answer"]=result
                        dic["keyword"]=name

                        if len(dic["question"])>10 and len(dic["answer"])>20:
                            dbconn(tablename, dic)
                        # except:
                    #     print(dic["index"])
        except:
            continue

def select_data(tablename, col1, col2,how=5000):
    how=int(input("몇개 가져올래?"))
    conn = ms.connect(server='192.168.0.176', user='bit2', password='1234',database='bitdb')
    # conn = ms.connect(server='127.0.0.1', user='bit2', password='1234',database='bitdb')
    cursor = conn.cursor()
    sql = f'SELECT {col1}, {col2} FROM {tablename}'
    #              
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
    #"question", "answer"
    for data in origin_data:
        # print(data[0])
        t3 = data[1]#answer
        if t3=="null" or t3=="":
            continue
        else:
            t3 = replace_str(t3)
            col2_ls.append(t3)  
    
        if data[0] != 'null':#제목이 공백인 경우
            t1 = replace_str(data[0])
            col1_ls.append(t1)
        else:
            cnt+=1
            print(data[2])
            # t2 = data[1]+' '+data[2]
            # t2 = replace_str(t2)
            # col1_ls.append(t2[:200])
            t1 = replace_str(data[2].strip())
            col1_ls.append(t1)

    # print(f"cnt :{cnt}")
    data_dic['Q'] = col1_ls
    data_dic['A'] = col2_ls
    data_dic['label'] = [0 for i in range(len(col2_ls))]

    return data_dic

tablename = 'haemin_used'

choice = input("create,drop,insert,delete,select 중에 선택하세요 1/2/3/4/5 (기타는 select)\n")

if choice=="drop and create" or choice=="1"or choice=="c":
    # drop_table(tablename)
    create_table(tablename)
elif choice=="drop" or choice=="2":
    drop_table(tablename)
elif choice=="insert" or choice=="3"or choice=="i":
    insert(tablename)
elif choice=="delete" or choice=="4":
    delete_table(tablename)
elif choice=="select" or choice=="5":
    # col_ls = ["question_title", "question_context", "answer_writer", "answer_context","url","idx"]
   
    origin_data = select_data(tablename,"question", "answer")
    converted_origin_data = convert_dict(origin_data)

    df = pd.DataFrame(converted_origin_data)
    df.to_csv('D:\private\KoGPT2-chatbot\Chatbot_data/ChatbotData_recipe.csv',index=None)

    print(df.info())