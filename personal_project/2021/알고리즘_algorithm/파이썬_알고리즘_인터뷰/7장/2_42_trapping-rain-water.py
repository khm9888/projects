# # # 7-2 빗물 트래핑

# # # 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
# https://leetcode.com/problems/trapping-rain-water/

# # import timeit

# # input_values = [0,1,0,2,1,0,1,3,2,1,2,1]

#     def trap(self, a_list):
#         le = len(a_list)
#         total = 0
#         for i,value in enumerate(a_list):
#             if i !=0 and i != le-1:
#                 dif=min(max(a_list[:i]),max(a_list[i+1:]))
#                 if value<dif:
#                     total+=dif-value             
#         return total


# # # # 투 포인터를 통해서 이동

# # import timeit
# # input_values = [0,1,0,2,1,0,1,3,2,1,2,1]

#     def trap(self, height):
#         if not height:
#             return 0

#         volume=0

#         left,right = 0, len(height)-1

#         left_max,right_max = height[left],height[right]

#         print(left,right,left_max,right_max)
#         while left<right:

#             left_max,right_max = max(left_max,height[left]),max(right_max,height[right])

#             if left_max<=right_max:
#                 volume+=left_max-height[left]
#                 left+=1
#             else:
#                 volume+=right_max-height[right]
#                 right-=1
#             print(left,right,left_max,right_max)
#         return volume
            
        
# t1 = timeit.default_timer()
# trap(input_values)
# t2 = timeit.default_timer()
# print("t1",t1)
# print("t2",t2)
# print((t2-t1)*1000)

# #스택 쌓기
class Solution:
    def trap(self, height):
        stack  =list()
        volume=0

        for i in range(len(height)):
            while stack and height[i] >height[stack[-1]]:
                print(stack)        
                top = stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1]-1
                waters = min(height[i],height[stack[-1]])-height[top]

                volume+=distance*waters
                print(volume)        
            stack.append(i)
        return volume

