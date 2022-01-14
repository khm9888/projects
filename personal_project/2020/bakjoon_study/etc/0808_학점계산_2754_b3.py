'''
--url--
https://www.acmicpc.net/problem/2754

--title--
2754번: 학점계산

--problem_description--


	어떤 사람의 C언어 성적이 주어졌을 때, 평점은 몇 점인지 출력하는 프로그램을 작성하시오.


	A+: 4.3, A0: 4.0, A-: 3.7


	B+: 3.3, B0: 3.0, B-: 2.7


	C+: 2.3, C0: 2.0, C-: 1.7


	D+: 1.3, D0: 1.0, D-: 0.7


	F: 0.0

--problem_input--


	첫째 줄에 C언어 성적이 주어진다
성적은 문제에서 설명한 13가지 중 하나이다.

--problem_output--


	첫째 줄에 C언어 평점을 출력한다.

'''

grade = input()

if grade[0]=="A":
    score=4
elif grade[0]=="B":
    score=3
elif grade[0]=="C":
    score=2
elif grade[0]=="D":
    score=1
elif grade[0]=="F":
    score=0

if grade[0]!="F":
	if grade[1]=="+":
		score+=0.3
	elif grade[1]=="0":
		pass
	elif grade[1]=="-":
		score-=0.3
print(float(score))