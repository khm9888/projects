'''
--url--
https://www.acmicpc.net/problem/2751

--title--
2751번: 수 정렬하기 2

--problem_description--
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

--problem_output--
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

'''
# # # #계속된 시간초과


# import sys 
# input = sys.stdin.readline
# n = int(input())
# values=[int(input()) for i in range(n)]

# def gapInsertionSort(values, start, gap):
#     for target in range(start+gap, len(values), gap):
#         val = values[target]
#         i = target
#         while i > start:
#             if values[i-gap] > val:
#                 values[i] = values[i-gap]
#             else:
#                 break
#             i -= gap
#         values[i] = val

# def shellSort(values):
#     gap = len(values) // 2
#     while gap > 0:
#         for start in range(gap):
#             gapInsertionSort(values, start, gap)
#         gap = gap // 2
#     return values 

# values =  shellSort(values)
            
# for i in values:
#     print(i)




# # # #계속된 시간초과




#1. set & sorted()

import sys 
input = sys.stdin.readline
n = int(input())
v= set()
[(v.add(int(input()))) for i in range(n)]

[print(i) for i in sorted(v)]
    
#2. sort()
import sys

data = []
for i in range(int(input())):
    data.append(int(sys.stdin.readline()))

data.sort()
for i in data:
    print(i)


#결론, 왠만한 정렬보다 기본 sort 함수가 더 빠름..