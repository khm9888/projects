# # 12-4 조합(combination)

# # 전체 수 n을 입력받아 k개의 조합 을 리턴하라
# # https://leetcode.com/problems/combinations/
# # 파일 이름 고치기

""" #1번 itertools 모듈 사용 - 책에서 있는대로 사용

from typing import List
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1,n+1),k))
    
    
c= Solution()
print(c.combine(4,2))
 """


#2번 dfs
      
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        def dfs(elements, start:int, k:int):
            if k==0:
                results.append(elements[:])
                return
            
            #자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements,i+1,k-1)
                elements.pop()
                
        dfs([],1,k)
        return results
    

c= Solution()
print(c.combine(4,2))

