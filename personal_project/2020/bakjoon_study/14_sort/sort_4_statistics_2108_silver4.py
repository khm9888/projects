'''
--url--
https://www.acmicpc.net/problem/2108

--title--
2108번: 통계학

--problem_description--
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

--problem_output--
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.
'''


import sys
from collections import Counter
input =sys.stdin.readline

n=int(input())#몇개
v=[int(input()) for i in range(n)]#값들 다 저장


if n >1:
    def average(v):#평균
        return round(sum(v)/len(v))
    def median(v):#중앙값
        v.sort()
        return v[len(v)//2]
    v.sort()
    c = Counter(v).most_common(2)

    if  c[0][1] == c[1][1]:
        offen = c[1][0]
    else:
        offen = c[0][0]


    avg = average(v)
    mid = median(v)
    offen = offen
    

else:
    
    avg = v[0]
    mid = v[0]
    offen = v[0]
coverage = max(v)-min(v)
# print("-"*10)
print(avg)
print(mid)
print(offen)
print(coverage)