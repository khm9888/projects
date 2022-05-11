'''
--url--
https://www.acmicpc.net/problem/2443

--title--
2443번: 별 찍기 - 6

--problem_description--
첫째 줄에는 별 2×N-1개, 둘째 줄에는 별 2×N-3개, ..., N번째 줄에는 별 1개를 찍는 문제
별은 가운데를 기준으로 대칭이어야 한다.

--problem_input--
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

--problem_output--
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

'''
n = int(input())
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
