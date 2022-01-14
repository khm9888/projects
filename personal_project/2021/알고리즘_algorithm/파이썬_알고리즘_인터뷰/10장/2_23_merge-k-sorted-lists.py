# # 10-2 k개 정렬 리스트 병합

# # k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라
# # https://leetcode.com/problems/merge-k-sorted-lists/
# # 파일 이름 고치기


# from typing import List

# Definition for singly-linked list.

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        root = result = ListNode(None)
        heap = list()
        
        #각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))
                # print(i,heap)
        # print(heap)
        
        cnt = 0
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            
            if result.next:
                heapq.heappush(heap,(result.next.val, idx, result.next))
                
            # print(True)
            # print(node)
            cnt+=1
            # input()
        return root.next

a3 = ListNode(5)
a2 = ListNode(4,a3)
a1 = ListNode(1,a2)

b3 = ListNode(4)
b2 = ListNode(3,b3)
b1 = ListNode(1,b2)

c2 = ListNode(6)
c1 = ListNode(2,c2)

c= Solution()
v=c.mergeKLists([a1,b1,c1])
# print(v)
