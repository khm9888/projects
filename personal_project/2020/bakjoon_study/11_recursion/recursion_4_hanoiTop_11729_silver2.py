'''
--url--
https://www.acmicpc.net/problem/11729

--title--
11729번: 하노이 탑 이동 순서

--problem_description--
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

아래 그림은 원판이 5개인 경우의 예시이다.

None

--problem_input--
첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

 

--problem_output--
첫째 줄에 옮긴 횟수 K를 출력한다.

두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

'''

#1개가 있으면 3번으로 옮긴다.
#2개가 있으면 1을 2번으로 옮기고, 2를 3으로 옮기고, 1을 다시 3으로 옮긴다.
#3기가 있으면 위를 실행하고,3을 옮긴다.

def hanoi(n,one,two,three):
    if n==1:
        cnt.append((one,three))
    else:
        hanoi(n-1,one,three,two)
        cnt.append((one,three))
        hanoi(n-1,two,one,three)
    return cnt

n = int(input())
cnt=[]
top = hanoi(n,1,2,3)
print(len(top))

[print(i,j) for i,j in top]