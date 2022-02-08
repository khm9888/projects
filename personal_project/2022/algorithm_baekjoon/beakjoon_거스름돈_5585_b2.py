'''
--url--
https://www.acmicpc.net/problem/5585

--title--
5585번: 거스름돈

--problem_description--
타로는 자주 JOI잡화점에서 물건을 산다
JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다
타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.

--problem_input--
입력은 한줄로 이루어져있고, 타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져있다.

--problem_output--
제출할 출력 파일은 1행으로만 되어 있다
잔돈에 포함된 매수를 출력하시오.

'''

price = int(input())

charge_list =[500,100,50,10,5,1]

charge = 1000-price
count_coin=0

for coin_kind in charge_list:
    count_coin+=charge//coin_kind
    charge=charge%coin_kind
#     print("coin_kind",coin_kind)
#     print("count_coin",count_coin)
#     print("charge",charge)
    if not charge:
        break

print(count_coin)