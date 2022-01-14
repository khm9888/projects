# # 8-7 역순 연결 리스트

# # 인덱스 m에서 n가지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.
# https://leetcode.com/problems/reverse-linked-list-ii/

# from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1번 반복 구조로 노드 뒤집기
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m==n:
            return head
        
        root = start = ListNode(None)
        root.next = head
        
        #start, end 지정
        
        for _ in range(m-1):
            start = start.next
        end = start.next
        
        #반복하면서 노드 차례대로 뒤집기
        for _ in range(n-m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
    

n5 = ListNode(5)
n4 = ListNode(4,n5)

n1_3 = ListNode(3)
n1_2 = ListNode(4,n1_3)
n1_1 = ListNode(2,n1_2)

n2_3 = ListNode(7)
n2_2 = ListNode(0,n2_3)
n2_1 = ListNode(8,n2_2)




c= Solution()
print(c.addTwoNumbers(n1_1,n2_1).next.val)

    

