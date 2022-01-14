# #import 위치와 다른 파이썬 파일에서 함수 및 클래스 불러오기. 적용


# # def hello(count=5):
# #     if count==0:
# #         return
# #     print("hello~~",count)
    
# #     count-=1
# #     hello(count)
    
# # hello()

# #1

# # def factorial(n):
# #     if n==1 or n==0:
# #         return 1
# #     return n*factorial(n-1)

# # print(factorial(5))

# #2

# # def factorial(n):
# #     if n==1:
# #         return n
# #     return n*factorial(n-1)

# # print(factorial(10))


# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1)+fib(n-2)

# n = int(input())
# print(fib(n))

# #32장

# def plus_ten(x):
#     return 10+x

# print(plus_ten(10))

#lambda

# plus_ten=lambda x:x+10
# print(plus_ten(10))

# #lambda 바로 호출

# print((lambda x:x+10)(10))

#람다 표현식이나, 함수를 인수로 활용

# print(list(map(plus_ten, [1, 2, 3])))

# #map에 객체를 여러 개 넣기

# a= list(range(1,6))
# b= list(range(2,11,2))

# print(list(map(lambda x,y:x*y,a,b)))

# #filter

# def f(x):
#     return x>5 and x<10

# a=list(range(15))
# print(list(filter(f,a)))


# print(list(filter(lambda x:x>5 and x<10,a)))

# def f(x,y):
#     return x+y

# a = list(range(1,6))

# from functools import reduce
# print(reduce(f,a))
# print(reduce(lambda x,y:x+y,a))


#practice quiz##

# files = input().split()
# list(map(lambda x:(3-len(x.split(".")[0]))*"0"+x
# ,files))

##33장##

# def A():
#     x = 10        # A의 지역 변수 x
#     def B():
#         nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용
#         x = 20        # A의 지역 변수 x에 20 할당
 
#     B()
#     print(x)      # A의 지역 변수 x 출력
 
# A()


# ###

# x = 1
# def A():
#     x = 10
#     def B():
#         x = 20
#         def C():
#             global x
#             x = x + 30
#             print(x)
#         C()
#     B()
 
# A()

##closer##

# def calc():
#     a = 3
#     b = 5
#     def mul_add(x):
#         return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
#     return mul_add          # mul_add 함수를 반환
 
# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))


# def calc():
#     a,b=3,5
#     return lambda x:a*x+b

# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))

# #quiz

# def counter():
#     i = 0
#     def count():
#         nonlocal i
#         i += 1
#         return i
#     return count     
 
# c = counter()
# for i in range(10):
#     print(c(), end=' ')
    
#practice quiz##
    
def countdown(n):
    number=int(n)
    def closwer():
        nonlocal number
        number-=1
        return number+1
    return closwer

n = int(input())
 
c = countdown(n)
for i in range(n):
    print(c(), end=' ')