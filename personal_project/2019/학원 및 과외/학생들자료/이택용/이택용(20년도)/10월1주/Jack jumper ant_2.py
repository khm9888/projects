x = input()[::-1]
# x = "CBA"[::-1]
y = input()
# y = "DEFG"


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

    print_x=[]
    print_y=[]
    # print(f"---------------------{c}---------------------")
    if c!=0:
        check=0
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
                    break
            # print(m_list)
    print_list=[]
    for i,m in enumerate(m_list):
        if i==len(m_list)-1:
            print(m_list[i][0])
        else:        
            print(m_list[i][0],end="")