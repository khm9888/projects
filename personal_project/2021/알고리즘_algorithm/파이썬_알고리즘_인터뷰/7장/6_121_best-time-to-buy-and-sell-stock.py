# # 7-6 주식을 사고팔기 가장 좋은 시점

# # 한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# from typing import List

# class Solution:
#     def maxProfit(self,prices):
#         min_v=float("inf")
#         max_v=-float("inf")
#         for i, price in enumerate(prices):
#             if price<min_v:
#                 min_v=price
#                 min_loc=i
#         # print(min_loc)
#         for price in prices[min_loc+1:]:
#             if price>max_v:
#                 max_v=price
#         return max_v-min_v
                
#2번째 책에서

class Solution:
    def maxProfit(self,prices):
        min_v=float("inf")#syts.maxsize
        profit=0
        for price in prices:
            min_v=min(price,min_v)
            profit=max(profit,price-min_v)
        return profit
                
c= Solution()
print(c.maxProfit([7,1,5,3,6,4]))
