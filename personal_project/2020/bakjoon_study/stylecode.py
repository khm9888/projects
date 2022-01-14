# 파이썬 스타일 코드


# 파이썬 코드는 잘 활용만 하면 굉장히 짧은 코드로, 구현이 가능함.

colors=['red','blue','green','yellow'] 
result=''.join(colors) 
print(result) 

# redbluegreenyellow

# # ⊙ split() 함수
items='zero one two three'.split() 
print(items) 

# ['zero','one','two','three']

# # ⊙ join() 함수

colors=['red','blue','green'] 
result=','.join(colors) 

# 'red,blue,green,yellow'


# 문자열을 합칠 때 유용하게 쓰이는 함수.

# 사용법은 위와 같음

# # 리스트 컴프리헨션

# 리스트 컴프리헨션의 기본 개념은 기존 리스트형을 사용하여 간단하게 새로운 리스트를

# 만드는 기법이다. 리스트와 for문을 한 줄에 사용할 수 있는 장점이 있다.


result = [] 

for i in range(10): 

    result.append(i)

# 


# 위의 구조가 일반적인 반복문 + 리스트의 구조이다.

result=[i+1 for i in range(10)] # 앞의 i+1은 Append할 값 
print(result) 

# [1,2,3,4,5,6,7,8,9,10]


# ==> 위의 구조를 리스트 컴프리헨션 방법으로 바꿔 본 코드이다.

#        위와 같이 씀으로써 간단하게 표현이 가능하다. 

#        익숙하지 않아서 처음에는 문법파괴에 당황스러우나, 보다보면 나름 익숙해진다.

# ​

# ⊙ 리스트 컴프리헨션 용법 : 필터링


# 필터링은 if문과 함께 사용하는 리스트 컴프리헨션이다.

print(result=[i for i in range(10) if i % 2 == 0])
print(result) 
# [0,2,4,6,8]

# 위는 짝수일때만 result에 i값을 추가하는 코드이다.

result=[i if i%2==0 else 10 for i in range(10)] 
print(result) 

# [0,10,2,10,4,10,6,10,8,10]


# 위 코드처럼 if문을 앞으로 옮겨 else 문과 함께 사용하면, 조건을 만족하지 않을 때,

# else 뒤에 i의 값을 할당하는 코드를 작성할 수 있다.


# ! 주의 ! if문을 앞으로(<-) 당겨서 쓰게 된다면, else문을 필수적으로 써주어야 한다.


# # ⊙ 리스트 컴프리헨션 용법 : 중첩 반복문

result=[i+j for i in range(5) for j in range(5)] 
print(result) 

# [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8]


# # ⊙ 리스트 컴프리헨션 용법 : 중첩 반복문 + 필터링

  
case_1=["A","B","C"] 
case_2=["D","E","A"] 
result=[i+j for i in case_1 for j in case_2 if not(i==j)] 
result 

# ['AD', 'AE', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']


# ==> 당연한 얘기지만, 여기서 i,j는 인덱스가 아닌 "A","B"와 같은 값이다.

#        인덱스를 할당하려면 for i in range() 형식을 쓰면 된다.


# index & 값 모두 이용하고 싶으면??? => enumerate() 함수 이용


# ⊙ 리스트 컴프리헨션 용법 : 이차원 리스트


# # 방법 ①
words=[]
words=[chr(i) for i in range(65,70)]
stuff=[[w.upper(),w.lower(),len(w)] for w in words] 
print(stuff)

# ==> 안에 리스트를 만들고, 뒤에 for문을 돌리면 된다.

# # 방법 ②


result=[[i+j for i in case_1] for j in case_2]
print(result)

# ⊙ 꼭 구분해야 하는 코드

# ① 
[i+j for i in case_1 for j in case_2]
# ② 
[[i+j for i in case_1] for j in case_2]


# ==> 첫 번째 코드는 앞의 for문이 먼저 실행된다. 두 번째 코드는 뒤의 for문이 먼저 실행된다.

# # enumerate() Function

# 리스트 값을 추출할 때 인덱스를 붙여 함께 출력하는 방법이다.
for i,v in enumerate(['tic','tac','toc']): # 언패킹 
    print(i,v) 

