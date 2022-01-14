# #ch35 클래스 속성과 클래스 메서드, 정적 메서드

# class Person:
#     def __init__(self):
#         self.bag = []#코드를 수정했더니 수정되었다.
    
#     def put_bag(self, stuff):
#         self.bag.append(stuff)

# james = Person()
# james.put_bag("책")

# maria = Person()
# maria.put_bag("열쇠")

# print(james.bag)
# print(maria.bag)

#######################

# class Knight:
#     __item_limit = 10    # 비공개 클래스 속성
 
#     def print_item_limit(self):
#         print(Knight.__item_limit)    # 클래스 안에서만 접근할 수 있음
 
 
# x = Knight()
# x.print_item_limit()    # 10
 
# print(Knight.__item_limit) 


###############################3

# class Person:
#     '''사람 클래스입니다.'''
    
#     def greeting(self):
#         '''인사 메서드입니다.'''
#         print('Hello')
 
# print(Person.__doc__)             # 사람 클래스입니다.
# print(Person.greeting.__doc__)    # 인사 메서드입니다.
 
# maria = Person()
# print(maria.greeting.__doc__)  

# class Person:
#     "사람클래스 입니다"

# print(Person.__doc__)

#######################################

# class Calc:
#     @staticmethod
#     def add(a,b):
#         print(a+b)
        
#     @staticmethod
#     def mul(a,b):
#         print(a*b)
        
# Calc.add(10,20)
# Calc.mul(10,20)
#######################################

# class Person:
#     count = 0
    
#     def __init__(self):
#         Person.count +=1
        
#     @classmethod
#     def print_count(cls):
#         """cls로 클래스 속성에 접근"""
#         print(f"{cls.count}명이 생성되었습니다.")
        
# james = Person()
# maria = Person()

# Person.print_count()
# print(Person.count)
# print(Person.print_count.__doc__)

#########################################33

# class Date:
                                                                
#     @staticmethod
#     def is_date_valid(date):
#         date_list= list(map(int,date.split("-")))
#         if 1<=date_list[1]<=12 and 1<=date_list[-1]<=31:
#             return True
#         else:
#             return False
 
# if Date.is_date_valid('2000-10-31'):
#     print('올바른 날짜 형식입니다.')
# else:
#     print('잘못된 날짜 형식입니다.')


#######################################

# 표준 입력으로 시:분:초 형식의 시간이 입력됩니다. 
# 다음 소스 코드에서 Time 클래스를 완성하여 시, 분, 초가 출력되게 만드세요. 
# from_string은 문자열로 인스턴스를 만드는 메서드이며 
# is_time_valid는 문자열이 올바른 시간인지 검사하는 메서드입니다. 
# 시간은 24시까지, 분은 59분까지, 초는 60초까지 있어야 합니다. 
# 정답에 코드를 작성할 때는 class Time:에 맞춰서 들여쓰기를 해주세요.

# judge_class_static_class_method.py
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    @staticmethod
    def is_time_valid(time_string):
        time_string = time_string.split(":")
        check = list(map(int,time_string))
        return check[0]<=23 and check[1]<=59 and check[2]<=59
    
    @classmethod
    def from_string(cls,time_string):
        time_string = time_string.split(":")
        check = list(map(int,time_string))
        t = cls(check[0],check[1],check[2])
        return t

    
time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
# 예
# 입력
# 23:35:59
# 결과
# 23 35 59