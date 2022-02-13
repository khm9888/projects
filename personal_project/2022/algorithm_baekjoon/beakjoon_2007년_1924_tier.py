'''
--url--
https://www.acmicpc.net/problem/1924

--title--
1924번: 2007년

--problem_description--
오늘은 2007년 1월 1일 월요일이다
그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

--problem_input--
첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다
참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

--problem_output--
첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

'''
x,y = tuple(map(int,input().split()))#값을 입력받아서 x,y에 대입하는 함수

#1/1-월 31일 // 7 - 3
#2/1-목 28일 // 7  0
#3/1-목 
#4/1-일
#5/1-화
#6/1-금
#7/1-일
#8/1-수
#9/1-목
#10/1-토
#11/1-화
#12/1-목

# 1. datetime 라이브러리. 활용
# 2. 월별로 계산을 해서, 각 월의 첫번째 요일계산하게끔 만들기.

def find_day(month,day):
    find_end_days=dict()
    month1 = [1, 3, 5, 7, 8, 10, 12]#31
    for m in month1:
        find_end_days[m]=31
    month2 = [4, 6, 9, 11]#30
    for m in month2:
        find_end_days[m]=30
    month3 = [2]#28
    for m in month3:
        find_end_days[m]=28
    total_day = day
    # print(51,total_day)
    for d in range(1,month):
        total_day+=find_end_days[d]
    total_day%=7
    day_transform_list=["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    # print(month,day,day_transform_list[total_day])
    print(day_transform_list[total_day])
# for i in range(1,13):
#     find_day(i,1)
find_day(x,y)
