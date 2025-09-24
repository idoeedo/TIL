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
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        left_vals = []
        center_vals = []
        right_vals = []

        order = 0
        while head:
            if order < left - 1:
                left_vals.append(head.val)
            elif order >= right:
                right_vals.append(head.val)
            else:
                center_vals.append(head.val)

            order += 1
            head = head.next

        values = left_vals + center_vals[::-1] + right_vals

        new_head = ListNode(0)
        node = new_head
        for val in values:
            node.next = ListNode(val)
            node = node.next

        return new_head.next


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        root = ListNode(None)
        root.next = head

        start = root
        for _ in range(left - 1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp

        return root.next
