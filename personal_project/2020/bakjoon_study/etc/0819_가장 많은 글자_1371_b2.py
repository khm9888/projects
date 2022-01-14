'''
--url--
https://www.acmicpc.net/problem/1371

--title--
1371번: 가장 많은 글자

--problem_description--
영어에서는 어떤 글자가 다른 글자보다 많이 쓰인다
예를 들어, 긴 글에서 약 12.31% 글자는 e이다.
어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.

--problem_input--
첫째 줄부터 글의 문장이 주어진다
글은 최대 5000글자로 구성되어 있고, 공백, 알파벳 소문자, 엔터로만 이루어져 있다
그리고 적어도 하나의 알파벳이 있다.

--problem_output--
첫째 줄에 가장 많이 나온 문자를 출력한다
여러 개일 경우에는 알파벳 순으로 앞서는 것부터 모두 공백없이 출력한다.

'''

dict_words  = dict()
sentences =""

while True:
    try:
        sentences+= input().replace(" ","")
    except:
        break
for s in sentences:
    if s in dict_words:
        dict_words[s]+=1
    else:
        dict_words[s]=1

max_value=max(list(dict_words.values())) 

answer=[]
for k,v in dict_words.items():
    if v==max_value:
        answer.append(k)

answer.sort()
print("".join(answer))
