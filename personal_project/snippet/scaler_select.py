t_num = int(input("sclaer 번호는 1.StandardScaler, 2.MinMaxScaler, 3.RobustScaler : "))

# t_num=1

if t_num==1:
    scaler = StandardScaler()
elif t_num==2:
    scaler = MinMaxScaler()
elif t_num==3:
    scaler = RobustScaler()