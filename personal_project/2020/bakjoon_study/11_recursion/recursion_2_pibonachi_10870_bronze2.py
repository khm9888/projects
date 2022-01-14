'''
--url--
https://www.acmicpc.net/problem/10870

--title--
10870번: 피보나치 수 5

--problem_description--
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

None

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.

--problem_output--
첫째 줄에 n번째 피보나치 수를 출력한다.

'''

n = int(input())

pibonachi=[0,1]#len 1

def pibo(n):#2
    if n==0 or n==1:
        return pibonachi[n]
    if len(pibonachi)>=n+1:#2>=3
        # print("case1")
        # print(n,pibonachi)
        return pibonachi[n-2]+pibonachi[n-1]
    elif len(pibonachi)<n+1:#2==2
        # print("case2")
        # print(n,pibonachi)
        pibonachi.append(pibo(n-2)+pibo(n-1))
        return pibonachi[n]

print(pibo(n))
# print(pibonachi)
