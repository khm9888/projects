'''
--url--
https://www.acmicpc.net/problem/4493

--title--
4493번: 가위 바위 보?

--problem_description--
가위 바위 보는 두 명이서 하는 게임이다
보통 미리 정해놓은 수 만큼 게임을 하고, 많은 게임을 이긴 사람이 최종 승자가 된다.
가위 바위 보를 한 횟수와 매번 두 명이 무엇을 냈는지가 주어졌을 때, 최종 승자를 출력하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에는 테스트 케이스의 개수 t(0 < t < 1000)가 주어진다
각 테스트 케이스의 첫째 줄에는 가위 바위 보를 한 횟수 n(0 < n < 100)이 주어진다
다음 n개의 줄에는 R, P, S가 공백으로 구분되어 주어진다
R, P, S는 순서대로 바위, 보, 가위이고 첫 번째 문자는 Player 1의 선택, 두 번째 문자는 Player 2의 선택이다.

--problem_output--
각 테스트 케이스에 대해서 승자를 출력한다
(Player 1 또는 Player 2) 만약, 비겼을 경우에는 TIE를 출력한다.

'''
n = int(input())


def trans_rps(x):
    if x == "R":
        return 1
    elif x == "P":
        return 2
    else:
        return 3


for _ in range(n):
    m = int(input())
    first = 0
    second = 0
    for _ in range(m):
        f, s = map(trans_rps, input().split())
        # f, s = trans_rps(f), trans_rps(s)
        if f == s:
            pass
        elif (f == 2 and s == 1) or (f == 3 and s == 2) or (f == 1 and s == 3):
            first += 1
        else:
            second += 1
    if first == second:
        print("TIE")
    elif first > second:
        print("Player 1")
    else:
        print("Player 2")
