# a = [i for i in range(10)]

# print(a)

# a = [i for i in range(10) if i%2 ==0]

# print(a)

# #구구단
# a = [i * j for j in range(2, 10) for i in range(1, 10)]

# print(a)


# x,y = tuple(map(int,input().split()))
# l=[2**i for i in range(x,y+1)]
# l.pop(1)
# l.pop(-2)
# print(l)

#####################################23##################


# # list comprehension // sort // lambda

# students = [
#     ['john', 'C', 19],
#     ['maria', 'A', 25],
#     ['andrew', 'B', 7]
# ]

# print(students)
# print(sorted(students, key=lambda student: student[1]))  # 안쪽 리스트의 인덱스 1을 기준으로 정렬
# print(sorted(students, key=lambda student: student[2]))  # 안쪽 리스트의 인덱스 2를 기준으로 정렬

# # [['john', 'C', 19], ['maria', 'A', 25], ['andrew', 'B', 7]]
# # [['maria', 'A', 25], ['andrew', 'B', 7], ['john', 'C', 19]]
# # [['andrew', 'B', 7], ['john', 'C', 19], ['maria', 'A', 25]]

# # 다차원 복사

# import copy             # copy 모듈을 가져옴

# a = [[10, 20], [30, 40]]
# b = copy.deepcopy(a)    # copy.deepcopy 함수를 사용하여 깊은 복사
# b[0][0] = 500
# print(a)
# [[10, 20], [30, 40]]
# print(b)
# [[500, 20], [30, 40]]

row_leng,col_leng = list(map(int,input().split()))
bombs = list()
for row in range(row_leng):
    r = list(input())
    sample = list()
    for w in r:
        if w ==".":
            sample.append(0)
        else:
            sample.append("*")
    bombs.append(sample)
        

loc = [(i,j) for i in range(-1,2) for j in range(-1,2)]
print(loc)
for row in range(row_leng):
    for col in range(col_leng):
        # print(row,col)
        if bombs[row][col]=="*":
            for i,j in loc:
                row_i = row +i
                col_i = col +j
                if row_i<=-1 or row_i>=len(bombs) or col_i<=-1 or col_i>=len(bombs):
                    continue 
                elif not bombs[row_i][col_i]=="*":
                    bombs[row_i][col_i]+=1
for bomb in bombs:
    for b in bomb:
        print(b,end="")
    print()
    
# 먼저 2차원 리스트의 가로와 세로가 한 줄에 입력되므로 input에서 split을 사용한 뒤 변수 두 개에 저장해주면 됩니다(이하 변수는 col, row). 이때 input().split()의 결과는 문자열 상태이므로 map에 int를 사용하여 정수로 변환해줍니다.

# 가로와 세로를 입력받았으면 빈 리스트 matrix를 만듭니다. 그리고 row만큼 matrix.append(list(input()))를 반복해주면 입력된 문자열이 2차원 리스트 형태로 들어갑니다. 즉, input으로 한 줄씩 입력받은 뒤 list를 사용하면 문자열이 문자 리스트로 변환됩니다. 이걸 matrix에 append로 추가하면 2차원 리스트가 됩니다.

# 2차원 리스트가 준비되면 for range로 col, row만큼 반복하면서 요소가 *이면 continue로 건너뛰고 *가 아니면 0을 넣습니다.

# 0을 넣은 뒤에는 요소 주변 8개를 탐색하면서 *이면 요소를 1개씩 증가시키면 됩니다. 주변 요소를 탐색할 때는 range에 시작하는 값을 i - 1로 지정하고, 끝나는 값을 i + 2로 지정하여 한 칸 위부터 한 칸 아래까지 탐색합니다. 왜냐하면 range에서 생성한 숫자의 마지막 값은 끝나는 값보다 1 작은데, 탐색을 위해서 한 칸 아래까지 더 반복해야 하므로 i + 1이 아닌 i + 2가 되어야 합니다. 그리고 한 칸 앞과 한 칸 뒤도 같은 방식으로 반복합니다.

# for y in range(i - 1, i + 2):         # 한 칸 위부터 한 칸 아래까지 반복
#     for x in range(j - 1, j + 2):     # 한 칸 앞(왼쪽)부터 한 칸 뒤(오른쪽)까지 반복
# 단, 주변 요소를 탐색할 때 리스트의 범위를 벗어나면(y < 0 or x < 0 or y >= row or x >= col) 요소에는 접근하지 않고 건너뛰어야 합니다. 그렇지 않으면 인덱스가 음수가 되어 반대편 요소를 검사하거나, 요소가 없는 인덱스에 접근하게 됩니다.

# 참고로 2차원 리스트를 반복할 때 for i in matrix:와 for j in i:처럼 요소만 가져오면 인덱스를 알 수 없어서 주변을 탐색할 수 없습니다. 따라서 for에 range 또는 enumerate를 사용하거나 while을 사용하세요.
    
# a, b = map(int, input().split())

# mine_map = []
# for i in range(b):
#     mine_map.append([v for v in input()])

# finder = []
# value_range = (-1, 0, 1)
# for i in value_range:
#     for k in value_range:
#         if not(i == 0 and k == 0):
#             finder.append((i, k))
# result_map = [[0 for _ in range(b)] for _ in range(a)]

# print(result_map)#[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for i, row in enumerate(mine_map):
#     for j, v in enumerate(row):
#         if v == '*':
#             result_map[i][j] = '*'
#             print('*', end='')
#         else:
#             count = 0
#             for k, l in finder:
#                 temp_i = i + k
#                 temp_j = j + l
#                 if temp_i >= a or temp_i < 0 or temp_j >= b or temp_j <0:
#                     continue          
#                 if mine_map[temp_i][temp_j] == '*':
#                     count += 1
#             print(count, end='')
#         print(mine_map)

#     print()

