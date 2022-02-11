'''
--url--
https://www.acmicpc.net/problem/11047

--title--
11047번: 동전 0

--problem_description--
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 N과 K가 주어진다
(1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

'''
coin_kind, total_value = tuple(map(int,input().split()))

coin_kind_list = [int(input()) for _ in range(coin_kind)]
coin_kind_list.sort(reverse=True)
# print(coin_kind_list)

charge_count=0
for coin in coin_kind_list:
    charge_count+=total_value//coin
    total_value=total_value%coin
    # print("coin",coin)
    # print("charge_count",charge_count)
    # print("total_value",total_value)
    # print("*"*50)
    if not total_value:
        break
    
print(charge_count)