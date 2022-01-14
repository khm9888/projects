# #unit 4

# #factorial - 4-1

# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f *= i
#     return f

# print(fact(5))

# #matroshoca

# def hello(cnt):
#     if cnt<10:
#         print("hello")
#         cnt+=1
#         hello(cnt)
        
# hello(0)

# #4-2 factorial

# def fact(n):
#     if n>1:
#         r =n *fact(n-1)
#     else:
#         r = 1
#     return r

# print(fact(5))    
        
    
# #unit4- practice

# #Q.4-1
# def recrusive(n):
#     if n==1:
#         return n
#     else:
#         return n+recrusive(n-1)
    
# n=recrusive(10)

# print(n)

# #Q.4-2

# n= [10,20,30,40,34,35,15]
# def findmax(index,maxvalue):
#     print(f"i:{index},maxv:{maxvalue}")
#     if n[index]>maxvalue:
#         maxvalue=n[index]
#     if index != 0:
#         maxvalue= findmax(index-1,maxvalue)
#     return maxvalue

# v=findmax(len(n)-1,n[len(n)-1]) 
# print(v)

# #Q.4-3

# def fibonachi(n):
#     if n == 0: 
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonachi(n-1)+fibonachi(n-2)
    
# n = fibonachi(3)
# print(n)
# n = fibonachi(5)
# print(n)

###########################################################

# # unit5

# def hanoi (n, from_pos, to_pos, aux_pos):
#     if n == 1:
#         print(f"{from_pos}->{to_pos}")
#         return
#     hanoi (n-1, from_pos, aux_pos, to_pos)     
#     print(f"{from_pos}->{to_pos}")
#     hanoi (n-1, aux_pos, to_pos, from_pos) 
    

# print("cnt:1")
# hanoi(1,1,3,2)

# print("cnt:3")
# hanoi(3,1,3,2)


###########################################################

# unit6 - 순차탐색 , sequential search

def sequential_search(alist,v):
    n=len(alist)
    for i in range(0,n):
        if v==alist[i]:
            return i
    return -1

v=[10,20,30,40,0]

print(sequential_search(v,30))
print(sequential_search(v,0))
print(sequential_search(v,15))

#unit6-practice

#Q. 6-1

def sequential_search_2(alist,v):
    n=len(alist)
    answer =[]
    for i in range(0,n):
        if v==alist[i]:
            answer.append(i)
    return answer

#Q. 6-3
std_no = [39,14,67,105]
std_name = ["mike","james","justin","mary"]

def sequential_search(alist,v,std_name):
    n=len(alist)
    for i in range(0,n):
        if v==alist[i]:
            print(std_name[i])
            return
    print("?")
    return

sequential_search(std_no,14,std_name)
sequential_search(std_no,1,std_name)
