'''
--url--
https://www.acmicpc.net/problem/9237

--title--
9237번: 이장님 초대

--problem_description--
농부 상근이는 마당에 심기 위한 나무 묘목 n개를 구입했다
묘목 하나를 심는데 걸리는 시간은 1일이고, 상근이는 각 묘목이 다 자라는데 며칠이 걸리는지 정확하게 알고 있다.
상근이는 마을 이장님을 초대해 자신이 심은 나무를 자랑하려고 한다
이장님을 실망시키면 안되기 때문에, 모든 나무가 완전히 자란 이후에 이장님을 초대하려고 한다
즉, 마지막 나무가 다 자란 다음날 이장님을 초대할 것이다.
상근이는 나무를 심는 순서를 신중하게 골라 이장님을 최대한 빨리 초대하려고 한다
이장님을 며칠에 초대할 수 있을까?

--problem_input--



'''

import sys

input = sys.stdin.readline
N = int(input())  # 묘목의 수
tree = list(map(int, input().split()))
tree.sort(reverse=True)
for i in range(len(tree)):
    tree[i] = tree[i] + i + 1  # 심는 일 수와 묘목이 자라는 일 수를 더한다.
print(max(tree) + 1)  # 이장님은 그 다음날 온다
