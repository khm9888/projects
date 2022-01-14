
def card2symbols(file):
    dict_word = dict()
    with open(f"{file}","r") as f:
        lines = f.readlines()
        for i,line in enumerate(lines):
            word_list=line.strip().split(",")
            dict_word[i+1]=set(word_list)
            
            # cards.append(word_set)
    return dict_word


def common_symbols(num1,num2,c2s):
    return c2s[num1] &  c2s[num2]

def symbol2cards(c2s):
    dict_word = dict()
    for key,value in c2s.items():
        for word in value:
            if not word in dict_word:
                dict_word[word]={key}
            else:
                dict_word[word].add(key)
    return dict_word

def common_cards(word1,word2,s2c):
    return s2c[word1] & s2c[word2]
        

def missing_card(file):
    words=card2symbols('cards.txt').values()
    word_set=set()
    for word in words:
        print(word)
        for w in word:
            word_set.add(w)
            
    
    words=card2symbols(file).values()
    word_set_2=set()
    for word in words:
        for w in word:
            word_set_2.add(w)
    print(word_set)
    print(word_set_2)
    return word_set_2-word_set
    
def missing_card(file):
    check_value=0
    c2s=card2symbols(file)
    s2c=symbol2cards(c2s)
    s2c_len_dict = dict()
    for key,value in s2c.items():
        l=len(value)
        if not l in s2c_len_dict.keys():  
            s2c_len_dict[l]={key}
        else:
            s2c_len_dict[l].add(key)

    return s2c_len_dict[min(list(s2c_len_dict.keys()))]
        
        

c2s =card2symbols('cards.txt')
v= common_symbols(1, 2, c2s)
s2c = symbol2cards(c2s)


v=common_cards('snowman', 'ice cube', s2c)
# {1, 2, 3, 11}
# common_cards('ice cube', 'zebra', s2c)
# {2, 3, 5}
# common_cards('zebra', 'snowman', s2c)
# {2, 3, 4, 6, 8}

v = missing_card('missing.txt')
# {'baby bottle', 'carrot', 'clown', 'daisy flower'}



print(v)