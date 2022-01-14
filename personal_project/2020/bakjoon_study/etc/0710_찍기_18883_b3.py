'''
--url--
https://www.acmicpc.net/problem/18883

--title--
18883번: N M 찍기

--problem_description--
자연수 N, M이 주어졌을 때, 1부터 N×M까지 출력 형식대로 출력해보자.

--problem_input--
첫째 줄에 공백 한 칸으로 구분한 N, M이 주어진다. 두 수는 1,000보다 작거나 같은 자연수이다.

--problem_output--
총 N개의 줄을 출력해야 한다. 
각 줄에는 M개의 정수를 공백 한 칸으로 구분해 출력해야 한다. 
1번 줄에는 1부터 M까지, 2번 줄에는 M+1부터 2×M까지, ..., N번 줄에는 (N-1)×M+1부터 N×M까지 출력해야 한다.
None
'''

n, m =map(int,input().split())
for i in range(n):
    for j in range(1,m+1):
        if j!=m:
            print(j+m*i, end=" ")
        else:
            print(j+m*i)
    