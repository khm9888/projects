
#x,y,z는 동갑이 아니다
#x+y+z는 9를 넘지 않는다.
#x*y*z는 12를 넘지 않는다.
##제일 나이 많은 아이도 6살 이하다

x,y,z = 0,0,0
chk=False
for x in range(1,7):
    for y in range(1,7):
        for z in range(1,7):
            if x !=y and y!=z and z!=x:
                if x*y*z == x+y+z+3:
                    print(x,y,z)
                    chk=True
                    break
        if chk:
            break
    if chk:
        break

