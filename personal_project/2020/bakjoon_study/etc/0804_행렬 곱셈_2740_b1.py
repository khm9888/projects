'''
--url--
https://www.acmicpc.net/problem/2740

--title--
2740번: 행렬 곱셈

--problem_description--
N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 행렬 A의 크기 N 과 M이 주어진다
둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 순서대로 주어진다
그 다음 줄에는 행렬 B의 크기 M과 K가 주어진다
이어서 M개의 줄에 행렬 B의 원소 K개가 차례대로 주어진다
N과 M, 그리고 K는 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

--problem_output--
첫째 줄부터 N개의 줄에 행렬 A와 B를 곱한 행렬을 출력한다
행렬의 각 원소는 공백으로 구분한다.

'''
first=[]
n,m = map(int,input().split())
for c_n in range(n):
    rows=list(map(int,input().split()))
    first.append(rows)

second=[]
m,k = map(int,input().split())
for c_m in range(m):
    rows=list(map(int,input().split()))
    second.append(rows)
    
mat=[]
for c_n in range(n):
    rows=[]
    for c_k in range(k):
        value=0
        for c_m in range(m):
            value+=first[c_n][c_m]*second[c_m][c_k]
        rows.append(value)
        # print(rows)
    mat.append(rows)

for i_k,c_k in enumerate(mat):
    for i_n,c_n in enumerate(c_k):
        if i_n!=len(c_k)-1:
            print(c_n,end=" ")
        else:
            print(c_n)
 
# print(mat)

