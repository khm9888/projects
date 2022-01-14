# # 12-8 코스 스케줄

# # 0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0,1] 쌍으로 표현하는 n개의 코스가 있다.
# 코스 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라.

# # https://leetcode.com/problems/course-schedule/
# # 파일 이름 고치기

"""
#1번 dfs로 순환 구조 판별

from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        #그래프 구성
        
        for x,y in prerequisites:
            graph[x].append(y)
        traced = set()
        
        def dfs(i):
            #순환구조이면 False
            if i in traced:
                return False
            traced.add(i)
            
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            
            return True
        
        #순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False   
            
        return True        

c= Solution()
print(c.canFinish(2,[[1,0]]))
 """



#2번 가지치기를 이용한 최적화

from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        #그래프 구성
        
        for x,y in prerequisites:
            graph[x].append(y)
            
        traced = set()
        visited = set()
        
        def dfs(i):
            #순환구조이면 False
            if i in traced:
                return False
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            
            visited.add(i)
            
            return True
        
        #순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False   
            
        return True        

c= Solution()
print(c.canFinish(2,[[1,0]]))
