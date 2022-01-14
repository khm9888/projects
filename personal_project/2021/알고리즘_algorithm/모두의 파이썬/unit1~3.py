# #0-1

# answer = int(input("값을 입력하시오"))

# def abs(answer):
#     if answer<0:
#         answer_1 = -answer

#     return answer_1

# answer_1=abs(answer)
        
# print(answer,"의 절대값은",answer_1)
    

# #unit1

# def sum_n(start_num=1,end_num=1):
    
#     total = 0
#     for num in range(start_num,end_num+1):
#             total+=num
#     return total

# print(sum_n(1,10))


# def sum_n_2(start_num=1,end_num=1):

#     total = end_num*(end_num+1)//2
    
#     return total

# print(sum_n_2(1,10))


# #1-1

# def sol(n):
#     total=0
#     for num in range(n+1):
#         total+=num**2
#     return total

# print(sol(10))

# #1-2

# #O(n)

# #1-3

# #n*n(n+1)(2n+1)//6, O(n)

# #2-1

# def max_find(a_list):
#     # max_val = float('inf')
#     # print(max_val)
#     max_value = a_list[0]
    
#     for i in range(1,len(a_list)+1):
#         if i>max_value:
#             max_value=i
#     return max_value

# print(max_find([1,2,3,4,5]))

# #2-2

# a_list = [30,490,4,12,599,40]

# def find_max(a_list):
#     max_v=a_list[0]
#     loc = 0
#     for i,n in enumerate(a_list):
#         if a_list[i]>a_list[loc]:
#             loc=i
#     return loc

# print(find_max(a_list))

# def find_min(a_list):
#     min_v=a_list[0]
#     loc = 0
#     for i,n in enumerate(a_list):
#         if a_list[i]<a_list[loc]:
#             loc=i
#     return loc
   
# print(find_min(a_list))

# #unit3

# s = set()

# s.add(1)
# s.add(2)
# s.add(2)

# print(s)

# print(len(s))

# print({1,2}=={2,1})

# #3-1

a_list = ["a","b","c","a","b"]
values = dict() #hash


for v in a_list:#n
    if v not in values: #nlogn #탐색방법에 따라 달라짐.
        values[v]=1
    else:
        values[v]+=1



def find_same_name(a): #[a,b,c] a,b  a,c  b,c #a,b,c,a,b 
    n = len(a)
    result=set()
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]==a[j]:
                result.add(a[i])
    return result

# print(find_same_name([1,2,3,4,12,1,2]))

# #연습문제 3-1

# def match_two(a):
#     result = set()
#     for i in range(len(a)-1):
#         for j in range(i,len(a)):
#             if i==j:
#                 pass
#             else:
#                 result.add(f"{a[i]} - {a[j]}")
#     return result            
# print(match_two([1,2,3]))
