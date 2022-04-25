'''
--url--
https://www.acmicpc.net/problem/10707

--title--
10707번: 수도요금

--problem_description--
JOI군이 살고 있는 지역에는 X사와 Y사, 두 개의 수도회사가 있다
두 회사의 수도요금은 한 달간 수도의 사용량에 따라 다음과 같이 정해진다.
JOI군의 집에서 한 달간 쓰는 수도의 양은 P리터이다.
수도요금이 최대한 싸게 되도록 수도회사를 고를 때, JOI군의 집의 1달간 수도요금을 구하여라.

--problem_input--
입력은 5줄이고 한 줄에 하나씩 정수가 입력된다.
입력되는 정수 A,B,C,D,P는 전부 1 이상 10000 이하이다.

--problem_output--
JOI군의 집에서 지불하는 한 달간 수도요금을 첫째 줄에 출력한다.

'''
x = int(input())
y_basic = int(input())
y_limit = int(input())
y_add_fee = int(input())
u = int(input())
y = y_basic + ((u - y_limit) * y_add_fee if u > y_limit else 0)
# print(f"{y_basic} + (({u}-{y_limit}) * {y_add_fee} if u <= y_limit else 0)")

# print(x * u, y)
print(min(x * u, y))
