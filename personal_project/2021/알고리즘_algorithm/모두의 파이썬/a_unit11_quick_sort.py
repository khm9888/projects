#unit 11_quick_sort

# #p11-1
# def quick_sort(alist):
#     n = len(alist)
#     if n<=1:
#         return alist
    
#     center = alist[-1]
    
    
#     a1 = []
#     a2 = []
#     for i in range(n-1):
#         if alist[i]< center:
#             a1.append(alist[i])
#         else:
#             a2.append(alist[i])
#     return quick_sort(a1)+[center]+quick_sort(a2)

# d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

# print(quick_sort(d))

#p11-2

def quick_sort_sub(a, start, end):
    # d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    
    # 종료 조건: 정렬 대상이 한 개 이하이면 정렬할 필요가 없음

    if end - start <= 0:
        return

    # 기준 값을 정하고 기준 값에 맞춰 리스트 안에서 각 자료의 위치를 맞춤
    # [기준 값보다 작은 값들, 기준 값, 기준 값보다 큰 값들]
    pivot = a[end]   # 편의상 리스트의 마지막 값을 기준 값으로 정함
    i = start # i  = 0 
    for j in range(start, end):#0~8
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            print(a)
            i += 1
    a[i], a[end] = a[end], a[i]
    print(a)
    print()
    # 재귀 호출 부분

    quick_sort_sub(a, start, i - 1) # 기준 값보다 작은 그룹을 재귀 호출로 다시 정렬
    quick_sort_sub(a, i + 1, end)  # 기준 값보다 큰 그룹을 재귀 호출로 다시 정렬

# 리스트 전체(0 ~ len(a) -1)를 대상으로 재귀 호출 함수 호출

def quick_sort(a):

    quick_sort_sub(a, 0, len(a) - 1)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

quick_sort(d)

print(d)

#연습문제 11장

#bubble-sort 알고리즘

def bubble_sort(alist):
    n = len(alist)
    if n<=1:
        return alist
    for i in range(n-1):
        for j in range(0,n-1-i):
            print(f"j:{j}")
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                print(alist)
    return alist

print(bubble_sort([5,4,3,2,1]))        
        
