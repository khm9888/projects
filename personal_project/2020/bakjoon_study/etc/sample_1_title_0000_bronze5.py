#블랙잭

#카드 3장의 값을 합쳐서, 정해진 숫자를 넘지 않고, 가장 큰 수를 구하여라

n,m = map(int,input().split())#몇 장의 카드를 받을지 n, 제한은 몇으로 할지  m

cards = list(map(int,input().split()))
cards.sort(reverse =True)#오름차순으로 정렬
# print(cards)
total=0
sum_cards=0
length=len(cards)
for i_num in range(0,length-2):
    for j_num in range(i_num+1,length-1):
        for k_num in range(j_num+1,length):
            sum_cards=cards[i_num]+cards[j_num]+cards[k_num]#3장의 합
            if sum_cards==m:#3장의 합이 m과 같다면, for문 탈출 -1번
                total=sum_cards
                break
            elif sum_cards<m and sum_cards>total:
                total=sum_cards
        if sum_cards==m:#3장의 합이 m과 같다면, for문 탈출 -2번
            break
    if sum_cards==m:#3장의 합이 m과 같다면, for문 탈출 -3번
        break
print(total)
