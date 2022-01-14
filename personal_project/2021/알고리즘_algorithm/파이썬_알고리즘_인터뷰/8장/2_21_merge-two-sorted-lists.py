# # 8-2 두 정렬 리스트의 병합

# # 정렬되어 있는 두 연결 리스트를 합쳐라.
# https://leetcode.com/problems/merge-two-sorted-lists/

# from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

""" class Solution:
    def mergeTwoLists(self, l1, l2):
        merge_list=[]
        while l1 and l2:
            if l1.val <= l2.val:
                merge_list.append(l1)
                l1 = l1.next                
            else:
                merge_list.append(l2)
                l2 = l2.next                
        while l1:
            merge_list.append(l1)
            l1 = l1.next                
        while l2:
            merge_list.append(l2)
            l2 = l2.next
        # l = len(merge_list)
        node_next = None
        for node in (merge_list[::-1]):
            node.next = node_next
            node_next = node
            # print(node.val)
        for n in merge_list:
            print(n.val)  
        # return    
n2_3 = ListNode(4)
n2_2 = ListNode(3,n2_3)
n2_1 = ListNode(1,n2_2)

n1_3 = ListNode(4)
n1_2 = ListNode(2,n1_3)
n1_1 = ListNode(1,n1_2)


c= Solution()
print(c.mergeTwoLists(n1_1,n2_1))
 """
#2번째 책에서 풀이

class Solution:
    def mergeTwoLists(self, l1, l2):
        if (not l1) or (l2 and l1.val > l2.val):
            l1,l2=l2,l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next,l2)
        return l1

n2_3 = ListNode(4)
n2_2 = ListNode(3,n2_3)
n2_1 = ListNode(1,n2_2)

n1_3 = ListNode(4)
n1_2 = ListNode(2,n1_3)
n1_1 = ListNode(1,n1_2)

c= Solution()
print(c.mergeTwoLists(n1_1,n2_1).next.val)
    

