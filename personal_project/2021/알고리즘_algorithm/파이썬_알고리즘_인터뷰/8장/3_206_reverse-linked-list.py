# # 8-3 역순 연결 리스트

# # 연결리스트를 뒤집어라
# https://leetcode.com/problems/reverse-linked-list/

# from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
""" 
#1번째. 풀다가 포기
class Solution:
    def reverseList(self,head):
        node = head
        before=None
        if node.next == None:
            node.next=before
        else:
            
 """
""" 
#2번. 책 재귀구조
class Solution:
    def reverseList(self,head):
        def reverse(node,prev=None):
            if not node:
                return prev
            next,node.next = node.next,prev
            return reverse(next, node)
        return reverse(head)
                 """

#3번. 책 반복구조          
class Solution:
    def reverseList(self,head):
        node,prev = head,None
        
        while node:
            next,node.next = node.next,prev#뒤 대신 앞은 연결하여 역순으로 만들고
            prev,node = node,next#그 연결 리스트로 넘어가기 위해 swift 해준다.
            
        return prev
                
n5 = ListNode(5)
n4 = ListNode(4,n5)
n3 = ListNode(3,n4)
n2 = ListNode(2,n3)
n1 = ListNode(1,n2)

c= Solution()
print(c.reverseList(n1).va)

    

