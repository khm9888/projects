'''
--url--
https://www.acmicpc.net/problem/5618

--title--
5618번: 공약수

--problem_description--
자연수 n개가 주어진다
이 자연수의 공약수를 모두 구하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 n이 주어진다. n은 2 또는 3이다. 둘째 줄에는 공약수를 구해야 하는 자연수 n개가 주어진다. 모든 자연수는 108 이하이다.

출력
입력으로 주어진 n개 수의 공약수를 한 줄에 하나씩 증가하는 순서대로 출력한다.
'''
n = int(input())
v_list = list(map(int, input().split()))
v_list.sort()
result = [1]
for i in range(2, v_list[0]+1):
    cnt = 0
    for v in v_list:
        if v % i == 0:
            cnt += 1
        else:
            break
        if cnt == n:
            result.append(i)
for r in result:
    print(r)
