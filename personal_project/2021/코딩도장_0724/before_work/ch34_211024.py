# #ch34 클래스

# class Test_Class:
#     def __init__(self):
#         self.hello ="안녕하세요"
    
#     def greeting(self):
#         print(self.hello)
    
# james = Test_Class()
# james.greeting() 

# class Person:
#     def __init__(self, name, age, address):
#         self.hello =  "안녕하세요."
#         self.name = name
#         self.age = age
#         self.address = address
    
#     def greeting(self):
#         print(f"{self.hello} 저는 {self.name}입니다")
        
# maria = Person("마리아", 20, "서울시 서초구 반포동")
# maria.greeting()

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet  

    def pay(self, amount):
        if amount > self.__wallet:
            print("돈이 모자르네...")
            return
        self.__wallet -= amount
        print(f"이제 {self.__wallet}원 남았네요.")    

maria = Person("마리아", 20, "서울시 서초구 반포동", 10000)
maria.__wallet -= 10000
maria.pay(3000)

### 34장 연습문제 -1

                                         
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    
    def slash(self):
        print("베기")
                                       
 
x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

# 542.4 210.3 38
# 베기

### 34장 연습문제 -2

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power 
        
    def tibbers(self):
        damage = self.ability_power*0.65+400
        print(f"티버: 피해량 {damage}")
        
#34장 완료#        
##########################################
