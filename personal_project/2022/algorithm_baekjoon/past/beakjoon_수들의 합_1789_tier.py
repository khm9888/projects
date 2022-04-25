'''
--url--
https://www.acmicpc.net/problem/1789

--title--
1789번: 수들의 합

--problem_description--
서로 다른 N개의 자연수의 합이 S라고 한다
S를 알 때, 자연수 N의 최댓값은 얼마일까?

--problem_input--
첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

--problem_output--
첫째 줄에 자연수 N의 최댓값을 출력한다.

'''

N = int(input())

temp = 1
answer = 0

while True:
    N -= temp

    if N >= 0:
        answer += 1
        temp += 1

    else:
        print(answer)
        break