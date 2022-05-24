'''
--url--
https://www.acmicpc.net/problem/6359

--title--
6359번: 만취한 상범

--problem_description--
서강대학교 곤자가 기숙사의 지하에는 n개의 방이 일렬로 늘어선 감옥이 있다
각 방에는 벌점을 많이 받은 학생이 구금되어있다.
그러던 어느 날, 감옥 간수인 상범이는 지루한 나머지 정신나간 게임을 하기로 결정했다
게임의 첫 번째 라운드에서 상범이는 위스키를 한 잔 들이키고, 달려가며 감옥을 한 개씩 모두 연다
그 다음 라운드에서는 2, 4, 6, ..
번 방을 다시 잠그고, 세 번째 라운드에서는 3, 6, 9, ..
번 방이 열려있으면 잠그고, 잠겨있다면 연다
k번째 라운드에서는 번호가 k의 배수인 방이 열려 있으면 잠그고, 잠겨 있다면 연다
이렇게 n번째 라운드까지 진행한 이후, 상범이는 위스키의 마지막 병을 마시고 쓰러져 잠든다.
구금되어있는 몇 명(어쩌면 0명)의 학생들은 자신의 방을 잠그지 않은 채 상범이가 쓰러져버렸단 것을 깨닫고 즉시 도망친다.
방의 개수가 주어졌을 때, 몇 명의 학생들이 도주할 수 있는지 알아보자.

--problem_input--
입력의 첫 번째 줄에는 테스트 케이스의 개수 T가 주어진다
각 테스트 케이스는 한 줄에 한 개씩 방의 개수 n(5 ≤ n ≤ 100)이 주어진다.

--problem_output--
한 줄에 한 개씩 각 테스트 케이스의 답, 즉 몇 명이 탈출할 수 있는지를 출력한다.

'''

# 6359_만취한상범
# # import sys
# # n = int(sys.stdin.readline())
# # for _ in range(n):
# # m = int(sys.stdin.readline())
# # d = [0] * (n+1)
# # for i in range(1, n+1):
# # for j in range(i, n+1, i):
# # d[j] += 1 # cnt = 0
# # for i in range(1, n+1):
# # if d[i] % 2 == 1:
# # cnt +=1
# # print(cnt)
import sys
from math import floor
n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    print(floor(m ** 0.5))
