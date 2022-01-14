# from collections import defaultdict
# z = defaultdict(lambda: 'python')
# print(z['a'])
# 'python'
# print(z[0])
# 'python'


# keys = ['a', 'b', 'c', 'd']
# x = {key: value for key, value in dict.fromkeys(keys).items()}
# # {'a': None, 'b': None, 'c': None, 'd': None}

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
 
# for key, value in x.items():
#     if value == 20:    # 값이 20이면
#         del x[key]     # 키-값 쌍 삭제
 
# # print(x)

# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# for key, value in x.items():
#     if value == 40:
#         del x[key]
# print(x)
        
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x = {key: value for key, value in x.items() if value != 40}
# print(x)


# 표준 입력으로 문자열 여러 개와 숫자 여러 개가 두 줄로 입력되고, 
# 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성합니다. 
# 다음 코드를 완성하여 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제하도록 만드세요.
keys = input().split()
values = map(int, input().split())
 
x = dict(zip(keys, values))
 
x = {k:v for k,v in x.items() if k !="delta" and v!=30}

print(x)