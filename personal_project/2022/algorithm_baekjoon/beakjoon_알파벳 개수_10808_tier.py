'''
--url--
https://www.acmicpc.net/problem/10808

--title--
10808번: 알파벳 개수

--problem_description--
알파벳 소문자로만 이루어진 단어 S가 주어진다
각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 단어 S가 주어진다
단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

--problem_output--
단어에 포함되어 있는 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력한다.

'''
alphabet_count=[0 for _ in range(ord("z")-ord("a")+1)]
alphabets=[chr(a) for a in range(ord("a"),ord("z")+1)]
word = list(input())
for w in word:
    # print(w)
    alphabet_count[ord(w)-97]+=1
    
# print(alphabets)
# print(len(alphabets))
print(" ".join(map(str,alphabet_count)))