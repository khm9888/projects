# # 9-3 일일 온도

# # 매일의 화씨 온도 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.
# https://leetcode.com/problems/daily-temperatures/

# from typing import List

class Node:
    def __init__(self,item,next) -> None:
        self.item = item
        self.next = next

class Stack:
    def __init__(self) -> None:
        self.last=None
    
    def push(self,item):
        self.last=None(item,self.last)
        
    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item


#1번 자체 풀이했으나, 타임아웃
""" 
class Solution:
    def dailyTemperatures(self, T):
        result = []
        for idx,temp in enumerate(T):
            # print(idx,temp)
            if idx == len(T)-1:
                result.append(0)
            for idx2,temp2 in enumerate(T[idx+1:]):
                if temp2>temp:
                    result.append(idx2+1)
                    break
                if idx2 == len(T[idx+1:])-1:
                    result.append(0)
            # print(temp,result)      
        return result
 """
#2번 책에서 풀이

class Solution:
    def dailyTemperatures(self, T):
        result = [0]*len(T)
        stack = list()
        for idx,temp in enumerate(T):
            #현재 온도가 스택 값보다 높다면 정답처리
            while stack and temp >T[stack[-1]]:
                last = stack.pop()#가장 마지막의 인덱스
                result[last] = idx-last#현재 인덱스에서 이전 인덱스 뺌.
            stack.append(idx)
            # print(result)
        return result      
            
        
        

c= Solution()
print(c.dailyTemperatures([73,74,75,71,69,72,76,73]))