# 0 tic 
# 1 tac 
# 2 toc

# enumerate() 함수는 주로 인덱스를 키로, 단어를 값으로 하여 쌍으로 묶어

# 결과를 출력하는 방식을 사용한다.


# zip() Function

# 1개 이상의 리스트 값이 같은 인덱스에 있을 때 병렬로 묶는 함수이다.

alist=['a1','a2','a3'] 
blist=['b1','b2','b3'] 
for a,b in zip(alist,blist): 
     print(a,b) 

#np/df 와 비슷

# a1 b1 

# a2 b2 

# a3 b3


# ⊙ zip() 함수의 활용

print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])

# [111,222,333]


# ==> 위와 같은 기능은 벡터 덧셈이나 행렬의 덧셈 등에 유용하게 쓰인다.


# enumerate() & zip()

alist=['a1','a2','a3'] 
blist=['b1','b2','b3'] 
for i, (a,b) in enumerate(zip(alist,blist)): 
    print(i,a,b) 

    # 0 a1 b1 

    # 1 a2 b2 

    # 2 a3 b3


# ==> alist와 blist를 묶고, 같은 인덱스 값까지 같이 묶어 출력하였다.

print("--------------------파이썬 스타일 코드2----------------------")

# 파이썬 스타일 코드2


# 람다(lambda) Function


# 함수 자체를 다른 함수의 인자로 넘기기 위해 주로 사용하고, 주로 단순히 인자로 넘길

# 목적으로 생성하므로 별도의 이름을 지정하지 않는다.


# # lambda arguments : expression


print((lambda x:x+1)(5))


# 람다함수는 위 코드처럼 괄호에 람다 함수를 넣고, arguments로 5를 입력한 것으로

# 사용이 가능하다.



# map() Function

# map(function,iterable)
ex=[1,2,3,4,5] 
f=lambda x:x**2 
print(list(map(f,ex))) 

# [1,4,9,16,25]


# map(f,ex) 코드를 해석하면, 함수 f를 ex의 각 요소에 Mapping하라라는 뜻이다.

# list()로 감싸주는 이유는, 파이썬 3.x버젼부터는 list를 붙여야 리스트로 반환하기 때문


# ⊙ map() 함수 : 필터링 기능


# map()함수도 리스트 컴프리헨션처럼 필터링 기능을 사용할 수 있다. 단, 한 가지 기억

# 해야하는 점은, 리스트 컴프리헨션과 달리 else문을 반드시 작성해야 한다는 점이다.

# ​
list(map(lambda x:x**2 if x%2==0 else x,ex)) # map() 필터링 

# [1,4,3,16,5] 
[x**2 if x%2==0 else x for x in ex] # 리스트 컴프리헨션 필터링 

# [1,4,3,16,5]


# reduce() Function

# ​

# reduce() 함수는 map() 함수와 용법은 다르지만, 형제처럼 함께 사용하는 함수이다.

# reduce() 함수는 리스트와 같은 시퀀스 자료형에 차례대로 함수를 적용하여 하나의

# 통합된 값만 리턴한다.

from functools import reduce
   print(reduce(lambda x,y: x+y,[1,2,3,4,5]))   



# 15


# ==> 계산 과정

# 1+2 = 3

# 3+3 = 6

# 6+4=10

# 10+5=15

# 누적해서 계산을 한다고 생각하면 편할 듯 하다.

# reduce() 함수가 어떤 식으로 구성되었는지를 흉내내어 본다면, 재귀적으로

# 이루어져 있을 것이다. 이를 간단하게 표현하면 다음과 같다.


# function(function(function(function(function(10, 1), 2), 3), 4), 5)


# # *(asterisk)

# *는 여러개의 변수를 담는 컨테이너라고 생각을 하자.

# * : Tuple형으로 여러 변수를 담음.

# ** : Dictionary 형으로 여러 변수를 담음.​

# ⊙ asterisk의 언패킹 기능


   def asterisk_test(a,args): #type 확인

    print(a,*args) 

    print(type(args)) 

asterisk_test(1,(2,3,4,5,6)) 

    # 1 2 3 4 5 6


