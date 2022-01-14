# # 36 chapter

# class Person:
#     def greeting(self):
#         print("안녕하세요")
        
        
        
# class Student(Person):
#     def study(self):
#         print("공부하기")
        
# james = Student()
# james.greeting()
# james.study()


# print(issubclass(Student, Person))

# ################33


# class Person:
#     def greeting(self):
#         print("안녕하세요")
        
# class PersonList:
#     def __init__(self) -> None:
#         self.person_list = []
        
#     def append_person(self, person):
#         self.person_list.append(person)
        
# # ##############################

# class Person:
#     def __init__(self) -> None:
#         print("Person __init__")
#         self.hello = "안녕하세요"
        
# class Student(Person):
#     def __init__(self) -> None:
#         print("Student __init__")
#         super().__init__()
#         self.school = "파이썬 코딩도장"
        
# james = Student()
# print(james.school)
# print(james.hello)

# ########################3

# class Person:
#     def greeting(self):
#         print('안녕하세요.')
 
# class Student(Person):
#     def greeting(self):
#         super().greeting()    # 기반 클래스의 메서드 호출하여 중복을 줄임
#         print('저는 파이썬 코딩 도장 학생입니다.')
 
# james = Student()
# james.greeting()

# ########################3

# class Person:
#     def greeting(self):
#         print("안녕하세요")
        
# class University:
#     def manage_credit(self):
#         print("학점 관리")
        
# class Undergrduate(Person, University):
#     def study(self):
#         print("공부하기")

# james = Undergrduate()
# james.greeting()
# james.manage_credit()
# james.study()

############################

# class A:
#     def greeting(self):
#         print('안녕하세요. A입니다.')
 
# class B(A):
#     def greeting(self):
#         print('안녕하세요. B입니다.')
 
# class C(A):
#     def greeting(self):
#         print('안녕하세요. C입니다.')
 
# class D(B, C):
#     pass
 
# x = D()
# x.greeting()    # 안녕하세요. B입니다.

# D.mro()
# #  [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# int.mro()
# # [<class 'int'>, <class 'object'>]

# #############################
# from abc import *
 
# class StudentBase(metaclass=ABCMeta):
#     @abstractmethod
#     def study(self):
#         pass
 
#     @abstractmethod
#     def go_to_school(self):
#         pass
 
# class Student(StudentBase):
#     def study(self):
#         print('공부하기')
 
#     def go_to_school(self):
#         print('학교가기')
 
# james = Student()
# james.study()
# james.go_to_school()

# # 추상 클래스이기 때문에

###########################3


#quiz
                         
class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new                         
 
x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)


#################################33

class Animal:
    def eat(self):
        print('먹다')
 
class Wing:
    def flap(self):
        print('파닥거리다')

class Bird(Animal,Wing):
    def fly(self):
        print("날다")

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))