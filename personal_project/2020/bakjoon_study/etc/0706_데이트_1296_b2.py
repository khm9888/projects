'''
--url--
https://www.acmicpc.net/problem/1296

--title--
1296번: 데이트

--problem_description--
오민식은 자기가 좋아하는 여자 N명 중에 한 명과 함께 데이트하러 나가고 싶어한다.

하지만 N명 모두를 사랑하는 오민식에게는 한 명을 선택하고 나머지 여자를 버리는 것은 슬픈 결정이기 때문에 누구를 선택해야 할지 고민에 빠졌다.

마침 오민식은 사랑계산기를 얻었다. 사랑계산기는 두 사람의 이름을 이용해서 두 사람이 성공할 확률을 계산해 준다. 사랑계산기는 다음과 같이 작동한다.

위의 개수를 모두 계산 한 후에 확률 계산은 다음과 같이 한다.

((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) mod 100

오민식의 영어 이름과 나머지 여자들의 이름이 주어졌을 때, 오민식과 성공할 확률이 가장 높은 여자의 이름을 출력하는 프로그램을 작성하시오. 여러명일 때에는 알파벳으로 가장 앞서는 이름을 출력하면 된다.

--problem_input--
첫째 줄에 오민식의 영어 이름이 주어진다. 둘째 줄에는 좋아하는 여자가 몇 명인지 N이 주어지고, 셋째 줄부터 N개의 줄에 여자의 이름이 하나 씩 주어진다. N은 50보다 작거나 같고, 모든 이름은 알파벳 대문자로만 구성되어 있고 모두 길어야 20글자이다.

--problem_output--
오민식이 선택한 여자의 이름을 출력한다.

'''

man = input()
n = int(input())
women = [input() for _ in range(n)]
women.sort()
values=[]

for i,w in enumerate(women):
    names = man+w
    L = names.count("L")
    O = names.count("O")
    V = names.count("V")
    E = names.count("E")
    value = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    values.append(value)

print(women[values.index(max(values))])
        
    
