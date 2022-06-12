'''
--url--
https://www.acmicpc.net/problem/11059

--title--
11059번: 크리 문자열

--problem_description--
숫자로만 이루어진 문자열 S가 주어진다
S의 연속된 부분 문자열 중에서 길이가 짝수이고, 앞의 절반의 합과 뒤의 절반의 합이 같은 부분 문자열을 크리 문자열이라고 한다
빈 문자열은 크리 문자열이 아니다.
S의 크리 문자열 중에서 가장 길이가 긴 것을 찾는 프로그램을 작성하시오.
예를 들어 S = "67896789" 인 경우에 정답은 "67896789"이 된다. 또, S = "6789789" 인 경우에 정답은 "789789"가 된다. S = "6789678" 인 경우에 정답은 "9678" 이다.

입력
첫째 줄에 문자열 S가 주어진다. S는 숫자로만 이루어져 있으며, 길이는 1,000을 넘지 않는다. 항상 크리 문자열이 존재하는 입력만 주어진다.

출력
첫째 줄에 S의 크리 문자열 중에서 가장 긴 것의 길이를 출력한다.
'''
from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, char):
    q = deque()
    q.append([i, j])
    chain.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6 and visit[nx][ny] == 0 and s[nx][ny] == char:
                visit[nx][ny] = 1
                q.append([nx, ny])
                chain.append([nx, ny])


def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if s[j][i] != "." and s[k][i] == ".":
                    s[k][i] = s[j][i]
                    s[j][i] = "."
                    break


s = [list(input().strip()) for i in range(12)]
result = 0
while True:
    isTrue = False
    visit = [[0] * 6 for i in range(12)]
    for i in range(12):
        for j in range(6):
            if s[i][j] != "." and visit[i][j] == 0:
                visit[i][j] = 1
                chain = []
                bfs(i, j, s[i][j])
                if len(chain) > 3:
                    isTrue = True
                    for x, y in chain:
                        s[x][y] = "."
    if not isTrue:
        break
    down()
    result += 1
print(result)
