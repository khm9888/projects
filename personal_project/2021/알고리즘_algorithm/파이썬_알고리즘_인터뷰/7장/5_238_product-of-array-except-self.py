# # 7-5-자신을 제외한 배열의 곱

# # 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되로록 출력하라.
# https://leetcode.com/problems/product-of-array-except-self/

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         k =[]
#         r =[]
#         for i, x in enumerate(nums):
#             v = nums.copy()
#             v.pop(i)
#             n=1
#             for j in v:
#                n*=j
#             r.append(n)  
#         return r
# c= Solution()
# print(c.productExceptSelf([1,2,3,4]))


#2번 책에서 제공하는 코드

class Solution:
    def productExceptSelf(self, nums):
        out = []
        p = 1
        #왼쪽 곱셈
        for i in range(0,len(nums)):
            out.append(p)
            p=p*nums[i]
        # print(out)#[1, 1, 2, 6]
        p = 1
        for i in range(len(nums)-1,0-1,-1):
            out[i]*=p
            p=p*nums[i]
        # print(out)#[24, 12, 8, 6]
        return out
        
c= Solution()
print(c.productExceptSelf([1,2,3,4]))
    
        
        