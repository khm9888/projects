#table *25 = > value
#double 하면, 

table = int(input())
start_value = int(input())
double_round = int(input())
result = input()
total_value=0

for t in range(1,table+1):
    round_value=t*start_value
    if result=="lost" and t==table:
        total_value/=2
        total_value=int(total_value)
        print(f"table #{t}: €{total_value}")
    elif t%double_round==0:
        total_value=(total_value+round_value)*2
        print(f"table #{t} (x2): €{total_value}")        
    else:
        total_value+=round_value
        print(f"table #{t}: €{total_value}")