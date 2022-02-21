'''
--url--
https://www.acmicpc.net/problem/24509

--title--
24509번: 상품의 주인은?

--problem_description--
혜민이네 반은 총 $N$명의 학생으로 이루어져 있으며 학생마다 번호가 다르게 배정되어 있다
이번 시험은 국어, 영어, 수학, 과학 총 4과목으로 진행되며, 학생들이 공부를 열심히 할 수 있게 과목별 1등에게 상품을 주기로 했다
수상은 국어, 영어, 수학, 과학 순서로 하며 최대한 많은 학생에게 상품을 주고 싶기 때문에 학생마다 상품은 한 번만 받을 수 있다
예를 들어 국어 과목에서 1등 한 사람이 수학 과목에서 또 1등을 한다면 국어 과목에서 상품을 받았기 때문에 이 학생은 다른 과목에서 상품을 더 받을 수 없다
따라서 수학 과목은 상품을 받지 않은 학생 중에 점수가 가장 높은 학생이 상품을 받는다
단, 동점이 있으면 번호가 빠른 사람이 상품을 받는다
과목별 상 받을 사람의 번호를 출력하시오.

--problem_input--
첫 번째 줄에 학생의 수 $N$($4 \leq N \leq 200\,000$)이 주어진다.
두 번째 줄부터 $N+1$번째 줄까지 $N$개의 줄에 걸쳐서 학생의 번호 $X$($1 \leq X \leq N$)와 학생의 국어 점수 $A$, 영어 점수 $B$, 수학 점수 $C$, 과학 점수 $D$가 순서대로 공백을 기준으로 정수로 주어진다
학생의 번호는 중복될 수 없다
($0 \leq A, B, C, D \leq 100$)

--problem_output--
국어, 영어, 수학, 과학 순서대로 상품을 받는 학생의 번호를 공백으로 구분하여 출력한다.

'''

import sys

input = sys.stdin.readline

count_student=int(input())
student_scores_list=[list(map(int,input().split())) for _ in range(count_student)]

price_had_students_list=list()
for c in range(4):
    # print(f"과목 순서는 {c}")
    # print(f"price_had_students_list:{price_had_students_list}")
    max_score = 0
    order_num = 0
    for s in range(count_student):
        # print(f"--학생 순서는 {s}")
        score=student_scores_list[s][c+1]#과목당 점수
        if max_score<score and student_scores_list[s][0] not in price_had_students_list:
            max_score=score
            student_num=student_scores_list[s][0]
            order_num=student_scores_list[s][0]
            # print(f"student_num:{student_num},score:{score}")
    price_had_students_list.append(student_num)
print(" ".join(map(str,price_had_students_list)))