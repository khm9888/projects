#merge_sort

def gapInsertionSort(values, start, gap):
    for target in range(start+gap, len(values), gap):
        val = values[target]
        i = target
        while i > start:
            if values[i-gap] > val:
                values[i] = values[i-gap]
            else:
                break
            i -= gap
        values[i] = val

def shellSort(values):
    gap = len(values) // 2
    while gap > 0:
        for start in range(gap):
            gapInsertionSort(values, start, gap)
        gap = gap // 2
    return values 

        
d=[2,4,5,1,3]
d=shellSort(d)
print(d)