# # 8-6 홀짝 연결 리스트

# # 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.
# https://leetcode.com/problems/odd-even-linked-list/

# from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1번

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #예외처리
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
            
        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
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

    

