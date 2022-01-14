# # 7-3 세 수의 합

# # 배열을 입력받아 합으로 -을 만들 수 있는 3개의 엘리먼트를 출력하라
# https://leetcode.com/problems/3sum/

# nums = [-1,0,1,2,-1,4]

# def sum_3(a_list):
#     ans = list()
#     for i,i_n in enumerate(a_list[:-2]):
#         for j,j_n in enumerate(a_list[i+1:]):
#             for k,k_n in enumerate(a_list[j+1:]):
#                 if (i_n+j_n+k_n)==0:
#                     ans.append([i,a_list.index(j_n),a_list.index(k_n)])
#     return ans

# def sum_3_2(a_list):
#     ans = list()
#     dict_value=dict()
#     for i,i_n in enumerate(a_list[:-2]):
#         for j,j_n in enumerate(a_list[i+1:]):
#             complement=i_n+j_n
#             dict_value[complement]+=(i,j)
#     for i,k in enumerate(a_list):
#         if k in dict_value and i not in dict[k][0] and i not in dict[k][1]:
            
        
# print(sum_3(nums))        

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i,n in enumerate(nums):
            complement = target - n
            if complement in nums[i+1:]:
                return i, nums[i+1:].index(complement)+(i+1)


nums = [2,7,11,15] ; target = 9
nums = [3,3] ; target = 6
s = Solution()

print(s.twoSum(nums,target))
