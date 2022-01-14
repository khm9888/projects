my_list  = ['Tick', 'Tock', 'Tock'] # 나의 리스트
new_list = ['Tick', 'Tock', 'Song'] # 추가로 나타난 리스트

# 나의 리스트 원소의 개수를 직접 센다
from collections import defaultdict
counter = defaultdict(int)
for item in my_list:
    counter[item] += 1
print(counter)    

# 추가된 리스트 원소의 개수를 누적하여 직접 센다
for item in new_list:
    counter[item] += 1
print(counter)      

# 값으로 정렬하여 가장 많이 나타난 2개를 출력한다
print(sorted(counter.items(), key=lambda kv: kv[1], reverse=True)[:2])


my_list  = ['Tick', 'Tock', 'Tock'] # 나의 리스트
new_list = ['Tick', 'Tock', 'Song'] # 추가로 나타난 리스트

# 나의 리스트를 센다
from collections import Counter
counter = Counter(my_list)
print(counter)

# 추가된 리스트를 누적하여 센다
counter.update(new_list)
print(counter)

# 가장 많이 나타난 2개를 출력한다
print(counter.most_common(n=2)


from collections import Counter
st = "나는 정말하하호호 히히 후후하하하 호호하하"
count = Counter(st)
count 
sorted(count.elements())