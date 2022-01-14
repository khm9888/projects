

def list_representation(values,division,count_n=None):
    answer = []
    if count_n==None:
        count_n=len(values)//division
    for i in range(division):
        answer.append(list(map(int,values[i*count_n:(1+i)*count_n])))
    return answer


def string_representation(answer):
    values=""
    for a in answer:
        for b in a:
            values+=str(b)
    return (values,len(answer),len(a))

def move(number,locate,answer):
    for loc in locate:
        answer[loc[0]][loc[1]]+=number
    return answer

def is_solved(answer):
    number=answer[0][0]
    for a in answer:
        for b in a:
            if b!=number:
                return False
            
    return True


# def group(loc,answer,group=set()):
#     values = [(i,j) for i,a in enumerate(answer) for j,b in enumerate(a)]
#     print(loc)
#     for i,a in enumerate(answer): 
#         for j,b in enumerate(a):
#             group=set()
#             # if values in
#             if (i,j) in values:
#                 group.add((i,j))
#                 values.remove((i,j))
#             print(number)
#             if i+1<len(a) and (i+1,j) in values:
#                 if answer[i][j] ==answer[i+1][j]:
#                     group.add((i+1,j))
#                     values.remove((i+1,j))
#             if j+1<len(answer) and (i,j+1) in values:
#                 if answer[i][j] ==answer[i][j+1]
#                     group.add((i,j+1))
#                     values.remove((i,j+1))
#     return values

def group(loc,answer):
    # values = [(i,j) for i,a in enumerate(answer) for j,b in enumerate(a)]
    # print(loc)
    values=list()
    for i,a in enumerate(answer): 
        for j,b in enumerate(a):
            if i==0 and j==0:
                v=set()
                v.add((i,j))
                values.append(v)
                continue
            if i-1>=0 and answer[i][j]==answer[i-1][j]:
                    for idx,value in enumerate(values):
                        print("value")
                        print(value)
                        if (i,j) in value:
                            print(1)
                            value.add((i-1,j))
                            # values[idx].append((i-1,j))
                            continue
            
            elif j-1>=0 and answer[i][j]==answer[i][j-1]:
                    for idx,value in enumerate(values):
                        if (i,j) in value:
                            print(2)
                            value.add((i,j-1))
                            # values[idx].append((i,j-1))
                            continue
            else:
                v=set()
                v.add((i,j))
                values.append(v)                          
        print(values)
        
    return values

v= list_representation('1221133113322222', 4)

print(v)
# v=grid
# [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]

# ('1221133113322222', 4, 4)


# v=move(-1, {(1, 2), (1, 1), (2, 1), (2, 2)}, v)
# [[1, 2, 2, 1], [1, 2, 2, 1], [1, 2, 2, 2], [2, 2, 2, 2]]
# v=grid
# [[1, 2, 2, 1], [1, 2, 2, 1], [1, 2, 2, 2], [2, 2, 2, 2]]
# v=move(+1, {(0, 3), (1, 3)}, grid)
# [[1, 2, 2, 2], [1, 2, 2, 2], [1, 2, 2, 2], [2, 2, 2, 2]]
# v=grid
# [[1, 2, 2, 2], [1, 2, 2, 2], [1, 2, 2, 2], [2, 2, 2, 2]]
# v=move(+1, {(2, 0), (1, 0), (0, 0)}, grid)
# [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]

# v=grid
# [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
# v=is_solved(v)
# True

# v=grid
# [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
v=group((2, 1), v)
# {(1, 2), (1, 1), (2, 1), (2, 2)}
# v=group((0, 3), grid)
# {(0, 3), (1, 3)}
# v=group((1, 0), grid)
# {(2, 0), (1, 0), (0, 0)}

# v=grid = [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
# v=is_solution([(1, 1, False), (3, 2, False)], grid)
# True
# v=grid
# [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]
# v=is_solution([(1, 3, True), (3, 2, False), (0, 1, True)], grid)
# False
# v=grid
# [[1, 2, 2, 1], [1, 3, 3, 1], [1, 3, 3, 2], [2, 2, 2, 2]]

print(v)