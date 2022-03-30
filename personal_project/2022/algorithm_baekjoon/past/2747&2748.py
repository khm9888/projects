# https://www.acmicpc.net/problem/2748

n = int(input())

a_list =[0,1]

for i in range(2,n+1):
    a_list.append(a_list[i-2]+a_list[i-1])
    
print(a_list[n])