# ==> 매개변수 인자는 Tuple형인데, 출력할때 *를 사용했더니

# 언패킹되어 출력된 것을 볼 수 있다.


# ==> **는 딕셔너리형을 언패킹하는 효과를 볼 수 있다.


# 선형대수학


# 선형대수학에 나오는 행렬, 벡터 등의 연산을 파이썬 스타일 코드로 표현하면

# 간결하게 코드로 표현이 가능하다.

u=[2,2] 
v=[2,3] 
z=[3,5] 
result=[sum(x) for x in zip(u,v,z)] 
print(result) 

# [7,10]


# 위 코드를 이런 식으로도 표현 가능하다.


def vector(*args): 

    return [sum(t) for t in zip(*args)] 

vector(u,v,z) 

# [7,10]


# ⊙ 행렬의 연산

matrix_a=[[3,6],[4,5]] 
matrix_b=[[5,8],[6,7]] 
[[sum(row) for row in zip(*t)] for t in zip(matrix_a,matrix_b)] 
print(result) 

    # [[8,14],[10,12]]


# ==> zip() 함수는 같은 인덱스에 있는 값들이 추출되므로, 처음에

# [3,6]과 [5,8]이 Tuple로 묶여 ([3,6],[5,8])로 추출된다.


all([row[0]==value for t in zip(matrix_a,matrix_b) 

    for row in zip(*t) for value in row])


# ⊙ all & any

any([False,False,False]) 

    # False 
any([True,False,False]) 

    # True 
all([False,True,True]) 

    # False 
all([True,True,True]) 

    # True


# ==> any는 or 연산, all은 and 연산



#
print("+"*20)

#  Generator

# list의 문제점 중 하나는 그 길이가 매우 커질 수 있다는 점이다.

# 위의 예시는 정말 간단하게 보여 주었지만 list 원소가 100만 개가 있다고 했을 때

# 예를 들어 for 문을 돌리가 위해 100만 개를 모두 생성하여 메모리에 저장하는 것은 낭비이다.

# ​

# 쉽게 설명하면 for i in [1,2,3,4]에서 [1,2,3,4]는 한 번에 메모리에 저장하지만

# x=[1,2,3,4]를 generator로 저장해서 for i in x를 하면 1~4를 하나씩 가지고 오면서 진행한다.

# ​

# 이때 iterator의 한 종류인 Generator을 사용하면 반복 요청이 있을 시에

# 한 번에 하나씩 생성하게 한다.

#예제 1, 안 돌아감

def fun(n):
    print(n)
    while True:
        n+=1
        if n%2==0:
            yield 2*n
        else:
            yield 2*n+1
        # if n>20:
        #     break
# print(list(fun()))

x=fun(3)

print(next(x))

for i in x:n
    print(i)
    if i>=10:
        break

########################################################################
 
#예제 2

def countdown(n): # 01 제너레이터 함수를 정의함

    print("%d 부터 카운트다운 합니다" %n) #02
    while n >= 0: #03
        yield n #04 값을 반환하고 멈춤
        n -= 1 #05 값을 만듬

gen = countdown(5) #06 제너레이터를 생성함

for i in countdown(5):
    print(i)


print(next(gen)) #07
print(next(gen)) #08
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) #09




# ■ Counter

# counter이라는 모듈을 이용

from collections import Counter

#에 있음

# list 안에 값들이 몇 개씩 있는지 알려주는 역할

# dictionary와 비슷한 형태로 표현이 된다.

c = Counter([1,2,3,1])
print(c.most_common(2))

print(c)
x=dict(c).__iter__()

# # iterator

# https://blog.naver.com/pisibook/221700733332

# 어떤 객체가 이터러블인지 아닌지를 좀 더 확실하게 알기 위해서는 다음과 같이  dir() 함수를 사용하여 해당 객체에 "__iter__"라는 메소드가 있는 가를 확인하면 됩니다.

#  "__iter__" 메소드가 있으면 이터러블입니다.

c = Counter([1,2,3,1])
print(c.most_common(2))

print(c)
x=dict(c).__iter__()

print(x.__next__)


it = iter([1, 2, 3])
print(next(it))
# 1
print(next(it))
# 2
print(next(it))
# 3

