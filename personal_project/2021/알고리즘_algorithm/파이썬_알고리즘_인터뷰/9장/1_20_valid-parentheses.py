# # 9-1 유효한 괄호

# # 괄호로 된 입력값이 올바른지 판별하라
# https://leetcode.com/problems/valid-parentheses/

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

#1번 stack을 구현하고, 첫번째 글자는 그냥 stack에 넣게끔 key로 넣지 않음.
#그 다음 stack이 비어있거나, value값과 stack.pop 값이 다르면 False
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
                 ")":"(",
                 "]":"[",
                 "}":"{"
                 }
        #스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char]!=stack.pop():
                return False
        return len(stack)==0

c= Solution()
print(c.isValid("[]{}()"))
