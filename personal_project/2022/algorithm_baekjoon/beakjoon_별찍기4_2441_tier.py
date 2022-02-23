'''
--url--
https://www.acmicpc.net/problem/2445

--title--
2441번: 별 찍기 - 8

문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
'''
x = int(input())
for i in range(1,x+1):
    print("*"*(i)+" "*(x-i)*2+"*"*(i))
for i in range(x-1,0,-1):
    print("*"*(i)+" "*(x-i)*2+"*"*(i))