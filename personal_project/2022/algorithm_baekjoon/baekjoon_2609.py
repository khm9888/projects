#두 숫자의 최소공배수와 최대공약수를 찾으려면, 소인수분해부터 해야할 거 같음.

# # 1번. 이미 구현되어 있는 math library 사용

# import math

# a,b = list(map(int,input().split()))
# print(math.gcd(a, b))
# print(math.lcm(a, b))

# 2번. 유클리드 호제법 이용

a,b = list(map(int,input().split()))

if a>=b:
    pass
else:
    a,b=b,a
    
def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))

