#8-1 13번 팰린드롬 연결 리스트

#연결리스트가 팰린드롬 구조인지 판별하라
# https://leetcode.com/problems/palindrome-linked-list/

#1->2
#False

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#1번 리스트 변환        
''' class Solution:
    def isPalindrome(self, head):
        q = []
        if not head:
            return True

        node = head
        #리스트반환
        while node is not None:
            q.append(node.val)
            node = node.next

        #팰린드롬 판별
        while len(q)>1 :
            if q.pop(0)!=q.pop():
                return False
            
        return True
     '''
''' #2번 de-que (데크를 사용)
from collections import deque
class Solution:
    def isPalindrome(self, head):
        q = deque()
        
        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q)>1:
            if q.popleft()!=q.pop():
                return False
            
        return True
     '''


#2번 de-que (데크를 사용)
from collections import deque
class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        #러너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow  = slow.next
            
        #팰린드롬 여부 확인
        
        while rev and rev.val == slow.val:
            slow ,rev = slow.next,rev.next
        return not rev

n4 = ListNode(1)
n3 = ListNode(2,n4)
n2 = ListNode(2,n3)
n1 = ListNode(1,n2)

s= Solution()
v = s.isPalindrome(n1)
print(v)


