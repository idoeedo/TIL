import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list:
            return []

        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next

        vals.sort()

        head = ListNode()
        node = head
        for v in vals:
            node.next = ListNode(v)
            node = node.next

        return head.next


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        root = ListNode(None)
        result = root
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
