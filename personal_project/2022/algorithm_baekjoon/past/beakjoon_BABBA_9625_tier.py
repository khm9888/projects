'''
--url--
https://www.acmicpc.net/problem/9625

--title--
9625번: BABBA

--problem_description--
상근이는 길을 걷다가 신기한 기계를 발견했다
기계는 매우 매우 큰 화면과 버튼 하나로 이루어져 있다.
기계를 발견했을 때, 화면에는 A만 표시되어져 있었다
버튼을 누르니 글자가 B로 변했다
한 번 더 누르니 BA로 바뀌고, 그 다음에는 BAB, 그리고 BABBA로 바뀌었다
상근이는 화면의 모든 B는 BA로 바뀌고, A는 B로 바뀐다는 사실을 알게되었다.
버튼을 K번 눌렀을 때, 화면에 A와 B의 개수는 몇 개가 될까?

--problem_input--
첫째 줄에 K (1 ≤ K ≤ 45)가 주어진다.

--problem_output--
첫째 줄에 A의 개수와 B의 개수를 공백으로 구분해 출력한다.

'''

k = int(input())

a = [1, 0]
b = [0, 1]

for i in range(2, k + 1):
    a_num = a[i - 1] + a[i - 2]
    a.append(a_num)
    b_num = b[i - 1] + b[i - 2]
    b.append(b_num)

print(a[k], b[k])