from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyAnswer:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev_prev = ListNode(val=-1, next=head)
        prev = head
        curr = head.next

        answer = prev_prev

        while True:
            prev_prev.next, curr.next, prev.next = curr, prev, curr.next

            if prev.next and prev.next.next:
                prev_prev, prev, curr = prev, prev.next, prev.next.next
            else:
                break

        return answer.next


class Solution1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            # prev → head (a) → b 순서로 존재

            # b가 head를 가리키도록
            b = head.next
            head.next = b.next
            b.next = head

            # prev가 b를 가리키도록
            prev.next = b

            # 다음 번 비교를 위해 이동
            head = head.next
            prev = prev.next.next

        return root.next


class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p

        return head
