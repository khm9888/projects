'''
--url--
https://www.acmicpc.net/problem/1748

--title--
1748번: 수 이어 쓰기 1

--problem_description--
1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.
1234567891011121314151617181920212223...
이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 N(1 ≤ N ≤ 100,000,000)이 주어진다.

--problem_output--
첫째 줄에 새로운 수의 자릿수를 출력한다.

'''

number = int(input())
num_loc = len(str(number)) #9 ->1 #20 - 2
total_length=0

for e in range(1,num_loc+1):
    if number>=10**e:
        add_one = (int((10**e)*0.9*e))
        total_length+=add_one
    else:
        # print("else")
        add_one = (number-10**(e-1)+1)*e
        total_length+=add_one
    # print(e,add_one,total_length)
print(total_length)