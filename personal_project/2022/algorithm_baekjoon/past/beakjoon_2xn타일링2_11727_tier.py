'''
--url--
https://www.acmicpc.net/problem/11727

--title--
11727번: 2×n 타일링 2

--problem_description--
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
아래 그림은 2×17 직사각형을 채운 한가지 예이다.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
'''
n = int(input())
values = [0, 1, 3]
for i in range(3, n+1):
  values.append((values[i - 2] * 2) + values[i - 1])
print(values[n] % 10007)