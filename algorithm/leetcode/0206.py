from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_ll = None

        while head:
            head.next, reversed_ll, head = reversed_ll, head, head.next

        return reversed_ll


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
