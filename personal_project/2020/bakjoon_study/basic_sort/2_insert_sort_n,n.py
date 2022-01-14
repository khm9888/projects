#insert_sort

def insert_sort(values):
    n=len(values)
    for i in range(1,n):
        key = values[i]#작은 값이라고 기준 잡은 값
        j=i-1#그 이전 값
        while j>=0 and values[j]>key:#기준값 전이 순서상 0번 이상이고, 기준값 보다 크다면
            values[j+1] = values[j] #오른쪽으로 이동
            j-=1 #그 이전 값과 비교하기 위해 감사
            # print(values)
        values[j+1]=key
d=[2,4,5,1,3]
insert_sort(d)
print(d)