def numbers(values):
    v_set=set()
    for value in values:
        for v in value:    
            v_set.add(v)
    
    return v_set

def sums(values):
    v_set=set()
    for value in values:
        row_value=0
        for v in value:
            row_value+=v
        v_set.add(row_value)
        
    values_length = len(values)
    for i in range(values_length):
        column_value=0
        for j in range(values_length):
            column_value+=values[j][i]
        v_set.add(column_value)
    
    diagonal_value=0
    for i in range(values_length):
        diagonal_value+=values[i][i]
    v_set.add(diagonal_value)

    diagonal_value_2=0
    for i in range(values_length):
        diagonal_value_2+=values[i][values_length-1-i]
    v_set.add(diagonal_value_2)
    
    return v_set

def ismagic(values):
    check = len(numbers(values))==len(values)**2
    
    if len(sums(values))==1 and check:
        return True
    return False

def ishetero(values):
    check = len(numbers(values))==len(values)**2
    
    length=len(values)
    if len(sums(values))==length*2+2 and check:  
        return True
    return False


def isantimagic(values):
    
    check = len(numbers(values))==len(values)**2
    
    v = sorted(list(sums(values)))
    check2 = list(range(min(v),max(v)+1)) 
    
    if ismagic(values):
        return False
    elif v==check2 and check:
        return True
    else:
        return False
