import re
import random
def ngrams (word,count):
    word = re.sub('[^a-zA-Z]','-',word)
    
    words = word.split("-")    
    a_list = list()
    for word in words:
        target = word[-count:]
        start_word = word[:count]
        i=0
        idx=word.rfind(target)
        while i!=idx:
            # print(start_word)
            if len(start_word)==count and start_word not in a_list:
                a_list.append(start_word)
            i+=1
            start_word = word[i:count+i]
        if len(start_word)==count:
            a_list.append(start_word)
    return a_list

def dictionary(file,count):
    a_dict=dict()
    with open(file,"r") as f:
        lines = f.readlines()
        for line in lines:
            word = line.strip()
            
            for v in ngrams(word,count):
                # input()
                v=v.upper()
                if v in a_dict:
                    # print(v)
                    a_dict[v].add(word)
                else:
                    a_dict[v]={word}
                # input()
                # print("a_dict",a_dict)
                # print("a_dict.keys()",a_dict.keys())
                # print("a_dict.values()",a_dict.values())
    return a_dict
            
def ngram_count(a_dict,cnt=None):
    # print(not cnt)
    if not cnt:
        return len(a_dict.keys())

    result = 0 
    # print (a_dict.values())
    for v in a_dict.values():
        if len(v)==cnt:
            result+=1
    return result
    
def unique_ngram(a_dict):
    # print(a_dict.keys())
    a_list = [ ]
    for k,v in a_dict.items():
        if len(v)==1:
            a_list.append(k)
    k = random.choice(a_list)
    # print(a_dict[k])
    v = random.choice(list(a_dict[k]))
    return k,v
        # cnt=len(list(a_dict.keys())[0])
    # a_set=set()
    # for c,v in a_dict.items():
    #     for w in v:
    #         a_set.add(w)
    # print(a_set)    
    # y=list()
    # for w in a_set:
    #     print(w)
    
    #     y.extend(ngrams(w,cnt))
    #     # y=ngrams('Disgrace', 4)
    #     # print(y)
    # # return len(a_set)
    
    


v=ngrams('curliewurlie', 4)

# ['Disg', 'isgr', 'sgra', 'grac', 'race']
# v= ngrams('four-year-old', 3)
# # ['fou', 'our', 'yea', 'ear', 'old']
# v= ngrams('façade', 2)
# # ['fa', 'ad', 'de']
# v= ngrams('semi-self-sustaining', 4)
# ['semi', 'self', 'sust', 'usta', 'stai', 'tain', 'aini', 'inin', 'ning']

v = dictionary('dictionary.en.txt', 4)
v = dictionary('dictionary_01.txt', 3)
# v= english['SGRA']
# {'disgrading', 'disgrade', 'disgracers', 'misgrafts', 'palsgrave', 'hansgrave', 'disgracement', 'misgraded', 'misgrading', 'disgracer', 'disgraced', 'grosgrain', 'misgracious', 'disgracive', 'disgrace', 'predisgrace', 'palsgraf', 'disgracing', 'dysgraphia', 'misgrafting', 'disgraded', 'disgracefulness', 'misgraft', 'misgrave', 'misgraffed', 'misgrade', 'grosgrained', 'disgraceful', 'disgracia', 'disgracefully', 'disgracious', 'grosgrains', 'disgradation', 'disgraces', 'sgraffiti', 'crossgrainedness', 'misgraff', 'sgraffiato', 'undisgraced', 'disgradulate', 'misgrafted', 'sgraffito', 'palsgravine'}
# v= ngram_count(v)
# v= ngram_count(v,2)
# 63546
# v= ngram_count(english, 1)
# 13711
# v= ngram_count(english, 2)
# 7408
# v= ngram_count(english, 3)
# 4613
v= unique_ngram(v)
# ('RLBU', 'pearlbush')
# v= unique_ngram(english)
# ('FIFR', 'kefifrel')
# v= unique_ngram(english)
# ('PPAT', 'wappato')

# v= english = dictionary('dictionary.en.txt', 3)
# v= english['GNT']
# {'sovereignties', 'pgntt', 'supersovereignty', 'pgnttrp', 'sovereignty', 'cosovereignty', 'semisovereignty'}
# v= ngram_count(english)
# 9025
# v= ngram_count(english, 1)
# 1125
# v= ngram_count(english, 2)
# 561
# v= ngram_count(english, 3)
# 332
# v= unique_ngram(english)
# ('HMP', 'rhythmproof')
# v= unique_ngram(english)
# ('IPZ', 'leipzig')
# v= unique_ngram(english)
# ('LZH', 'alzheimer')

# v= dutch = dictionary('dictionary.nl.txt', 4)
# v= dutch['SGRA']
# {'visgraatje', 'bezettingsgraad', 'hardheidsgraad', 'asgrauwe', 'jongensgrappen', 'verzuringsgraad', 'doctorsgraden', 'alfabetiseringsgraad', 'werkgelegenheidsgraad', 'schansgravers', 'orpheusgrasmussen', 'visgraatmotief', 'moeilijkheidsgraad', 'werkloosheidsgraad', 'stadsgrachten', 'zeemansgraf', 'tewerkstellingsgraad', 'basisgrammatica', 'varkensgras', 'werkloosheidsgraden', 'werkingsgraad', 'leesgrage', 'scholingsgraad', 'ontwikkelingsgraad', 'vullingsgraad', 'glansgraad', 'Bosgra', 'koersgrafieken', 'vervuilingsgraad', 'activiteitsgraad', 'traangasgranaten', 'visgraatpatronen', 'gifgasgranaten', 'paltsgraven', 'visgraatdessins', 'kostendekkingsgraden', 'bewustzijnsgraad', 'visgraat', 'beladingsgraad', 'oorlogsgraf', 'zelfvoorzieningsgraad', 'oorlogsgraven', 'hellingsgraad', 'paltsgraaf', 'liesgras', 'koningsgraf', 'dekkingsgraden', 'moeilijkheidsgraden', 'visgraatdiagram', 'gasgranaten', 'vrijheidsgraad', 'beschavingsgraad', 'vrijheidsgraden', 'gasgranaat', 'doctorsgraad', 'asgrauw', 'besmettingsgraad', 'dekkingsgraad', 'luchtvochtigheidsgraad', 'beursgraadmeters', 'automatiseringsgraad', 'bezettingsgraden', 'leesgraag', 'Palsgraaf', 'koersgrafiek', 'stadsgracht', 'bedekkingsgraad', 'opleidingsgraad', 'olifantsgras', 'vochtigheidsgraad', 'beschermingsgraad', 'molenaarsgraaf', 'benuttingsgraad', 'zeemansgraven', 'hardheidsgraden', 'paltsgravin', 'bewolkingsgraad', 'struisgras', 'beursgraadmeter', 'koningsgraven', 'kostendekkingsgraad', 'visgraten', 'uitbuitingsgraad', 'paltsgraafschap', 'visgraatjes', 'jongensgrap', 'traangasgranaat', 'werkzaamheidsgraad', 'zuiverheidsgraad'}
# v= ngram_count(dutch)
# 57210
# v= ngram_count(dutch, 1)
# 8224
# v= ngram_count(dutch, 2)
# 7360
# v= ngram_count(dutch, 3)
# 3856
# v= unique_ngram(dutch)
# ('LAMR', 'glamrock')
# v= unique_ngram(dutch)
# ('ACGL', 'cognacglazen')
# v= unique_ngram(dutch)
# ('ALOL', 'afvalolie')

print(v)