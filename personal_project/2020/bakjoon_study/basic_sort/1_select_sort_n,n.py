#select_sort

def select_sort(values):
    n=len(values)
    for i in range(n):
        for j in range(i,n):
            if values[i]>values[j]:
                values[i],values[j]=values[j],values[i]
                