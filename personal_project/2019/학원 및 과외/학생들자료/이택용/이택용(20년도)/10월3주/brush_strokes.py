apartments = (1, 4, 3, 2, 3, 1)

def floors(apartments):
    answer = []
    max_floor = max(apartments)#4
    for heigth in range(1,max_floor+1):#1~4
        floor=[]
        for order in range(len(apartments)):
            if apartments[order] >= heigth:
                floor.append(True)
            else:
                floor.append(False)
        answer.insert(0,floor)
    return answer
    

def front_view(apartments, width=3, distance=1, apartment='#', air=" "):
    values=floors(apartments)
    top_bottom_floors=[]
    answer = ""
    for order in range(len(values)):
        top_bottom_floors.append(values[order])
    for o_i,order in enumerate(top_bottom_floors):
        for i,v in enumerate(order):
            if not v:#False
                answer+=air*width
            else:
                answer+=apartment*width
            if len(order)-1!=i:
                answer+=air*distance
        if len(top_bottom_floors)-1!=o_i:
            answer+="\n"

    return answer      

def brush_strokes(apartments):
    values=floors(apartments)
    total=0
    for v in values:
        cnt=0
        for i,bool_v in enumerate(v[:-1]):
            if not bool_v:
                pass
            elif bool_v and (v[i+1]==False or len(v[:-1])-1==i):
                cnt+=1                
        if v[-1] and not v[-2]:
            cnt+=1
        total+=cnt
    return total

