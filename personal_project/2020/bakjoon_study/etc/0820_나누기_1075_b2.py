'''
--url--
https://www.acmicpc.net/problem/1075

--title--
1075번: 나누기

--problem_description--
두 정수 N과 F가 주어진다
지민이는 정수 N의 가장 뒤 두 자리를 적절히 바꿔서 N을 F로 나누어 떨어지게 만들려고 한다
만약 가능한 것이 여러 가지이면, 뒤 두 자리를 가능하면 작게 만들려고 한다.
예를 들어, N=275이고, F=5이면, 답은 00이다
200이 5로 나누어 떨어지기 때문이다. N=1021이고, F=11이면, 정답은 01인데, 1001이 11로 나누어 떨어지기 때문이다.

--problem_input--
첫째 줄에 N, 둘째 줄에 F가 주어진다
N은 100보다 크거나 같고, 2,000,000,000보다 작거나 같은 자연수이다
F는 100보다 작거나 같은 자연수이다.

--problem_output--
첫째 줄에 마지막 두 자리를 모두 출력한다
한자리이면 앞에 0을 추가해서 두 자리로 만들어야 한다.

'''



#코드1

n= input()
f= int(input())

n_new_front =int(n[:-2])*100
n_new = [n_new_front+n for n in range(100)]
for n in n_new:
    if n%f==0:
        break
answer = n-n_new_front
if answer//10==0:
    print(0,end="")
print(answer)

####################################

#코드2

import sys

input = sys.stdin.readline

n = int(input())#1000
f = int(input())#3

n -= n%100 #1000
answer = f-n%f #3-1000%3 =>2
if answer == f:
    answer=0
print(f"{answer:02d}")