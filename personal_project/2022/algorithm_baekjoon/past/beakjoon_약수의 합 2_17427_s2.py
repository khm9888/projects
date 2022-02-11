'''
--url--
https://www.acmicpc.net/problem/17427

--title--
17427번: 약수의 합 2

--problem_description--
두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다
예를 들어, 2의 약수는 1, 2가 있고, 24의 약수는 1, 2, 3, 4, 6, 8, 12, 24가 있다
자연수 A의 약수의 합은 A의 모든 약수를 더한 값이고, f(A)로 표현한다
x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.
자연수 N이 주어졌을 때, g(N)을 구해보자.

--problem_input--
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

--problem_output--
첫째 줄에 g(N)를 출력한다.

'''

# https://enhjh.tistory.com/37 
# 약수의 합 구하는 공식. O(n)으로 줄임.

q_number = int(input())
sum_value=0
for i in range(1, q_number+1):
    	# i의 배수의 개수 = i를 약수로 갖는 수
    sum_value += (q_number//i)*i

print(sum_value)
    