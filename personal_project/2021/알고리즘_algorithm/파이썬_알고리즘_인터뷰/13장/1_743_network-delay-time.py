# # 13-1 네트워크 딜레이 타임

# # k부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴한다. 
# 입력값(u,v,w)는 각각 출발지, 도착지, 소요 시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.
# # https://leetcode.com/problems/network-delay-time/
# # 파일 이름 고치기


from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int):
        graph = defaultdict(list)
        
        #그래프 인접 리스트 구성
        for u,v,w in times:
            graph[u].append((v,w))
            
        #큐 변수 : [(소요 시간, 정점)]
        Q = [(0,k)]
        
        dist = defaultdict(int)
        
        #우선 순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        # print(f"Q:{Q}")
        
        while Q:
            time, node = heapq.heappop(Q)#0,k
            if node not in dist: #k not in dist
                dist[node] = time # dist[k] = 0
                for v,w in graph[node]: #v - 목적지, w - 소요시간
                    alt = time + w #0 + 소요시간
                    heapq.heappush(Q,(alt,v))
            # print(f"Q:{Q}")
            
        # Q = [[0,k]]
        
        # dist = defaultdict(int)
        
        # while Q:
        #     time, node  = heapq.heappop(Q)
        #     if node not in dist:
        #         dist[node] = time
        #         for v,w in graph[node]:
        #             alt = time+w
        #             heapq.heappush(Q,(alt,v))
            
            
        # Q:[(0, 2)]
        # Q:[(1, 1), (1, 3)]
        # Q:[(1, 3)]
        # Q:[(2, 4)]
        # Q:[]
        
        print(f"dist:{dist}")
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        
        return -1
    
c= Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n,k = 4,2
print(c.networkDelayTime(times,n,k))
