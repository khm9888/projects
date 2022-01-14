# # 11-2 보석과 돌

# # J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.
# # https://leetcode.com/problems/jewels-and-stones/
# # 파일 이름 고치기


# from typing import List

#1번은 생략

#2번은 생각해서 풀었기에 내 스타일로 작성

""" 
from collections import defaultdict

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        self.d_dict = defaultdict(int)
        for s in stones:
            self.d_dict[s]+=1
        self.result = 0 
        for j in jewels:
            self.result+=self.d_dict[j]
        return self.result
 """
 
#3번 Counter
""" 
from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)
        result = 0
        
        for j in jewels:
            result+= counter[j]
        return result
"""  

#4번 pythonic method

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)