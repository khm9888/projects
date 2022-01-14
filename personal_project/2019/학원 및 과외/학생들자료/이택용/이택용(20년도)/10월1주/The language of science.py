first=input()
second=input()
word_length= min(len(first),len(second))

record=0
for f in range(word_length):
    if first[f]==second[f]:
        record+=1
    else:
        break


record_back=0
cnt=0
for b in range(-1,-(word_length-record+1),-1):
    if first[b]==second[b]:
        record_back-=1
        cnt+=1        
    else:
        break
    
# long_length = max(len(first[record:record_back]),len(second[record:record_back]))
# short_length = min(len(first[record:record_back]),len(second[record:record_back]))
# length= (long_length-short_length)
# length_2=length//2
# gap = l
# if length%2==0:
#     length_1=length_2
# else:
#     length_1=length_2+1
# if len(first)>len(second):
#     if cnt!=0:
#         print(f"{' '*record}┏{first[record:record_back]}┓")
#         print(f"{first[:record]}┫{' '*long_length}┣{first[record_back:]}")
#         print(f"{' '*record}┗{' '*length_1}{second[record:record_back]}{' '*length_2}┛")
#     else:
#         print("case2")
#         print(f"{' '*record}┏{first[record:]}┓")
#         print(f"{first[:record]}┫{' '*fir}┣")
#         print(f"{' '*record}┗{' '*length_1}{second[record:]}{' '*length_2}┛")
        
# else:
#     if cnt!=0:
#         print(f"{' '*record}┏{' '*length_1}{first[record:record_back]}{' '*length_2}┓")
#         print(f"{first[:record]}┫{' '*long_length}┣{first[record_back:]}")
#         print(f"{' '*record}┗{second[record:record_back]}┛")
#     else:
#         print("case4")
#         print(f"{' '*record}┏{' '*length_1}{first[record:]}{' '*length_2}┓")
#         print(f"{first[:record]}┫{' '*long_length}┣")
#         print(f"{' '*record}┗{second[record:]}┛")
if cnt!=0:  
    first_inside=first[record:record_back]
    second_inside=second[record:record_back]
    try:
        splits=first.split(first[record:record_back])
    except:
        splits=["super","man"]
else:
    first_inside=first[record:]
    second_inside=second[record:]
    splits=first.split(first[record:])
max_length = max(len(first_inside),len(second_inside))
min_length = min(len(first_inside),len(second_inside))
length = max_length-min_length
length_2=length//2
if length%2==0:
    length_1=length_2
else:
    length_1=length_2+1
    
if first[record:record_back]=="re":
    splits=second.split(second[record:record_back])

if length==0:
    print(" "*len(splits[0])+"┏"+first_inside+"┓")
    print(splits[0]+"┫"+f"{' '*max_length}"+"┣"+"".join(splits[1:]))
    print(" "*len(splits[0])+"┗"+second_inside+"┛")
elif max_length == len(first_inside):
    print(" "*len(splits[0])+"┏"+first_inside+"┓")
    print(splits[0]+"┫"+f"{' '*max_length}"+"┣"+"".join(splits[1:]))
    print(" "*len(splits[0])+"┗"+" "*length_1+second_inside+" "*length_2+"┛")
else:
    print(" "*len(splits[0])+"┏"+" "*length_1+first_inside+" "*length_2+"┓")
    print(splits[0]+"┫"+f"{' '*max_length}"+"┣"+"".join(splits[1:]))
    print(" "*len(splits[0])+"┗"+second_inside+"┛")

# print(splits)