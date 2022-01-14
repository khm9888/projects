'''
--url--
https://www.acmicpc.net/problem/10989

--title--
10989번: 수 정렬하기 3

--problem_description--
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

--problem_output--
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

# import sys

# v= [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]

# # print("*"*10)

# for i in sorted(v):
#     print(i)
    

import sys

counts = [0] * 10001

for i in range(int(input())):
    temp = int(sys.stdin.readline())
    counts[temp] += 1

# print("counts")
# print(counts)

for i in range(len(counts)):
    for j in range(counts[i]):
        print(i)