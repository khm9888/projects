'''
--url--
https://www.acmicpc.net/problem/1439

--title--
1439번: 뒤집기

--problem_description--
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다
다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다
다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다
뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
예를 들어 S=0001100 일 때,
하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.
문자열 S가 주어졌을 때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오.

--problem_input--
첫째 줄에 문자열 S가 주어진다
S의 길이는 100만보다 작다.

--problem_output--
첫째 줄에 다솜이가 해야하는 행동의 최소 횟수를 출력한다.

'''

cnt=-1
v = input()
entire_length=len(v)
zero_cnt = v.count("0")
one_cnt = entire_length-zero_cnt
cnt2 = min(zero_cnt,one_cnt)
# print(zero_cnt)
for i,j in enumerate(v):
    if i!=0 and j!=v[i-1]:
        cnt+=1
if cnt==-1:
    cnt=0
print(min(cnt,cnt2))