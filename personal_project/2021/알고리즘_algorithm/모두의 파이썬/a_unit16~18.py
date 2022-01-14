# #unit16 - 응용 미로 찾기 알고리즘

# #16-1.py

# maze = {

#     'a': ['e'],
#     'b': ['c', 'f'],
#     'c': ['b', 'd'],
#     'd': ['c'],
#     'e': ['a', 'i'],
#     'f': ['b', 'g', 'j'],
#     'g': ['f', 'h'],
#     'h': ['g', 'l'],
#     'i': ['e', 'm'],
#     'j': ['f', 'k', 'n'],
#     'k': ['j', 'o'],
#     'l': ['h', 'p'],
#     'm': ['i', 'n'],
#     'n': ['m', 'j'],
#     'o': ['k'],
#     'p': ['l']

# }

# #지나간 루트를 기록하는 리스트
# #끝났을 목적지 기록

# def solve(maze,start,end):
#     qu = list()
#     done = list()
    
#     qu.append(start)
#     done.append(start)
    
#     while qu:
#         p = qu.pop(0)
#         print(f"p:{p}")
#         v = p[-1]
#         print(f"v:{v}")
#         if v == end:
#             return p
#         for x in maze[v]:
#             if x not in done:
#                 qu.append(p+x)
#                 done.append(x)
#     return "?"

# print(solve(maze,"a","p"))

# #unit17. 가짜 동전 찾기 알고리즘

# #17-1

# #주어진 동전 n개 중에 가짜 동전(fake)을 찾아내는 알고리즘
# #입력 전체 동전 위치의 시작과 끝
# #출력 가짜 동전의 위치

# def weigh(a,b,c,d):
#     fake = 29
#     if a<=fake<=b:
#         return -1
#     if c<=fake<=d:
#         return 1
#     return 0

# def find_fakecoin(left,right):
#     for x in range(left+1,right+1):
#         result = weigh(left,left,x,x)
#         if result == -1:
#             return left
#         elif result == 1:
#             return x
    
#     return -1

# n = 100

# print(find_fakecoin(0,n-1))

# #17-2

# def weigh(a,b,c,d):
#     fake = 29
#     if a<=fake<=b:
#         return -1
#     if c<=fake<=d:
#         return 1
#     return 0

# def find_fakecoin_2(left,right):#0 ~ n-1 까지
#     if left==right:
#         return left
#     half = (right-left+1)//2
#     g1_left = left
#     g1_right = left+half-1
    
#     g2_left = left+half
#     g2_right = g2_left+half-1
    
#     print(g1_left,g1_right,g2_left,g2_right,half)
    
#     result = weigh(g1_left,g1_right,g2_left,g2_right)
#     if result == -1:
#         return  find_fakecoin_2(g1_left,g1_right)
#     elif result == 1:
#         return  find_fakecoin_2(g2_left,g2_right)
#     else:
#         return right
    
# n = 100
# print(find_fakecoin_2(0,n-1))

#unit18 최대수익알고리즘

#18-1.py

# stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]

# max_profit = 0
# def max_profit(stock):
#     n = len(stock)
#     max_value =0
    
#     for i in range(0,n-1):
#         for j in range(i+1,n):
#             profit = stock[j]-stock[i]
#             if max_value<profit:
#                 max_value=profit
#                 start_day=i
#                 end_day=j
#                 # print(stock[i])
#                 # print(stock[j])
#     return max_value,start_day,end_day

# print(max_profit(stock))
    
#18-2.py

def max_profit(prices):
    n = len(prices)
    max_value = 0
    min_price = prices[0]
    for i in range(1,n):
        profit = prices[i]-min_price
        if profit>max_value:
            max_value=profit
        if prices[i]<min_price:
            min_price=prices[i]
    
    return max_value

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))

#18-3

import time     # 시간 측정을 위한 time 모듈

import random   # 테스트 주가 생성을 위한 random 모듈

 

# 최대 수익: 느린 O(n * n) 알고리즘

def max_profit_slow(prices):
    n = len(prices)
    max_profit = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

# 최대 수익: 빠른 O(n) 알고리즘

def max_profit_fast(prices):
    n = len(prices)
    max_profit = 0
    min_price = prices[0]
    for i in range(1, n):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]
    return max_profit


def test(n):
    a = []
    for i in range(0, n):
        a.append(random.randint(5000, 20000))
    # 느린 O(n * n) 알고리즘 테스트
    start = time.time()       # 계산 시작 직전 시각을 기억
    mps = max_profit_slow(a)  # 계산 수행
    end = time.time()         # 계산 시작 직후 시각을 기억
    time_slow = end - start   # 직후 시각에서 직전 시각을 빼면 계산에 걸린 시간
    # 빠른 O(n) 알고리즘 테스트
    start = time.time()       # 계산 시작 직전 시각을 기억
    mpf = max_profit_fast(a)  # 계산 수행
    end = time.time()         # 계산 시작 직후 시각을 기억
    time_fast = end - start   # 직후 시각에서 직전 시각을 빼면 계산에 걸린 시간

    # 결과 출력: 계산 결과

    print(n, mps, mpf)  # 입력 크기, 각각 알고리즘이 계산한 최대 수익 값(같아야 함)

    # 결과 출력: 계산 시간 비교

    m = 0 # 느린 알고리즘과 빠른 알고리즘의 수행 시간 비율을 저장할 변수

    if time_fast > 0:  # 컴퓨터 환경에 따라 빠른 알고리즘 시간이 0으로 측정될 수 있음

                       # 이럴 때는 0을 출력

        m = time_slow / time_fast # 느린 알고리즘 시간 / 빠른 알고리즘 시간

    # 입력 크기, 느린 알고리즘 수행 시간, 빠른 알고리즘 수행 시간, 계산 시간 차이

    # %d는 정수 출력, %.5f는 소수점 다섯 자리까지 출력을 의미

    print("%d %.5f %.5f %.2f" % (n, time_slow, time_fast, m))

 

test(100)

test(10000) 
