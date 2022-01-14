# # 12-3 순열

# # 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.
# # https://leetcode.com/problems/permutations/
# # 파일 이름 고치기



# 1번 dfs

""" from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = list()
        pre_elements = list()
        
        def dfs(elements):
            #리프 노드일 때 결과추가
            if len(elements) == 0:
                results.append(pre_elements[:])
            #순열 생성 재귀호출:
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                pre_elements.append(e)
                dfs(next_elements)
                pre_elements.pop()
                
        dfs(nums)
        return results

        
        if len(nums)<=1:
            return nums
c= Solution()
print(c.permute([1,2,3]))
 """
 
# 2번 itertools 모듈 사용

from itertools import permutations
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))
c= Solution()
print(c.permute([1,2,3]))
