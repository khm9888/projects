# >>> occurrences('lipo.txt')
# {'i': 21, 'm': 5, 't': 22, 'h': 8, 'n': 16, 'k': 3, 'g': 4, 'o': 12, 'f': 2, 'a': 19, 'r': 7, 'l': 6, 'q': 1, 'u': 9, 'y': 3, 'p': 1, 'c': 4, 's': 8, 'd': 6, 'w': 4, 'b': 2}

# >>> missing_letters('lipo.txt')
# {'e', 'j', 'v', 'x', 'z'}

# >>> make_lipogram('aeiou', 'lipo.txt')
# 'm thnkng f n rrtnl
# qntty mprtnt n clcls
# (t's hrd t dscss  ntrl
# lgrthms wtht t).
# Wht cnstnt m  thnkng f,
# nd why m  tlkng bt t
# n ths dd rndbt wy?

# >>> make_lipogram({'a', 'e', 'i', 'o', 'u'}, 'lipo.txt', 'copy.txt')




def occurrences(textfile):
    dict_word = dict()
    with open(f"{textfile}","r") as f:
        lines = f.readlines()
        for line in lines:
            # print(line)
            for word in line:
                if not word.isalpha():
                    continue
                # print(word)
                word = word.lower()
                # print(word)
                if word not in dict_word:
                    dict_word[word]=1
                else:
                    dict_word[word]+=1
    return dict_word                  
    
import string

def missing_letters(textfile):
    letters=set(occurrences(textfile).keys())
    alphaphet = set(string.ascii_lowercase)

    return alphaphet-letters          


# def make_lipogram(letters,textfile,copy="copy.txt"):
def make_lipogram(letters,textfile,copy=None):
    text = ""
    letters=list(letters)
    for i,l in enumerate(letters):
        letters[i] = letters[i].lower()
    with open(f"{textfile}","r") as f:
        lines = f.readlines()
        for line in lines:
            for word_0 in line:
                word = word_0.lower()
                if not word.isalpha():
                    text+=word
                    continue
                else:
                    if not word in letters:
                        text+=word_0
                    else:
                        continue
    if copy:  
        with open(f"{copy}","w") as f:
            f.write(text)
    else:
        print(text,end="")
    

# occurrences('G:\내 드라이브\공부\코드_학생 풀어준 자료\택용 2021\lipo.txt')


# print(missing_letters('G:\내 드라이브\공부\코드_학생 풀어준 자료\택용 2021\lipo.txt'))
# {'e', 'j', 'v', 'x', 'z'}

make_lipogram('WGVta', 'G:\내 드라이브\공부\코드_학생 풀어준 자료\택용 2021\lipo.txt')
    

# 'm thnkng f n rrtnl
# qntty mprtnt n clcls
# (t's hrd t dscss  ntrl
# lgrthms wtht t).
# Wht cnstnt m  thnkng f,
# nd why m  tlkng bt t
# n ths dd rndbt wy?
# >>> occurrences('lipo.txt')
# >>> make_lipogram({'a', 'e', 'i', 'o', 'u'}, 'lipo.txt', 'copy.txt')

