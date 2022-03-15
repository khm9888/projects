'''
--url--
https://www.acmicpc.net/problem/2407

--title--
2407번: 조합

--problem_description--

입력
n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)

출력
nCm을 출력한다.

'''

n, m = tuple(map(int, input().split()))

calc = 1
devide_one = 1

count_calc = min(n - m, m)

for i in range(1, count_calc + 1):
    calc *= (n - i + 1)
    devide_one *= i
    # print(calc)
    # print(devide_one)
calc //= devide_one
print(calc)
