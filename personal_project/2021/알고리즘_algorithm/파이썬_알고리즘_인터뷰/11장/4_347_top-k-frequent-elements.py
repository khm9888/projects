# # 11-4 상위 k 빈도 요소

# # 상위 k번째 빈도 요소 출력하기
# # https://leetcode.com/problems/top-k-frequent-elements/
# # 파일 이름 고치기

#1번 내가 Counter 사용한 방법
""" 
from typing import List

# from collections import defaultdict
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        result = list()
        for key in cnt:
            if cnt[key]>=k:
                result.append(key)

        return result    
c= Solution()
print(c.topKFrequent([1,1,1,2,2,3],2))
 """
#2번 책에서 Counter  사용한 방법
#빈도수를 음수 순으로 넣어서 앞에서부터 뽑아내는 방법. 다시 봐야할 필요 있음.
""" 
from typing import List

# from collections import defaultdict
from collections import Counter

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        freqs_heap = list()
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap,(-freqs[f], f))
        topk = list()
        # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
        
        print(freqs_heap)
        
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
            
        return topk

c= Solution()
print(c.topKFrequent([1,1,1,2,2,3],2)) 
"""

#3번 counter - python 용법 사용

from typing import List

# from collections import defaultdict
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*Counter(nums).most_common(k)))[0]
c= Solution()
print(c.topKFrequent([1,1,1,2,2,3],2)) 
