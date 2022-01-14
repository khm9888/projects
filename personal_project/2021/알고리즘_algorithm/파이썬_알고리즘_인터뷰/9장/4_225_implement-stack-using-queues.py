# # 9-4 큐를 이용한 스택 구현

# # 큐를 이용해 다음 연산을 지원하는 스택을 구현하라.
# https://leetcode.com/problems/implement-stack-using-queues/

# from typing import List

# #1번 이전에 만들어진 Node // Stack 으로 구현하려고 했으나 실패
""" 
class Node:
    def __init__(self,item,next) -> None:
        self.item = item
        self.next = next

class Stack:
    def __init__(self) -> None:
        self.last=None
    
    def push(self,item):
        self.last=Node(item,self.last)
        
    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item 

class MyStack:
    
    def __init__(self):
        
        self.last=None

    def push(self,item):
        self.last=Node(item,self.last)
        

    def pop(self) -> int:
        item = self.last.item
        self.last = self.last.next        
        return item

    def top(self) -> int:
        item = self.last.item
        self.last = self.last.next
        
        return item
        
    def empty(self) -> bool:
        return self.last
            
        
 """
 
 #2번 push 할 때 큐를 이용해 재정렬
from collections import deque
 
class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        #요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        
    def pop(self) -> int:
        return self.q.popleft()#제일 왼쪽에서 값 꺼내온 후 삭제.        

    def top(self) -> int:
        return self.q[0]#제일 왼쪽 값 가져오기만 하기.(삭제x)
        

    def empty(self) -> bool:
        return len(self.q)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# c= MyStack()
# print(c.func("asdffds"))
