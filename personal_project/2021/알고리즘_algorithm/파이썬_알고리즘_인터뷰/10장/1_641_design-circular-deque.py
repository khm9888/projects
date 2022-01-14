# # 10-0 원형 데크 디자인

# # 다음 연산을 제공하는 원형 데크를 디자인하라.

# # https://leetcode.com/problems/design-circular-deque/
# # 파일 이름 고치기


# from typing import List


#1번 이중 연결 리슽를 이용한 데크 구현

class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MyCircularDeque:
    
    def __init__(self, k: int):
        self.head,self.tail = ListNode(None),ListNode(None)
        self.k,self.len = k,0
        self.head.right,self.tail.left =self.tail,self.head
        
    def _add(self, node, new):
        n = node.right
        node.right = new
        new.left,new.right = node,n
        n.left = new        

    def _del(self, node):
        n = node.right.right
        node.right = n
        n.left = node      

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len+=1
        self._add(self.head,ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len+=1
        self._add(self.tail.left,ListNode(value))
        return True
            

    def deleteFront(self) -> bool:
        if self.len ==0:
            return False
        self.len-=1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len ==0:
            return False
        self.len-=1
        self._del(self.tail.left.left)
        return True
        

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1
        

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1
        

    def isEmpty(self) -> bool:
        return self.len == 0
        

    def isFull(self) -> bool:
        return self.len == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(5)

# param_= obj.insertFront(3)
# param_= obj.insertFront(1)
# param_= obj.insertFront(4)
# print(param_)
# param_= obj.insertLast(2)#4132
# print(param_)
# param_= obj.deleteFront()
# print(param_)
# param_= obj.deleteLast()
# print(param_)
# param_= obj.getFront()
# print(param_)
# param_= obj.getRear()
# print(param_)
# param_= obj.isEmpty()
# print(param_)
# param_= obj.isFull()
# print(param_)