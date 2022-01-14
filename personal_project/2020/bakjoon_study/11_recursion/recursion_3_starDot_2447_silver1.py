'''
--url--
https://www.acmicpc.net/problem/2447

--title--
2447번: 별 찍기 - 10

--problem_description--
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

--problem_input--
None

--problem_output--
첫째 줄부터 N번째 줄까지 별을 출력한다.

'''
def stars(star):
    matrix=[]
    for i in range(3 * len(star)):#3*3
        if i // len(star) == 1:
            x=star[i % len(star)] + " " * len(star) + star[i % len(star)]
        else:
            x=star[i % len(star)] * 3
        print(x,1)
        matrix.append(x)
    return(list(matrix))

star = ["***","* *","***"]

n = int(input())#3,9,27...
k = 0#0승, 1승
while n != 3: #3이 될 때까지 나눈다.
    n = n // 3 # 3으로 나눈 값의 반복
    k += 1 #3으로 나눌 때마다 승수 올림

for i in range(k):#승수만큼 #k=1 이라고 가정하고 풀가 
    star = stars(star)#증가, 증가  #1번

for i in star:
    print(i)