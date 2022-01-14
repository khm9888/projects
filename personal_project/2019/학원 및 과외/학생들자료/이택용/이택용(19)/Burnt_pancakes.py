

def flip(values, burnt=False):
    values_reverse=list(values)[::-1]
    if burnt:
        for i in range(len(values_reverse)):
            values_reverse[i]=-1*values_reverse[i]  
    return tuple(values_reverse)
        

         
def flip_top(values,num,burnt=False):
    values_reverse=list(values)[:num][::-1]
    values_reverse_copy=values_reverse.copy()
    values_reverse.extend(values[num:])
    # print(values_reverse)
    if burnt:
        for i in range(len(values_reverse_copy)):
            values_reverse[i]=-1*values_reverse[i]  
    return tuple(values_reverse)
    
def find_largest(values,num):
    values_abs = list(map(abs,values))
    values_abs_apart = values_abs[:num] 
    return values_abs.index(max(values_abs_apart))+1 

def mul(a):
    return -a

def sorting_step(values,num,burnt=False):
    large_num_index=find_largest(values,num)#3
    values=list(values)
    if burnt:
        if values[large_num_index-1]>=0:
            values[large_num_index:num]=list(map(mul,values[large_num_index:num]))
        else: 
            values[large_num_index-1:num]=list(map(mul,values[large_num_index-1:num]))
    answer = []
    
    # if burnt:
    #     for i,num1 in enumerate(values[:num]):
    #         # print(i,num1)
    #         values[i]=-1*num1
        
    answer.extend(values[large_num_index:num][::-1]) 
    answer.extend(values[:large_num_index])
    answer.extend(values[num:])

    return tuple(answer)

def sorting_steps(values):
    answer =list()
    answer.append(values)
    
    for i in range(len(values),0,-1):
        values=sorting_step(values,i)
        answer.append(values)
    return tuple(answer)
v=sorting_steps((1, 8, 5, 7, 2, 9, 4, 6, 3))
w=[(1, 8, 5, 7, 2, 9, 4, 6, 3), (3, 6, 4, 1, 8, 5, 7, 2, 9), (2, 7, 5, 3, 6, 4, 1, 8, 9), (1, 4, 6, 3, 5, 2, 7, 8, 9), (2, 5, 3, 1, 4, 6, 7, 8, 9), (4, 1, 3, 2, 5, 6, 7, 8, 9), (2, 3, 1, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 5, 6, 7, 8, 9)]
# v=sorting_steps((1, -8, -5, 7, 2, 9, -4, -6, 3), burnt=True)
w= [(1, -8, -5, 7, 2, 9, -4, -6, 3), (-3, 6, 4, 1, -8, -5, 7, 2, 9), (-2, -7, 5, -3, 6, 4, 1, 8, 9), (-1, -4, -6, 3, -5, -2, 7, 8, 9), (2, 5, -3, -1, -4, 6, 7, 8, 9), (4, 1, 3, 2, 5, 6, 7, 8, 9), (-2, -3, -1, 4, 5, 6, 7, 8, 9), (1, -2, 3, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 5, 6, 7, 8, 9)]


# print(len(w))
print(v)