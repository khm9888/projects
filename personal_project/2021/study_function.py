# a_list = list(range(1,20,2))

# def check(a_list):
#     total = 0
#     for i in a_list:
#         print(i)
#         total += i
#     return total
    
# print(check(a_list))


class Person:
    def __init__(self,age_1,name_1):
        self.age=age_1
        self.name=name_1
    
    def next_year_age(self):
        return self.age+1
    
con = Person(10,"김해민")
print(con.age)
print(con.name)
print(con.next_year_age())