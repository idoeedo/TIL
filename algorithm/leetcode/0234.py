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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        if values == values[::-1]:
            return True
        else:
            return False


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev
