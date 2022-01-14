x = input()[::-1]
# x = "CBA"[::-1]
y = input()
# y = "DEFG"

# x_list=

# print(x)
# print(y)
# list_x = list(x)
# list_y = list(y)
# merge_list=list_x+list_y
len_x = len(x)
len_y = len(y)
min_value = min(len_x,len_y)
cnt = len_x+len_y

x_list=[]
y_list=[]

for x_i in x:
    x_list.append([x_i,-1])
for y_i in y:
    y_list.append([y_i,1])
# print(x_list)
# print(y_list)
m_list=x_list+y_list
for c in range(cnt):#0~6 #1,2,3,4,5,6
    # if c!=0 and len(list_x)!=0:
    #     pop_x=list_x.pop(-1)
    # if c!=0 and len(list_y)!=0:        
    #     pop_y=list_y.pop(0)
    # if c<=cnt//2:
    #     # print(f"len_x:{len_x},len_x+1:{len_x+1}")
    #     print(f"c:{c}")
    # merge_list[len_x-1],merge_list[len_x-1+c]=merge_list[len_x-1+c],merge_list[len_x-1]
    print_x=[]
    print_y=[]
    # print(f"---------------------{c}---------------------")
    if c!=0:
        check=0
        
        if len_x<=len_y:#
            if c>min_value:
                c=min_value
            # print(f"c:{c}")
            for d in range(cnt):
                # print(f"d:{d}")
                if m_list[d][1]==1 and m_list[d-1][1]!=1 and d!=0:
                    # print(True)
                    m_list[d],m_list[d-1]=m_list[d-1],m_list[d]
                    check+=1
                    if check>=c:
                        # print("T")
                        break
                # print(m_list)
        else:
            if c>cnt//2:
                c=cnt-c
            # print(f"c:{c}")
            for d in range(-1,-cnt,-1):
                # print(f"d:{d}")
                if m_list[d][1]==-1 and m_list[d+1][1]!=1 and d!=-1:
                    # print(True)
                    m_list[d],m_list[d+1]=m_list[d+1],m_list[d]
                    check+=1
                    if check>=c:
                        # print("T")
                        break
    print_list=[]
    for i,m in enumerate(m_list):
        if i==len(m_list)-1:
            print(m_list[i][0])
        else:        
            print(m_list[i][0],end="")
        
            # if m_list[0][] ==
            
    
    

# reverse_x=x[::-1]

# start = reverse_x+y
# print(start)
# end = y+reverse_x
# sentence = start[:]
# print(sentence)



#abc 012
#defg 3456


# cnt=1
# while sentence==end:
#     if cnt
#     cnt+=1
#     if cnt>10:
#         break
#     print(sentence)
