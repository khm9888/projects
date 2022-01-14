

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
        x=loc[0]
        y=loc[1]
        answer[x][y]+=number
    return answer


def is_solved(answer):
    number=answer[0][0]
    for a in answer:
        for b in a:
            if b!=number:
                return False
    return True

def check(loc,answer,values=set()):
    x=loc[0]
    y=loc[1]
    if x-1>=0 and answer[x-1][y]==answer[x][y] and (x-1,y) not in values:
        values.add((x-1,y))
        values=check((x-1,y),answer,values)
    if y-1>=0 and answer[x][y-1]==answer[x][y] and (x,y-1) not in values:
        values.add((x,y-1))
        values=check((x,y-1),answer,values)
    if x+1<len(answer) and answer[x+1][y]==answer[x][y] and (x+1,y) not in values:
        values.add((x+1,y))
        values=check((x+1,y),answer,values)
    if y+1<len(answer[0]) and answer[x][y+1]==answer[x][y] and (x,y+1) not in values:
        values.add((x,y+1))
        values=check((x,y+1),answer,values)
    return values

def group(loc,answer):

    x=loc[0]
    y=loc[1]
    values=set()
    values.add(loc)
    number = answer[x][y]
    return check(loc,answer,values)

def is_solution(locations,answer):

    answer_1 = list_representation(string_representation(answer)[0],string_representation(answer)[1],string_representation(answer)[2])

    for loc in locations:
        x=loc[0]
        y=loc[1]
        dicision=loc[2]
        if dicision:
            move(1,group((x,y),answer),answer)
        else:
            move(-1,group((x,y),answer),answer)

    if is_solved(answer):

        for i,a in enumerate(answer):
            for j,b in enumerate(a):
                answer[i][j]=answer_1[i][j] 
        return True
    for i,a in enumerate(answer):
        for j,b in enumerate(a):
            answer[i][j]=answer_1[i][j] 

    return False
            

