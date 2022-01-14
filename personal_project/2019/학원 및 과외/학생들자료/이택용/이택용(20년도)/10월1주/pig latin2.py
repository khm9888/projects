

# print(ord("A"))
# print(ord("Z"))
# print(ord("a"))
# print(ord("z"))

#A 65
#Z 90
#a 97
#z 122

# text = input()
def pigword(word):
    answer=""
    ends= ["!","?",","]
    vowels_0=["a","e","i","o","u"]
    vowels=vowels_0.copy()
    [vowels.append(v.upper()) for v in vowels_0]

    # print(f"text:{text}")
    # print(i,word)
    end=""
    # print(f"word:{word}")
    # print(len(word))
    word_0=list(word)
    word_0="".join(word_0)
    i=-1
    if not (65<=ord(word[i])<=90 or 97<=ord(word[i])<=122): #특수기호처리
        # print("c")
        end+=word_0[i:]
        word=word_0[:i]   
    else:
        leng_word=len(word)
    # print(word)
    # print(f"end:{end}")
    check=False     
    check2=False     
        
    if word[0] in vowels:#처음이 모음이라면.
        check=True
    elif 65<=ord(word[0])<=90:# 처음이 자음 중에서 대문자라면
        check2=True

    for i,w in enumerate(word):
        if (word[i].lower()=="u" and word[i-1].lower()=="q"):#직전 글자가 qu처럼 되어있다면.
            pass
            # print("case1")
        elif word[i] in vowels:#모음이라면
            if 65<=ord(word[i])<=90:
                pass              
            elif check2:
                word=list(word)
                word[i]=word[i].upper()
                # print("word[i]")
                # print(word[i])
                word[0]=word[0].lower()
                # print("word[0]")
                # print(word[0])
                word="".join(word)
                check2=False
            word=word[i:]+word[:i]
            break              
        else:   
            # print("case3")
            pass
    if check:
        word+="way"
    else:
        word=word+"ay"
    if len(end)!=0:
        word+=end
    answer+=word+" "
    answer = answer.rstrip()
    return answer


def piglatin(words):
    answer=""
    words = words.split()
    for i,word in enumerate(words):
        if word.find("'")!=-1:
            w = word.split("'")
            # print(w)
            for i,a in enumerate(w):
                if i!=len(w)-1:
                    answer+=pigword(a)+"'"
                    # print(answer)
                else:
                    answer+=pigword(a)+" "
                    # print(answer)
                    
                    
        elif word.find("-")!=-1:
            w = word.split("-")
            # print(w)
            for i,a in enumerate(w):
                if i!=len(w)-1:
                    answer+=pigword(a)+"-"
                    # print(answer)
                else:
                    answer+=pigword(a)+" "
                    # print(answer)
                    
        # elif word.find("..")!=-1:
        #     w = word.split("..")
        #     # print(w)
        #     for i,a in enumerate(w):
        #         if i!=len(w)-1:
        #             answer+=pigword(a)+".."
        #             print(answer)
        #         else:
        #             answer+=pigword(a)+" "
        #             print(answer)
        else:
            answer+=pigword(word)+" "
    answer = answer.rstrip()
    return answer
# print(ord(" "))
# print(piglatin("And this'll help things turn out for the best..."))
# 'Andway ownay orfay omethingsay ompletelycay ifferentday!'
# print(pigword("different!"))
# "Onay, Iway'may onlyway ullingpay ouryay eglay, itway'say ucifixioncray eallyray!"
#  Onay, Iway'I'mway onlyway ullingpay ouryay eglay, itway'it'sway ucifixioncray eallyray!
# "Onay, Iway'may onlyway ullingpay ouryay eglay, itway'say ucifixioncray eallyray!"