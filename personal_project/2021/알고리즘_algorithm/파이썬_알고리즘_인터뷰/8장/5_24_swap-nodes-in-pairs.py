# # 8-5 페어의 노드 스왑

# # 연결 리스트를 입력받아 페어(pair) 단위로 스왑하라.
# https://leetcode.com/problems/swap-nodes-in-pairs/

# from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

''' #1번 값만 교환
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        cur = head
        
        while cur and cur.next:
            #값만 교환
            cur, cur.next = cur.next, cur
        
        return head '''

''' # 2번 반복 구조로 스왑
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            #b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head
            
            #prev가 b를 가리키도록 할당
            prev.next = b
            
            #다음 번 비교를 위해 이동
            head = head.next
            prev = prev.next.next
        return root.next
 '''
 
#3번 재귀 구조로 스왑
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p=head.next
            #스왑된 값 리턴 받음
            head.next=self.swapPairs(p.next)
            p.next = head
            return p
        return head

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

    

