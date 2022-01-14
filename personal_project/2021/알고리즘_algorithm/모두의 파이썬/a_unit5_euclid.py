#unit 5_ 최대공약수 구하기

# 1. 두 숫자 중 작은 수를 num을 구한다.

# 2. 큰 숫자를 작은 숫자로 나누었을 때 나누어 떨어지는지 구한다.

# 3. 떨어진다면, 작은 숫자가 최대공약수

# 4 .떨어지지 않는다면, num-1를 하여 2번으로 돌아가 반복한다.

# #5-1
# def gcd(a,b):
#     if a>b:
#         num = b
#     else:
#         num = a
#     while True:
#         if a%num==0 and b%num==0:
#             return num
#         else:
#             num -= 1
            
# print(gcd(100,35))

# #5-2 euclid

# def gcd_2(a,b):
#     if a==0:
#         return b
#     elif b==0:
#         return a
#     print(a,b)
#     return gcd_2(b,a%b)

# print(gcd_2(100,35))
# print(gcd_2(35,100))
# print(gcd_2(200,201))

# #5장 연습문제

# #5-1

def fibonachi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonachi(n-1)+fibonachi(n-2)
for i in range(1,6):
    print(fibonachi(i))
    
