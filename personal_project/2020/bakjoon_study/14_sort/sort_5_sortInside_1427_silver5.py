'''
--url--
https://www.acmicpc.net/problem/1427

--title--
1427번: 소트인사이드

--problem_description--
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

--problem_input--
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

--problem_output--
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

'''

import sys

input = sys.stdin.readline

v = [w for w in input()]
v.sort(reverse=True)

txt = ""
for w in v:
    txt+=w
print(txt)