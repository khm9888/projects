'''
--url--
https://www.acmicpc.net/problem/10872

--title--
10872번: 팩토리얼

--problem_description--
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

--problem_output--
첫째 줄에 N!을 출력한다.

'''

n = int(input())

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return factorial(n-1)*n

print(factorial(n))