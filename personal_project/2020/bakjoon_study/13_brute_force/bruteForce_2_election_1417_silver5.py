#1417
#국회의원선거

#리스트에서 0번째에서 위치한 숫자가, 가장 큰 수가 되기 위해. 기존의 큰 숫자에서 1씩 빼오려고 한다.
#이 행동을 몇 번을 해야 0번째가 가장 큰 수가 되는가?

persons=int(input())#등록한 후보 총 인원수는 몇?
people = []#후보들 
for i in range(persons):
    people.append(int(input()))#숫자입력
    
dasom = people[0]
candidate = people[1:]
candidate = sorted(candidate)
cnt=0#몇번했는지 확인
if persons==1:
    pass
else:
    dasom = people[0]
    candidate = people[1:]
    candidate.sort()
    while dasom<=candidate[-1]:#다솜이 다른 후보들의 가장 큰 값보다 작거나 같으면 -> 다솜이 가장 큰 값이 아니라면
        candidate[-1]-=1
        dasom+=1
        candidate = sorted(candidate)
        cnt+=1      
        # print(people)
        # print(cnt,people)
print(cnt)
