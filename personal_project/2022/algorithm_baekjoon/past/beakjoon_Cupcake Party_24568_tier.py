'''
--url--
https://www.acmicpc.net/problem/24568

--title--
24568번: Cupcake Party

--problem_description--
A regular box of cupcakes holds 8 cupcakes, while a small box holds 3 cupcakes
There are 28 students in a class and a total of at least 28 cupcakes
Your job is to determine how many cupcakes will be left over if each student gets one cupcake.

입력
The input consists of two lines.

The first line contains an integer R ≥ 0, representing the number of regular boxes.
The second line contains an integer S ≥ 0, representing the number of small boxes.
출력
Output the number of cupcakes that are left over.
'''
eights = int(input())
threes = int(input())
if (eights * 8 + threes * 3) >= 28:
    print((eights * 8 + threes * 3) - 28)
else:
    print(0)