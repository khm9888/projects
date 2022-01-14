'''
다음 사양에 따라 지정된 폭, 높이 및 깊이의 입체형을 비스듬히 그려 넣으십시오.

정육면체
전면은 파운드 기호(#), 측면은 플러스 기호(+), 상단면은 콜론(:)을 사용하여 그려야 한다. 전면과 측면은 슬래시(/)를 사용하여 서로 분리해야 한다. 출력 라인 중 어느 것도 후행 공백을 가질 수 없다.

입력
각각 정수 숫자를 포함하는 세 개의 입력 라인이 있다. 이 숫자들은 각각 너비, 높이, 그리고 입체파의 깊이를 나타낸다.

출력
위의 사양에 따라 너비, 높이, 깊이가 있는 입체체를 그리십시오.
'''

#입력 3개 받음, width, heigth, depth

width = int(input())
height = int(input())
depth = int(input())#3
for d in range(depth,0,-1):
    if depth-d>=height:
        print(" "*d+":"*(width-1)+"/"+"+"*(height-1))
    else:
        print(" "*d+":"*(width-1)+"/"+"+"*(depth-d))
           
for h in range(height,0,-1):#10~1
    if h<=depth:
        print("#"*width+"+"*(h-1))
    else:
        print("#"*width+"+"*depth)
# print(len(":::::::::::::::::::/"))