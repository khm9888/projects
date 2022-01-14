'''
--url--
https://www.acmicpc.net/problem/19538

--title--
19538번: 루머

--problem_description--
당신은 루머를 믿는가?
한 유명 심리학 실험에서는 사람들에게 두 개의 줄을 보여주고, 어떤 줄이 더 긴지 말하라 했다
사실 한 사람을 제외하고 나머지는 실험자에 의해 사전에 조작된 사람들이었다
조작된 사람들은 사실상 더 짧은 줄을 더 길다고 말했다
주변 모두가 같은 답변을 하자, 진짜 피실험자 또한 짧은 줄이 더 길다고 말했다
이 실험은 사람들이 주변인의 영향을 강하게 받는다는 것을 보여주었는데, 루머도 이와 같다.
루머는 최초 유포자로부터 시작한다
최초 유포자는 여러 명일 수 있고, 최초 유포자를 제외하고 스스로 루머를 만들어 믿는 사람은 없다.
매분 루머를 믿는 사람은 모든 주변인에게 루머를 동시에 퍼트리며, 군중 속 사람은 주변인의 절반 이상이 루머를 믿을 때 본인도 루머를 믿는다.
루머를 믿는 순간부터 다른 말은 듣지 않기 때문에, 한번 믿은 루머는 계속 믿는다.
이때, 사람들이 루머를 처음 믿기 시작하는 시간을 알아내 보자.

--problem_input--
첫째 줄에 사람의 수 이 주어진다. () 이는 번 사람부터 번 사람까지 있음을 의미한다.

둘째 줄부터 개의 줄이 주어진다. 이 중 번째 줄에는 번 사람의 주변인들의 번호와 입력의 마지막을 나타내는 0이 공백으로 구분되어 주어진다. 번호는  이상  이하의 자연수이고, 같은 줄에 중복된 번호는 없다. 자기 자신이 주변인이거나 일방적으로 주변인인 경우는 없으며, 전체 양방향 주변인 관계는 개를 넘지 않는다.

다음 줄에는 루머를 퍼뜨리는 최초 유포자의 수 이 주어진다. 
마지막 줄에는 최초 유포자의 번호가 공백으로 구분되어 주어진다. 최초 유포자의 번호는 중복되지 않는다.

출력
개의 정수 을 공백 단위로 출력한다. 는 번 사람이 루머를 처음 믿기 시작한 시간(분)이며, 충분히 많은 시간이 지나도 루머를 믿지 않을 경우 이다. 최초 유포자는 루머를 분부터 믿기 시작했다고 생각한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
connect_dict = dict()
connects = [list(map(int,input().split())) for i in range(n)]
for i,v in enumerate(connects):
    connect_dict[i+1]=v 
print(connect_dict) #{1: [2, 3, 0], 2: [1, 3, 0], 3: [1, 2, 4, 0], 4: [3, 5, 0], 5: [4, 0], 6: [0], 7: [0]}
m = int(input())
believes = [False]*(n+1)

num = list(map(int,input().split()))
time =[-1]*(n+1)

def search(num,t):
    for n in num:
        if t==0:
            believes[n]=True
        if n==0:
            return
        else:
            if ((believes[n]== False) or  believes[n]==True and time[n]>t) and connect_dict[n]:
                time[n]=t
                print(f"n:{n},t:{t}")
                search(connect_dict[n],t+1)

# for t in range(len(time)-1):
# print(f"t:{t}")
print(f"num:{num}")
search(num,0)#search([1,6],0)
for t in time[1:]:
    print(t, end=" ")