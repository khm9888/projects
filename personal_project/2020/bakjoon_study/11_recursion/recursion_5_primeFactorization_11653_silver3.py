'''
--url--
https://www.acmicpc.net/problem/11653

--title--
11653번: 소인수분해

--problem_description--
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

--problem_output--
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다.

'''

import sys

input = sys.stdin.readline

x = int(input())
d = 2

primes = []

while d<=x:
    if x%d==0:
        print(d)
        primes.append(d)
        x = x//d
    else:
        d=d+1


# 재귀함수를 만들려고 했으나, 백준에선 계속 실패로 나온다.

# import sys
# input = sys.stdin.readline

# n = int(input())
# d= 2
# primes = []
# def primefact(n,d,primes):
#     if n>=d:# 100 , d=2
#         if n%d ==0:
#             print(d)
#             n=n//d
#         else:
#             d+=1
#         primefact(n,d,primes)
#         return 0
#     # elif n!=1:
#     #     print(n)    

# primefact(n,d,primes)
