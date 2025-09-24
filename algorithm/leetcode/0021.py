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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return head.next


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
