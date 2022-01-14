def geo2dec(value):#ezs42
    total=0
    values = list(value)
    for i,v in enumerate(values):
        v=ord(v)
        # print(v)
        if v>=111:
            v-=91
        elif v>=108:
            v-=90
        elif v>=105:
            v-=89
        elif v>=98:
            v-=88
            
        elif v>=79:
            v-=59
        elif v>=76:
            v-=58
        elif v>=73:
            v-=57
        elif v>=66:
            v-=56 
            
        else:
            v-=48
        # print(v)
        calc=v*32**(len(values)-1-i)
        # print(calc)
        total+=calc
    return total

def geo2bin(txt):
    value = bin(geo2dec(txt))
    multi5_length=len(txt)*5
    # print(multi5_length)
    value=str(value)
    # print(len(value))
    if len(value)-multi5_length==1:
        value=value[0]+value[2:]
    elif len(value)-multi5_length==2:
        value=value[2:]
    return value

# print(geo2bin('DRUGGED'))


# print(geo2dec('n'))
# print(ord("B"))
# print(ord("Z"))
# print(ord("N"))
# print(ord("L"))
# print(ord("I"))

# print(ord("b"))
# print(ord("z"))
# print(ord("0"))
# print(ord("9"))
# 98
# 122
# 48
# 57
# print(ord("i"))
# print(ord("o"))
# for i in range(98,123):
#     print(chr(i))