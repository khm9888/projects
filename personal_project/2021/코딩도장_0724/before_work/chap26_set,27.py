# 그런데 요소를 변경할 수 없는 frozenset는 왜 사용할까요? frozenset는 세트 안에 세트를 넣고 싶을 때 사용합니다. 다음과 같이 frozenset는 frozenset를 중첩해서 넣을 수 있습니다. 단, frozenset만 넣을 수 있고, 일반 set는 넣을 수 없습니다.

# print(frozenset({frozenset({1, 2}), frozenset({3, 4})}))
# frozenset({frozenset({1, 2}), frozenset({3, 4})})

# x,y = tuple(map(int,input().split()))

# a = {c for c in range(1,x+1) if x%c==0}
# b = {d for d in range(1,y+1) if x%d==0}

# divisor = a & b
 
# result = 0
# if type(divisor) == set:
#     result = sum(divisor)
 
# print(result)

#1

# result=list()
# with open("word.txt","r") as f:
#     lines = f.readlines()
#     for line in lines:
#         words = line.split()
#         for word in words:
#             word = word.strip(",.")
#             if "c" in word:
#                 result.append(word)
# for w in result:
#     print(w)

#2

with open("word.txt","r") as f:
    words = f.read().split()
    # print(words)
    for word in words:
        word = word.strip(",.")
        if "c" in word:
            print(word)
