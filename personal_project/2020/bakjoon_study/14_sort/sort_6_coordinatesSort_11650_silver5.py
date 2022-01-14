'''
--url--
https://www.acmicpc.net/problem/11650

--title--
11650번: 좌표 정렬하기

--problem_description--
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

--problem_input--
None

--problem_output--
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

'''

import sys

input = sys.stdin.readline
n = int(input())
v = [ list(map(int,input().split())) for w in range(n)]
print(type(v[0]))
v.sort()

[print(i[0],i[1]) for i in v]


