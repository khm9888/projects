'''
--url--
https://www.acmicpc.net/problem/2294

--title--
2294번: 동전 2

--problem_description--
n가지 종류의 동전이 있다
이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다
그러면서 동전의 개수가 최소가 되도록 하려고 한다
각각의 동전은 몇 개라도 사용할 수 있다.
사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

--problem_input--
첫째 줄에 n, k가 주어진다
(1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다
가치가 같은 동전이 여러 번 주어질 수도 있다.

--problem_output--
첫째 줄에 사용한 동전의 최소 개수를 출력한다
불가능한 경우에는 -1을 출력한다.

'''

n, k = map(int, input().split())
c = []
dp = [0 for i in range(k + 1)]
for i in range(n):
    c.append(int(input()))
for i in range(1, k + 1):
    a = []
    for j in c:
        if j <= i and dp[i - j] != -1:
            a.append(dp[i - j])
    if not a:
        dp[i] = -1
    else:
        dp[i] = min(a) + 1
# print(dp)
print(dp[k])