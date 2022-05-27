'''
--url--
https://www.acmicpc.net/problem/16466

--title--
16466번: 콘서트

--problem_description--
HCPC (Hanyang Completely Perfect Celebrity)는 한양대학교 최고의 가수에게 주어지는 칭호이다
한양대학교는 매년 최고의 HCPC를 선발한다
HCPC가 되기란 여간 어려운 게 아니다
매일 아침 날달걀을 까먹고, 여름에도 목도리를 하여 목을 보호하고 평소에 한 마디도 하지 않으며 HCPC가 되기 위해 목을 보호한다
실제로 귀가 어둡고 잘 들리지 않던 사람도 HCPC의 노래 한 소절만 들으면 귀가 밝아지고 청명해지며 똑똑해지고 삶의 이치를 깨닫게 된다고 한다.
이런 HCPC의 목소리를 한양대생들에게 들려줄 기회를 마련하기 위해 한양대에선 매년 HCPC의 콘서트를 연다
HCPC 콘서트의 티켓팅은 매우 치열하며 티켓팅은 2차까지 있다
이 티켓의 번호가 작을수록 HCPC의 목소리를 가까이에서 들을 수 있다. 
양한이는 HCPC 콘서트의 1차 티켓팅을 놓치고, 2차 티켓팅에 도전한다
양한이는 매우 특별한 정보를 얻었는데, 이는 바로 1차 티켓팅에서 이미 팔린 티켓의 번호들의 목록이다
티켓의 번호는 1번부터 시작한다. 
양한이는 이 목록에 있는 번호들을 가진 티켓을 제외한 티켓 중 번호가 가장 작은 티켓의 번호를 알고 싶다
양한이를 도와주자!

--problem_input--
첫째 줄에 1차 티켓팅에서 팔린 티켓들의 수인 정수 N이 주어진다
(1 ≤ N ≤ 1,000,000)
둘째 줄에는 1차 티켓팅에서 팔린 티켓들의 번호 정수 Ai가 주어진다. (1 ≤ Ai ≤ 231 − 1)

출력
2차 티켓팅에서 양한이가 가질 수 있는 티켓 중 가장 작은 번호를 출력한다.
'''

import sys
import bisect

N = int(sys.stdin.readline())
tickets = list(map(int, sys.stdin.readline().split()))
tickets.sort()
max_tickets = tickets[-1]

for i in range(1, max_tickets + 1):
    index = bisect.bisect_left(tickets, i)

    if index < len(tickets) and tickets[index] != i:
        print(i)
        break

    if index == len(tickets) - 1:
        print(max_tickets + 1)
