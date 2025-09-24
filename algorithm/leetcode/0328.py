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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode(1)
        odd_node = odd_head

        even_head = ListNode(2)
        even_node = even_head

        order = 1

        while head:
            if order % 2 == 1:
                odd_node.next = ListNode(head.val)
                odd_node = odd_node.next
            else:
                even_node.next = ListNode(head.val)
                even_node = even_node.next

            head = head.next
            order += 1

        odd_node.next = even_head.next

        return odd_head.next


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        odd = head
        odd_head = head

        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next

            even.next = even.next.next
            even = even.next

        odd.next = even_head
        return odd_head
