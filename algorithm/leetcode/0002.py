from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyAnswer:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        base = 1
        d1 = 0
        while l1:
            d1 += base * l1.val
            base *= 10
            l1 = l1.next

        base = 1
        d2 = 0
        while l2:
            d2 += base * l2.val
            base *= 10
            l2 = l2.next

        head = ListNode()
        node = head
        sum_reversed = str(d1 + d2)[::-1]
        for val in sum_reversed:
            node.next = ListNode(int(val))
            node = node.next

        return head.next


class Solution1:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next
