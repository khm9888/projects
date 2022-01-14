# #unit 7  - selection sort

# #7-1

# def find_min(alist):
#     leng = len(alist)
#     min_idx = 0
#     for i in range(1,leng):
#         if alist[min_idx]>alist[i]:
#             min_idx=i
#     return min_idx

# def selection_sort(alist):
#     answer = []
#     while alist:
#         i=find_min(alist)
#         answer.append(alist.pop(i))
#     return answer

# v = [3,4,1,5,2]

# print(selection_sort(v))

# #7-2

# def sel_sort(alist):
#     n = len(alist)
#     for i in range(0,n-1):
#         min_idx = i
#         for j in range(i+1,n):
#             if alist[min_idx]>alist[j]:
#                 min_idx=j
#         alist[min_idx],alist[i]=alist[i],alist[min_idx]
#     return alist

# v = [3,4,1,5,2]

# print(sel_sort(v))

# #연습문제 2번
# #->max_index로 변수 이름 바꾸고, 비교기호 바꿈 

# def sel_sort(alist):
#     n = len(alist)
#     for i in range(0,n-1):
#         max_idx = i
#         for j in range(i+1,n):
#             if alist[max_idx]<alist[j]:
#                 max_idx=j
#         alist[max_idx],alist[i]=alist[i],alist[max_idx]
#     return alist

# v = [3,4,1,5,2]

# print(sel_sort(v))

# #unit 8 - Insertion sort
# #8-1
# def find_ins_idx(r,v):#r-list, v-value
#     for i in range(len(r)):
#         if v<r[i]:
#             return i
#     return len(r)

# def ins_sort(a):
#     result=[]
#     while a:
#         value=a.pop(0)
#         ins_idx = find_ins_idx(result,value)
#         result.insert(ins_idx,value)
#     return result            

# d = [3,2,1,4,6]
# print(ins_sort(d))

# #8-2
# d = [2,4,5,1,3]

# def ins_sort(a):
#     n = len(a)
#     for i in range(1,n):# i = 3
#         key = a[i]#1
#         j =i-1#2
#         while j>=0 and a[j]>key:#5>1
#             a[j+1]=a[j] #a[3]=5,a[2]=4,a[1]=2
#             j-=1
#         a[j+1]=key#a[0]=1
#         print(f"a:{a}")
#     return a

# ins_sort(d)

# #연습문제 8-2
# d = [2,4,5,1,3]

# def ins_sort(a):
#     n = len(a)
#     for i in range(1,n):# i = 3
#         key = a[i]#1
#         j =i-1#2
#         while j>=0 and a[j]<key:#5>1
#             a[j+1]=a[j] #a[3]=5,a[2]=4,a[1]=2
#             j-=1
#         a[j+1]=key#a[0]=1
#         print(f"a:{a}")
#     return a

# ins_sort(d)

#unit 9 - Merge sort

# #9-1

# def merge_sort(alist):
#     n=len(alist)#10
#     if n<=1:
#         return alist
#     mid = n//2 #5
#     print(f"alist:{alist}")
#     print(f"mid:{mid}")
#     g1 = merge_sort(alist[:mid])
#     g2 = merge_sort(alist[mid:])
#     print(g1)
#     print(g2)
#     result = []
#     while g1 and g2:
#         if g1[0] < g2[0]:
#             result.append(g1.pop(0))
#         else:
#             result.append(g2.pop(0))
#     while g1:
#             result.append(g1.pop(0))
#     while g2:
#             result.append(g2.pop(0))
#     return result

# d = [6,8,3,9,10,1,2,4,7,5]

# print(merge_sort(d))

#9-2

def merge_sort(alist):
    n = len(alist)
    if n<=1:
        return alist
    mid = n//2
    g1 = alist[:mid]
    g2 = alist[mid:]
    print(f"g1:{g1}")
    print(f"g2:{g2}")
    merge_sort(g1)
    merge_sort(g2)
    i1=0
    i2=0
    ia=0
    while i1<len(g1) and i2<len(g2):
        if g1[i1]<g2[i2]:
            alist[ia]=g1[i1]
            i1+=1
        else:
            alist[ia]=g2[i2]
            i2+=1
        ia+=1
    while i1<len(g1):
        alist[ia]=g1[i1]
        i1+=1
        ia+=1
    while i2<len(g2):
        alist[ia]=g2[i2]
        i2+=1
        ia+=1
    return alist   
d = [6,8,3,9,10,1,2,4,7,5]

print(merge_sort(d))

#9장 연습문제 9-1


def merge_sort(alist):
    n = len(alist)
    if n<=1:
        return alist
    mid = n//2
    g1 = alist[:mid]
    g2 = alist[mid:]
    print(f"g1:{g1}")
    print(f"g2:{g2}")
    merge_sort(g1)
    merge_sort(g2)
    i1=0
    i2=0
    ia=0
    while i1<len(g1) and i2<len(g2):
        if g1[i1]>g2[i2]:
            alist[ia]=g1[i1]
            i1+=1
        else:
            alist[ia]=g2[i2]
            i2+=1
        ia+=1
    while i1<len(g1):
        alist[ia]=g1[i1]
        i1+=1
        ia+=1
    while i2<len(g2):
        alist[ia]=g2[i2]
        i2+=1
        ia+=1
    return alist   

d = [6,8,3,9,10,1,2,4,7,5]

print(merge_sort(d))
d = [6,8,3,9,10,1,2,4,7,5]
