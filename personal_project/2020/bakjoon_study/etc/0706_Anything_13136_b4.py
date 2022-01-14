'''
--url--
https://www.acmicpc.net/problem/13136

--title--
13136번: Do Not Touch Anything

--problem_description--
ACM-ICPC 대회의 대회장은 R행 C열의 직사각형 형태로 좌석이 배치되어 있다. 대회가 시작하기 전에는 참가자들이 아무것도 만지면 안 되기 때문에 진행자는 'Do not touch ANYTHING!!!'을 연신 외친다.

하지만, 진행자가 성대결절에 걸리면서 'Do not touch ANYTHING!!!'을 외칠 수 없는 처지가 되었다. 따라서 주최측은 CCTV를 설치하여 참가자들을 감시하려고 한다. 이때, 각 CCTV는 N행 N열의 직사각형 영역의 좌석을 촬영할 수 있다.

모든 좌석을 전부 촬영하도록 CCTV를 배치할 때, 최소 몇 개의 CCTV가 필요할까?

--problem_input--
None

--problem_output--
모든 좌석을 전부 촬영하도록 CCTV를 배치할 때, 필요한 CCTV의 최소 개수를 출력한다.

'''

vals = list(map(int,input().split()))
if vals[0]%vals[2]!=0:
    a=vals[0]//vals[2]+1
else:
    a=vals[0]//vals[2]
if vals[1]%vals[2]!=0:
    b=vals[1]//vals[2]+1
else:
    b=vals[1]//vals[2]

print(a*b)