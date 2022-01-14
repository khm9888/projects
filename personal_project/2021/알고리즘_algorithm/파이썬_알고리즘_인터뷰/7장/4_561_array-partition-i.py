# # 7-4 배열 파티션 1

# # n개의 페어를 이용한 min(a,n)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
# https://leetcode.com/problems/array-partition-i/

from typing import List


# # 1번째. 짝수로 하는 방법

# a_list = [1,4,3,2]
# class Solution:
#     def arrayPairSum(self, nums: List[int]):
#             nums.sort(reverse=True)
#             leng = len(nums)//2
#             # max_v = 0 
#             v= 0 
#             for i in range(leng):
#                 v+=nums[2*i+1]
#             self.result = v
#             return self.result

# s = Solution()
# v = s.arrayPairSum(a_list)
# print(v)

# 2번째. 파이썬스러운 방법

a_list = [1,4,3,2]
class Solution:
    def arrayPairSum(self, nums: List[int]):
        nums.sort(reverse=True)
        print(nums)
        print(nums[1::2])
        return sum(nums[1::2])
    
s = Solution()
v = s.arrayPairSum(a_list)
print(v)
