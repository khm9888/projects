# # 12-6 부분합

# # 모든 부분 집합을 리턴하라
# # https://leetcode.com/problems/subsets/
# # 파일 이름 고치기

""" 
#1번 시도해보기 - 성공

from typing import List
from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        results = list()
        cadidates_list=[]
        for i in range(0, len(nums)+1):
            results.extend(list(combinations(nums,i)))
        results = list(map(list,results))
        # results.sort()
        return results

c= Solution()
print(c.subsets([1,2,3]))
 """
#2번 dfs

# from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list()
        
        def dfs(index, path):
            #매번 결과 추가
            result.append(path)
            
            #경로를 만들면서 dfs
            
            for i in range(index, len(nums)):
                dfs(i+1,path+[nums[i]])
        
        dfs(0,[])
        return result
c= Solution()
print(c.subsets([1,2,3]))
      