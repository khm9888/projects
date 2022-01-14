# # 8-4 두 수의 덧셈

# # 역순으로 저장된 연결 리스트의 숫자를 더하라.
# https://leetcode.com/problems/add-two-numbers/

# from typing import List
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
#1번 자체적으로 코드 진행했으나, 책에서 원하는 바를 모르겠음

'''         
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i=0
        while l1 and l2:
            print(i)
            l1.val=(l1.val+l2.val)%10
            if l1.next:
                next = l1.next
            elif l2.next:
                next = l2.next
            if next:
                next.val += (l1.val+l2.val)//10
            l1,l2 =l1.next,l2.next
            i+=1
        return l1 
'''
''' #2번 책에서 나온 코드
class Solution:
    def reverseList(self,head):#3_206 코드
        node,prev = head,None
        
        while node:
            next,node.next = node.next,prev#뒤 대신 앞은 연결하여 역순으로 만들고
            prev,node = node,next#그 연결 리스트로 넘어가기 위해 swift 해준다.
            
        return prev
    
    #연결리스트를 파이썬 리스트로 변환
    def toList(self, node:ListNode):
        a_list=[]
        while node:
            a_list.append(node.val)
            node=node.next
        return a_list
    
    #파이썬 리스트를 역행 연결리스트로 변환
    def toReversedLinkedList(self, result:list)->ListNode:
        prev : ListNode = None
        for r in result:
            node = ListNode(r)
            node.next=prev
            prev=node
        
        return node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))
        
        result = int("".join(str(e) for e in a))+\
                 int("".join(str(e) for e in b))
        # print(int("".join(str(e) for e in a)))
        # print(int("".join(str(e) for e in b)))
        # print(result)
        resultStr = str(result)
    
        return self.toReversedLinkedList(resultStr) '''
class Solution():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)
        
        carry=0
        while l1 or l2 or carry:
            sum=0
            #두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1=l1.next
            if l2:
                sum +=l2.val
                l2=l2.next
                
            #몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum+carry,10)
            head.next = ListNode(val)
            head=head.next
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

    

