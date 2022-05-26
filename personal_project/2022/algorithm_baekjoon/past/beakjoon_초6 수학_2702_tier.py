'''
--url--
https://www.acmicpc.net/problem/2702

--title--
2702번: 초6 수학

--problem_description--


	두 정수 a와 b 최소공배수는 두 수의 공통된 배수 중 가장 작은 수이고, 최대공약수는 두 수의 공통된 약수중 가장 큰 수이다.


	a와 b가 주어졌을 때, 최소공배수와 최대공약수를 구하는 프로그램을 작성하시오.

--problem_input--


	첫째 줄에 테스트 케이스의 개수 T(1<=T<=1,000)가 주어진다
각 테스트 케이스는 두 정수 a와 b로 이루어져 있고, 공백으로 구분되어 있다
(1 <= a,b <= 1,000)

--problem_output--


	각 테스트 케이스에 대해 최소공배수와 최대공약수를 차례대로 출력한다.

'''

# 1850 최대공약수
import sys
input = sys.stdin.readline
T = int(input())


def gcd_for(a, b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def gcd_r(a, b):
    if b == 0:
        return a
    else:
        return gcd_r(b, a % b)


def lcm(a, b):
    return a*b//gcd_r(a, b)


for _ in range(T):
    a, b = map(int, input().split())
    print(lcm(a, b), gcd_r(a, b))
