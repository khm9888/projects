'''
--url--
https://www.acmicpc.net/problem/2460

--title--
2460번: 지능형 기차 2

--problem_description--
최근에 개발된 지능형 기차가 1번역(출발역)부터 10번역(종착역)까지 10개의 정차역이 있는 노선에서 운행되고 있다
이 기차에는 타거나 내리는 사람 수를 자동으로 인식할 수 있는 장치가 있다
이 장치를 이용하여 출발역에서 종착역까지 가는 도중 기차 안에 사람이 가장 많을 때의 사람 수를 계산하려고 한다
단, 이 기차를 이용하는 사람들은 질서 의식이 투철하여, 역에서 기차에 탈 때, 내릴 사람이 모두 내린 후에 기차에 탄다고 가정한다.
예를 들어, 위와 같은 경우를 살펴보자
이 경우, 기차 안에 사람이 가장 많은 때는 2번역에서 3명의 사람이 기차에서 내리고, 13명의 사람이 기차에 탔을 때로, 총 42명의 사람이 기차 안에 있다.
이 기차는 다음 조건을 만족하면서 운행된다고 가정한다.
10개의 역에 대해 기차에서 내린 사람 수와 탄 사람 수가 주어졌을 때, 기차에 사람이 가장 많을 때의 사람 수를 계산하는 프로그램을 작성하시오.

--problem_input--
각 역에서 내린 사람 수와 탄 사람 수가 빈칸을 사이에 두고 첫째 줄부터 열 번째 줄까지 역 순서대로 한 줄에 하나씩 주어진다. 

--problem_output--
첫째 줄에 최대 사람 수를 출력한다
 

'''


count_max_peoples=0
now_people=0
p_list=list()
for _ in range(10):
    out_p,in_p = tuple(map(int,input().split()))
    now_people = in_p-out_p+now_people
    p_list.append((_,now_people))
    if now_people>count_max_peoples:
        count_max_peoples=now_people
print(p_list)
print(count_max_peoples)