'''
--url--
https://www.acmicpc.net/problem/5361

--title--
5361번: 전투 드로이드 가격

--problem_description--
상근이는 망가진 전투 드로이드를 고치려고 하고 있다
전투 드로이드의 각 부품의 가격은 다음과 같다.

--problem_input--
첫째 줄에 테스트 케이스의 개수가 주어진다
각 테스트 케이스는 음이 아닌 정수 다섯 개(A B C D E)로 이루어져 있다.

--problem_output--
각 테스트 케이스 마다, 입력으로 주어진 부품을 모두 구매하는데 필요한 비용을 소수점 둘째 자리까지 출력한다
달러 표시도 출력해야 한다
정답은 1억보다 작거나 같다.

'''
import sys

n=int(input())
values = [map(int,input().split()) for i in range(n)]
prices=[350.34,230.90,190.55,125.30,180.90]

for c in range(n):
    total=0
    for i,v in enumerate(values[c]):
        total+=prices[i]*v
    print(f"${total:.2f}")



