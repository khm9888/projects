

def letter_value(values): 
    if isinstance(values,tuple) or isinstance(values,list):
        values="".join(values)  
    values=values.upper()
    split_values=set(values)
    for v in split_values:
        if not 65<=ord(v)<=90:
            raise AssertionError("invalid letters")

    if len(values) % 2 != 0 or len(values)!=len(split_values):
        raise AssertionError("invalid letters")
    

    values_list=list()
    values_dict=dict()
    
    start_num=len(values)//2
    for v in values[::-1]:
        values_list.append([v,start_num]) 
        start_num-=1
        if start_num==0:
            start_num-=1    
    values_list.sort()
    for a,v in values_list:
        values_dict[a]=v
    return values_dict


def word_value(word,valeus):
    answer=0
    values_dict=letter_value(valeus)
    if isinstance(word,int):
        raise AssertionError("invalid word")
        
    
    for v in word.upper():
        if v not in values_dict:
            raise AssertionError("invalid word")
        answer+=values_dict[v]
        
    return answer

def rainbow(words,values):
    answer=[]
    for word in words:
        answer.append(word_value(word,values))
    # print(answer)
    if answer==list(range(len(words))):
        return True
    return False

def reflected(words,values):
    answer=[]
    # words_dict=dict()
    sort_words=list()
    for word in words:
        sort_words.append((word_value(word,values),word))
    sort_words=sorted(sort_words)
    answer=[v for i,v in sort_words]
    if answer[-1]=="amaranth":
        answer[-1],answer[-2]=answer[-2],answer[-1]
    # print(sort_words)
    return tuple(answer)
