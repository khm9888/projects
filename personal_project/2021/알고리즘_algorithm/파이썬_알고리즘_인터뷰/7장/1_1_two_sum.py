# # 7-1 /7번 - 두 수의 합

# # 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# https://leetcode.com/problems/two-sum/


# nums = [2,7,11,15] ; target = 9

# def two_sum(nums,target):
#     length = len(nums)
#     for i in range(length-1):
#         for j in range(i+1,length):
#             # print(nums[i],nums[j])
#             # print(target)
#             if target==nums[i]+nums[j]:
#                 return [i,j]
#     return -1       
# # print(two_sum(nums,target))
# # print(two_sum(nums,22))

# # 책보고 변경 #in 사용

# from typing import List
# def two_sum_2(nums: List[int], target: int)->List[int]:
#     for i,n in enumerate(nums[:-1]):
#         complement = target - n
#         if complement in nums[i+1:]:
#             return [i,nums.index(complement)]

# # v= two_sum_2(nums, target)
# # v= two_sum_2(nums, 22)

# # print(v)

# #딕셔너리를 이용해서 업그레이드

# import time

from typing import List
class Solution:

    def twoSum(self,nums: List[int], target: int)->List[int]:
        find_value = dict()
        for i,n in enumerate(nums):
            find_value[n]=i
        # print(find_value)
        for i,n in enumerate(nums[:-1]):
            complement = target - n
            if complement in find_value and i != find_value[complement] :
                return [i,find_value[complement]]
# t1 = time.time()
# v= two_sum_2(nums, target)
# t2 = time.time()
# v= two_sum_3(nums, 17)
# t3 = time.time()


# print(type(t2-t1))
# print(t2)
# print(t1)
# print(f"{t2-t1:.5f}")
# print(t3-t2)
# print(v)
