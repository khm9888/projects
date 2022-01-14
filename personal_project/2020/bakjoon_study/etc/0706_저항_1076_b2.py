'''
--url--
https://www.acmicpc.net/problem/1076

--title--
1076번: 저항

--problem_description--
전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다.

처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다.

저항의 값은 다음 표를 이용해서 구한다.

예를 들어, 저항에 색이 yellow, violet, red였다면 저항의 값은 4,700이 된다.

--problem_input--
첫째 줄에 첫 번째 색, 둘째 줄에 두 번째 색, 셋째 줄에 세 번째 색이 주어진다. 색은 모두 위의 표에 쓰여 있는 색만 주어진다.

--problem_output--
입력으로 주어진 저항의 저항값을 계산하여 첫째 줄에 출력한다.

'''
# #version1

# vals = [input() for _ in range(3)]

# t=""

# for v in vals[:-1]:
#     if v == "black" :
#         t+="0"	
#     elif v == "brown" :
#         t+="1"	
#     elif v == "red" :
#         t+="2"	
#     elif v == "orange" :
#         t+="3"	
#     elif v == "yellow" :
#         t+="4"	
#     elif v == "green" :
#         t+="5"	
#     elif v == "blue" :
#         t+="6"	
#     elif v == "violet" :
#         t+="7"	
#     elif v == "grey" :
#         t+="8"	
#     elif v == "white" :
#         t+="9"


# sub=0
# w = vals[-1]
# if w == "black" :
#     sub = 1	
# elif w == "brown" :
#     sub = 10	
# elif w == "red" :
#     sub = 100	
# elif w == "orange" :
#     sub = 1000	
# elif w == "yellow" :
#     sub = 10000	
# elif w == "green" :
#     sub = 100000	
# elif w == "blue" :
#     sub = 1000000	
# elif w == "violet" :
#     sub = 10000000	
# elif w == "grey" :
#     sub = 100000000	
# elif w == "white" :
#     sub = 1000000000

# print(int(t)*sub)

#################################################

#version2
vals = [input() for _ in range(3)]
colors = ["black" ,"brown" ,"red" ,"orange" ,"yellow" ,"green" ,"blue" ,"violet" ,"grey" ,"white" ]


for i,v in enumerate(vals):
    if i==0:
        choose1=colors.index(v)
    elif i==1:
        choose2=colors.index(v)
    else:
        digit=10**colors.index(v)
print((choose1*10+choose2)*digit)


    