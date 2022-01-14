#unit10 - binary search

# def binary_search(alist,v):
    
#     start = 0
#     end = len(alist) -1
    
#     while start <= end:
#         mid = (start+end)//2
#         if v == alist[mid]:
#             return mid
#         elif v>alist[mid]:
#             start = mid+1
#         else:
#             end = mid-1
#     return -1

# d= [1,4,9,16,25,36,49,64,81]
# print(binary_search(d,16))
# print(d[binary_search(d,16)])
# print(binary_search(d,17))

# #10장 연습문제 10-1

# def binary_search_sub(alist,v,start,end):

#     if start>end:
#         return -1
    
#     mid = (start+end)//2
#     if v == alist[mid]:
#         return mid
#     elif v>alist[mid]:
#         start = mid+1
#         return binary_search_sub(alist,v,start,end)
#     else:
#         end = mid-1
#         return binary_search_sub(alist,v,start,end)
#     return -1

# def binary_search(alist,v):
#     return binary_search_sub(alist,v,0,len(alist)-1)

# d= [1,4,9,16,25,36,49,64,81]
# print(binary_search(d,16))
# print(d[binary_search(d,16)])
# print(binary_search(d,17))


#unit11 - palindrome /  queue & stack

# qu = list()#qu
# x=1
# qu.append(x)#enqueue
# x=qu.pop(0)#dequeue

# st=list()
# st.append(x)#push
# x=st.pop()#pop

# #11-1
# def palindrome(sentence):
#     qu = list(sentence)
#     st = list(sentence)
#     r_qu=list()
#     r_st=list()
#     while qu:
#         r_qu.append(qu.pop(0))
        
#     while st:
#         r_st.append(st.pop())
        
#     for i in range(len(sentence)):
#         print(r_qu[i])
#         print(r_st[i])
#         if r_qu[i] != r_st[i]:
#             return False
#     return True

# print(palindrome("wow"))
# print(palindrome("wvow"))
        
# #11장 연습문제 11-1

# def palindrome(sentence):
#     n = len(sentence)//2
#     for i in range(n):
#         if sentence[i] != sentence[-i]:
#             return False
#     return True    

# print(palindrome("wow"))
# print(palindrome("wvow"))
        
#unit12 - dictionary

#12-1 

def samename(alist):
    count_name_dict=dict()
    result=set()
    for a in alist:
        if a not in count_name_dict:
            count_name_dict[a] = 1
        else:
            count_name_dict[a] += 1
    
    for k,v in count_name_dict.items():
        if v>=2:
            result.add(k)
    return result

al = ["m","as","nm","m"]

print(samename(al))
            
            
def find_stu(number,stu_dict):

    if number not in stu_dict:
        return "?"
    else:
        return stu_dict[number]

stu_dict={1:"kim",2:"park",3:"lee"}
print(find_stu(1,stu_dict))
print(find_stu(4,stu_dict))
        
        
