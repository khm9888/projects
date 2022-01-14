# # x= input()
# print("고려대학교")
# print("비와이")

# a,b,c = map(int,input().split())

# print(20080302)

# a = int(input())
# print(a%20000303)

#a 🍰 b = (a.z + b.x, a.y × b.y, a.x + b.z)

# 15 16 17
# 19 32 90

# ax,ay,az = map(int,input().split())
# cx,cy,cz = map(int,input().split())
# bx,by,bz = [cx-az,cy//ay,cz-ax]
# print(bx,by,bz)
# a,b,c,d = map(int,input().split())


# print(c*d*((a-1)//b))

# A,B = map(int,input().split())
# print((A+B)*(A-B))
# print("파이팅!!")

# print(2020)
# print("06")
# print(27)

# a = int(input())
# print(a*(a-1))
# if a%5>0:
#     print(a//5+1)
# else:
# #     print(a//5)
# people=[]
# a = int(input())
# for  i in range(a):
#     values=input().split()
#     people.append([int(values[0]),values[1],i])

# for i in range(len(people)-1):
#     for j in range(i+1,len(people)):
#         if people[i][0]>people[j][0] or (people[i][0]==people[j][0] and people[i][2]>people[j][2]):
#             people[i],people[j]=people[j],people[i]

# for i in range(len(people)):
#     print(people[i][0],people[i][1])
    
# input()

# n=int(input())
# for _ in range(n):
#     a,b=map(int,input().split())
#     print(a+b)
    
# import cv2

# # print(cv2.path)
# import sys
# x=sys.stdin()
# x=list(x)
# print(x)


# words=[chr(i) for i in range(65,70)]
# stuff=[[w.upper(),w.lower(),len(w)] for w in words] 
# print(stuff)

# def generator():
#     n=1
#     while True:
#         if n%2==0:
#             yield n
#             print(1)
#         n+1
#         # if n>20:
#         #     break
# # print(list(generator()))

# for i in generator():
#     print(i)
#     if i>=10:
#         break


# h,c=map(int, input().split())
# # h,c=max(h,c),min(h,c)
# if c==0 or h<c:
#     print(-1)
# else:
#     print((h+c)//2,(h+c)//2-h)

''' 
minute,b=map(int,input().split())#14 20
sec_o=int(input())+b#50 +20

sec= sec_o%60 #10
minute=minute+sec_o//60
minute %=24

print(minute, sec)
 '''

# p, m = map(int, input().split()) # 3 1 a=p-m # 2
# a = (p + m)/2
# b = (p - m)/2
# print(int(a), int(b)) if a % 1 == 0 and a >=0 and b >=0 else print(-1)

# x=input()
# print(ord(x))

# x = int(input())

# print(chr(x+44032-1))

# n = int(input())
# if n==0:
#     print("YONSEI")
# else:
#     print("Leading the Way to the Future")

# values = [[0] for i in range(10)]

# level = list(map(int,input().split()))

# print(abs(level[3]+level[0]-level[2]-level[1]))


# standard = int(input())
# numbers = list(map(int,input().split()))
# total = 0
# for i in numbers:
#     if i==standard:
#         total+=1
# print(total)

# t=0
# values = [int(input())for _ in range(5)]
# if values[0]<0:
#     t+=(abs(values[0])*values[2]+values[3])#10*5+10
#     values[0]=0
#     # print(t)
# t+=(values[1]-values[0])*values[4]
# print(t)


#13136

# vals = list(map(int,input().split()))
# if vals[0]%vals[2]!=0:
#     a=vals[0]//vals[2]+1
# else:
#     a=vals[0]//vals[2]
# if vals[1]%vals[2]!=0:
#     b=vals[1]//vals[2]+1
# else:
#     b=vals[1]//vals[2]

# print(a*b)

# n = int(input())

# if n%8==1:
#     print(1)
# elif n%8==2 or n%8==0:
#     print(2)
# elif n%8==3 or n%8==7:
#     print(3)
# elif n%8==4 or n%8==6:
#     print(4)
# else:
#     print(5)


t = int(input())
v = [int(input()) for i in range(t)]
for value in v:
    cnt = 1
    for i in range(2,value):
        while value%i==0:
            cnt+=1
            value//=i
            if value<i:
                break
        if value<i:
            break
    print(cnt)

