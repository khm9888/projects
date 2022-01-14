# # 12-5 조합의 합

# # 숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복으로 나열 가능하다.
# # https://leetcode.com/problems/combination-sum/
# # 파일 이름 고치기
""" 
#1번 combinations으로 확인하기 - 멀티플을 하는데 어떻게 하는지 모르겠음. haemin`s method try - 실패

from typing import List
from itertools import combinations

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # results = list()
        # def calc(a_list,target):
        #     if sum(a_list)==target:
        #         return a_list
        
        results = list()
        cadidates_list=[]
        for i in range(1, len(candidates)+1):
            cadidates_list.extend(list(combinations(candidates,i)))
        for c in cadidates_list:
            if sum(c)==target:
                results.append(list(c))
        results.sort()
        return results
        
c= Solution()
print(c.combinationSum([2,2,3,7],7))
 """
#2번 책에 있는 dfs

from typing import List
from itertools import combinations

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(csum, index, path):
            #종료 조건
            if csum<0:
                return
            if csum == 0:
                result.append(path)
                return
            
            #자신부터 하위원소까지의 나열 재귀 호출
            
            for i in range(index, len(candidates)):
                dfs(csum-candidates[i],i,path+[candidates[i]])#7-2,0,[]+[2]        
            
        dfs(target,0,[])
        return result
    
c= Solution()
print(c.combinationSum([2,3,6,7],7))