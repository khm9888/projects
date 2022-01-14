class Collection():
    def __init__(self,values):
        v = list()
        self.a_set=set()
        for v in values:
            if type(v)==tuple:
                v=list(v)
            if type(v)==list:
                # print(list(range(v[0],v[1]+1)))
                for i in (range(v[0],v[1]+1)):
                    self.a_set.add(i)
            else:
                self.a_set.add(v)
        self._data_len=len(self.a_set)
        
        # print(self.a_set)
        
    def numbers(self):
        return self.a_set
    def __len__(self):
       return self._data_len
    
    def normalform(self):
        a_list=list(self.a_set)
        a_list.sort()
        # if not a_list[0]:
        #     return []
        
        try:
            start=a_list[0]
        except:
            return list()
        
        # print("s",start)
        end=a_list[-1]
        # print("e",end)
        compare_list = list(range(start,end+1))
        # print(compare_list)
        values = []
        b_list = []
        for i in compare_list:
            if i in a_list:
                if len(b_list)==0:
                    b_list.append(i)                    
                elif len(b_list)==1:
                    b_list.append(i)                    
                elif len(b_list)==2:
                    b_list[1]=i
            elif not i in a_list:
                if len(b_list)>1:
                    values.append(b_list)
                    b_list=[]
                elif len(b_list)==1:
                    values.append(b_list[0])
                    b_list=[]
        if b_list:
            if len(b_list)==1:
                values.append(b_list[0])
            else:
                values.append(b_list)
                
        return values        
    def __str__(self):
        # return f"1{a_list}"
        return f"{self.normalform()}"
    def __repr__(self):
        # return f"1{a_list}"
        return f"Collection({self.normalform()})"

    # def __add__(self, other):
    #     return Collection(self.a_set+other.a_set)  
    
    def __sub__(self, other):
        # print(self.a_set)
        # print(other.a_set)
        return Collection(self.a_set-other.a_set)     
    
    def __add__(self, other):
        return Collection(self.a_set+other.a_set) 
        
    def __or__(self, other):
        return Collection(self.a_set|other.a_set)
         
    def __and__(self, other):
        return Collection(self.a_set&other.a_set)     
    
    def __xor__(self, other):
        return Collection(self.a_set^other.a_set)     
         
         
    def __lt__(self, other):
        return (self.a_set<other.a_set)     

    def __le__(self, other):
        return (self.a_set<=other.a_set)     

    def __eq__(self, other):
        return (self.a_set==other.a_set)     

    def __ne__(self, other):
        return (self.a_set!=other.a_set)     

    def __ge__(self, other):
        return (self.a_set>=other.a_set)     

    def __gt__(self, other):
        return (self.a_set>other.a_set)     


A = Collection([33, [27, 30], 32, 25, [20, 24], 31, 19])
print(A)
# v= A.numbers()
# {19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33}
# v= len(A)
# # 14
# v= A.normalform()
# # [[19, 25], [27, 33]]
# print(A)
# [[19, 25], [27, 33]]
# v= A
# Collection([[19, 25], [27, 33]])

B = Collection([22, 26, 30])
v= A - B
# Collection([[19, 21], [23, 25], [27, 29], [31, 33]])
# v= B - A
# Collection([26])
# v= A | B
# Collection([[19, 33]])
# v= A & B
# Collection([22, 30])
# v= A ^ B
# Collection([[19, 21], [23, 29], [31, 33]])


E = Collection([(3, 4), [2, 3], 4, (7, 12)])
v=E.normalform()
F = Collection([(15, 20)])
v=F.normalform()

# v=E & F

print(v)

