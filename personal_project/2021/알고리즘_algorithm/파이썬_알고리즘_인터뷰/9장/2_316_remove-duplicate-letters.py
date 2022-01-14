# # 9-2 중복 문자 제거

# # 증복된 문자를 제외하고 사전식 순서로 나열하라.
# https://leetcode.com/problems/remove-duplicate-letters/

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


#1번. 따로 시도했으나 사전식 정렬이 익숙치 않아서 실패
""" 
from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # a_set = set()
        o_dict = defaultdict()
        a_list = list()
        # a_node = Node()
        for al in s[::-1]:
            a_list.insert(0,al)
        result="".join(a_list)
        # print(a_list)
        # print(result)
        return result
     """
#2번 책 재귀함수 통해서 구현
""" from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):#중복값 없애고, 알파벳 순서대로 정렬.
            suffix = s[s.index(char):]#알파벳 처음 나온 글자의 index를 파악해서 거기부터 끝까지 
            # print("s",s)
            # print("suffix",suffix)
            # print("set(suffix)",set(suffix))
            # print("set(s)",set(s))
            if set(s) == set(suffix):#기준값 앞에도 중복되는게 있다.
                # print(True)
                # print("char",char)
                return char + self.removeDuplicateLetters(suffix.replace(char,""))
        return ""
            
 """
 
#3번 책 스택 구현
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter,seen,stack = Counter(s),set(),[]
        # print(counter)
        for char in s:
            # print("char",char)
            counter[char]-=1
            if char in seen:
                continue
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]]>0:#stack이 있고, stack 가장 오른 쪽 값이 현재보다 작고, 
                # print(stack and char < stack[-1] and counter[stack[-1]]>0)
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)      
            # print("stack",stack)
            
        return "".join(stack)
                  
        
        
 

c= Solution()
print(c.removeDuplicateLetters("cbacdcbc"))
