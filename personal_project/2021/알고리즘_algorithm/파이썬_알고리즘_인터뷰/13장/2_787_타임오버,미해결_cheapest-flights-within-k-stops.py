# # 13-2 k경유지 내 가장 저렴한 항공권

# # 시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, 
# k개의 경유지 이내에 도착하는 가격을 리턴하라. 경로가 존재하지 않을 경우 -1을 리턴한다.

# # https://leetcode.com/problems/cheapest-flights-within-k-stops/
# # 파일 이름 고치기


# # #1번 책의 풀이지만, 책풀이 틀렸음

# from typing import List
# from collections import defaultdict
# import heapq

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int):
#         #그래프 생성
#         graph = defaultdict(list)
#         for departure, arrival, cost in flights:
#             graph[departure]=arrival,cost

            
#         # if src in graph and graph[src][0]==dst:            
#         #     row_cost = graph[src][1]
        
#         # 큐 변수  : [(가격,정점, 남은 가능 경유지 수)]
#         Q = [(0,src,k)]
        
#         print(f"graph:{graph}")
#         print(f"Q:{Q}")
#         #우선 순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
#         while Q:
#             price, node , cnt = heapq.heappop(Q)
#             if cnt>=-1:
#                 if node == dst:
#                     return price
#             if k>=0:
#                 # print(f"k:{k}")
#                 # print(f"node:{node}")
#                 # print(f"graph[node]:{graph[node]}")
#                 v, w =graph[node]
#                 alt = price+w
#                 heapq.heappush(Q, (alt,v,cnt-1))
                    
#             # print(f"Q:{Q}")
#         return -1
        
# c= Solution()
# n=3
# edges = [[0,1,100],[1,2,100],[0,2,500]]
# print(c.findCheapestPrice(n,edges,0,2,1))



#2번 - 책 기본으로 해서 수정했으나, 타임오버

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int):
        #그래프 생성
        graph = defaultdict(list)
        for departure, arrival, cost in flights:
            graph[departure].append([arrival,cost])
            
        # if src in graph and graph[src][0]==dst:            
        #     row_cost = graph[src][1]
        
        # 큐 변수  : [(가격,정점, 남은 가능 경유지 수)]
        Q = [(0,src,k)]
        
        # print(f"graph:{graph}")
        # print(f"Q:{Q}")
        #우선 순위 큐 최솟값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node , cnt = heapq.heappop(Q)
            if node == dst and cnt>=-1:
                return price
            if k>=0:
                for v, w in graph[node]:
                    alt = price+w
                    heapq.heappush(Q, (alt,v,cnt-1))
                    
            # print(f"Q:{Q}")
        return -1
        
c= Solution()
n=3
edges = [[0,1,100],[1,2,100],[0,2,500]]
print(c.findCheapestPrice(n,edges,0,2,1))


# #3번. leetcode 가이드 - 해결은 됐으나, 파악이 제대로 안 됨. 꼼수 같음.

# from typing import List
# from collections import defaultdict
# import heapq

# class Solution(object):
#     def findCheapestPrice(self, n, flights, src, dst, K):
#         # n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
#         graph = defaultdict(list)
#         for flight in flights:
#             if flight[0] in graph:
#                 graph[flight[0]][flight[1]] = flight[2]
#             else:
#                 graph[flight[0]] = {flight[1]:flight[2]}

        
#         rec = {}
#         heap = [(0, -1, src)]
#         heapq.heapify(heap)
#         while heap:
#             cost, stops, city = heapq.heappop(heap)
#             if city == dst:
#                 return cost
#             print(f"graph:{graph}")
#             print(f"rec:{rec.get((city))}")
#             # print(f"rec.get(city, stops):{rec.get((city))}")
#             if stops == K or rec.get((city, stops), float('inf')) < cost:
#                 continue
#             if city in graph:
#                 print(f"city:{city}")
#                 print(f"city`s type:{(city)}")
#                 for nei, price in graph[city].items():
#                 # for nei, price in graph[city]:
#                     summ = cost + price
#                     if rec.get((nei, stops+1), float('inf')) > summ:
#                         rec[(nei, stops+1)] = summ
#                         heapq.heappush(heap, (summ, stops+1, nei))
#         return -1
    
# c= Solution()
# n=3
# edges = [[0,1,100],[1,2,100],[0,2,500]]
# print(c.findCheapestPrice(n,edges,0,2,1))
