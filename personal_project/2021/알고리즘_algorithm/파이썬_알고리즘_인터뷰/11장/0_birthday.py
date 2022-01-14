# # 11-0 생일이 같을 확률

# # 10만 번 실험 중 생일이 같을 실험의 확률
# # 문제 링크
# # 파일 이름 고치기


# from typing import List

import random

TRIALS = 100000
same_birthdays = 0

# 10만 번 실험 진행

for _ in range(TRIALS):
    birthdays = list()
    #23명이 모였을 때, 생일이 같을 경우 same_birthdays += 1
    for i in range(23):
        birthday = random.randint(1,365)
        if birthday in birthdays:
            same_birthdays+=1
            break
        birthdays.append(birthday)
        
    # 전체 10만 번 실험 중 생일이 같을 실험의 확률
    if _%10000==0:
        print(f'{_}번 : {same_birthdays/TRIALS*100}%')
        
print(f'{same_birthdays/TRIALS*100}%')