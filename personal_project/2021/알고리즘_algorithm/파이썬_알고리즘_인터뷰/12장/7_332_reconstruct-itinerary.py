# # 12-7 일정 재구성

# # [from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라. 여러 일정이 있는 경우
# 사전 어휘순(Lexical Order)으로 방문한다.

# # https://leetcode.com/problems/reconstruct-itinerary/
# # 파일 이름 고치기

""" 
#1번 dfs

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph  = defaultdict(list)
        
        #그래프 순서대로 구성
        for a,b in sorted(tickets):
            graph[a].append(b)
            
        # print(f"graph:{graph}")
        route=[]
        def dfs(a):
            # print(f"a:{a}")
            #첫 번째 값을 읽어 어휘 순 방문
            while graph[a]:
                # print(graph[a])
                dfs(graph[a].pop(0))
            route.append(a)
                # print(route)
                
        dfs("JFK")
        
        return route[::-1]
        

c= Solution()
print(c.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
 """
""" 

#2번 스택 연산으로 큐 연산 최적화 시도

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph  = defaultdict(list)
        
        #그래프 순서대로 구성
        for a,b in sorted(tickets,reverse=True):
            graph[a].append(b)
            
        route = list()
        def dfs(a):
            #마지막 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)
            
        dfs("JFK")
        #다시 뒤집어 어휘 순 결과로

        return route[::-1]            

c= Solution()
print(c.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))

 """
#3번 일정 그래프 반복

from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph  = defaultdict(list)
        
        #그래프 순서대로 구성
        for a,b in sorted(tickets):
            graph[a].append(b)
            
        route,stack = list(),["JFK"]
        while stack:
            #반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())
            
        #다시 뒤집어 어휘 순 결과로

        return route[::-1]            

c= Solution()
print(c.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))