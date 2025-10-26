from collections import deque


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def __init__(self, k: int):
        self.cd = deque()
        self.length = k

    def insertFront(self, value: int) -> bool:
        if len(self.cd) < self.length:
            self.cd.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.cd) < self.length:
            self.cd.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if len(self.cd) > 0:
            self.cd.popleft()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if len(self.cd) > 0:
            self.cd.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if len(self.cd) > 0:
            return self.cd[0]
        else:
            return -1

    def getRear(self) -> int:
        if len(self.cd) > 0:
            return self.cd[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.cd) == 0

    def isFull(self) -> bool:
        return len(self.cd) == self.length


# ==============================================================================
# Solution 1
# ==============================================================================
class ListNode:
    # Definition for doubly-linked-list
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution1:
    def __init__(self, k: int):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.k = k
        self.len = 0
        self.head.right = self.tail
        self.tail.left = self.head

    def _add(self, node: ListNode, new: ListNode):
        # node(이중 연결 리스트)의 오른쪽에 신규 노드를 삽입
        n = node.right
        node.right = new
        new.left = node
        new.right = n
        n.left = new

    def _del(self, node: ListNode):
        # node(이중 연결 리스트)의 오른쪽에 있는 노드를 제거
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        else:
            self.len += 1
            self._add(self.head, ListNode(value))
            return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        else:
            self.len += 1
            self._add(self.tail.left, ListNode(value))
            return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        else:
            self.len -= 1
            self._del(self.head)
            return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        else:
            self.len -= 1
            self._del(self.tail.left.left)
            return True

    def getFront(self) -> int:
        if self.len > 0:
            return self.head.right.val
        else:
            return -1

    def getRear(self) -> int:
        if self.len > 0:
            return self.tail.left.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k
