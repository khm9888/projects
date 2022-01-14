
def outside(word):
    return word[0] + word[-1]

def inside(word):
    return word[1:-1]


def issubword(word, words):
    chk = True
    i=0
    for w in word:
        if w in word:
            index=words[i:].find(w)+i
            i=max(i,index)
        if w not in words[i:]:
            chk=False
            break
    return chk

''' def issubword(word, words):
    woord = list(word)
    for i in range(len(woord)-1):
        if word[i] == word[i+1]:
            woord[i] = ''
    woord = ''.join(woord)
    woord = list(woord)
    for i in words:
        if i == woord[0]:
            del woord[0]
        if len(woord) == 0:
            return True
    return False
 '''

def iswandering(word, words):
    if issubword(word, words) == True and word[0] == words[0] and word[-1] == words[-1]:
        return True
    else:
        return False
    
def read_dictionary(file):
    dict_word = dict()
    with open(f"{file}","r") as f:
        lines = f.readlines()
        for word in lines:
            word = word.strip()
            # print(word)
            # print(outside(word))
            if not outside(word) in dict_word:
                dict_word[outside(word)]={inside(word)}
            else:
                dict_word[outside(word)].add(inside(word))
    return dict_word
                

def wanderings(word,dictionary):
    dict_word = dictionary
    set_word = set()
    # for key in dict_word.keys():
    key = outside(word)
    if key in dict_word:
        for word_0 in dict_word[key]:
            new_word=key[0]+word_0+key[-1]
            if iswandering(new_word,word):
                set_word.add(new_word)
    return set_word         
       
dictionary = read_dictionary('dictionary.txt')
v= wanderings('qwertyuihgfcvbnhjk', dictionary)
# {'quick'}
# v= wanderings('qwertyuytresdftyuiokn', dictionary)
# {'queen', 'question'}
v= wanderings('ghijakjthoijerjidsdfnokg', dictionary)
# {'gating', 'geeing', 'goring', 'going', 'gathering'}
# v= wanderings('xkzjunspebfgslddfksdrx', dictionary)
set()

print(v)


