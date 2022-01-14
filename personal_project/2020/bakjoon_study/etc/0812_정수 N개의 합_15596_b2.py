'''
--url--
https://www.acmicpc.net/problem/15596

--title--
15596번: 정수 N개의 합

--problem_description--
정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
작성해야 하는 함수는 다음과 같다.

--problem_input--
'''
#1
def solve(a):
    	sum=0
	for i in a:
		sum+=i
	return sum

#2
solve=sum

#3
def solve(a):
	return sum(a)