from collections import defaultdict


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def __init__(self):
        self.hm = {}

    def put(self, key: int, value: int) -> None:
        self.hm[key] = value

    def get(self, key: int) -> int:
        if key in self.hm:
            return self.hm[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        self.hm.pop(key, None)


# ==============================================================================
# Solution 1
# ==============================================================================
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class Solution1:
    def __init__(self):
        self.size = 1000
        self.table = defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            # index 값이 비어있는 경우
            self.table[index] = ListNode(key, value)
            return
        else:
            # index 값이 비어있지 않은 경우
            p = self.table[index]
            while p:
                if p.key == key:
                    p.value = value
                    return
                if p.next is None:
                    break
                p = p.next

            p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size

        if self.table[index].value is None:
            return -1
        else:
            p = self.table[index]
            while p:
                if p.key == key:
                    return p.value
                p = p.next
            return -1

    def remove(self, key: int) -> None:
        index = key % self.size

        if self.table[index].value is None:
            return

        # 첫 번째 노드일 때 삭제
        p = self.table[index]
        if p.key == key:
            if p.next is None:
                self.table[index] = ListNode()
            else:
                self.table[index] = p.next
            return

        # 첫 번째 노드 이후의 노드일 때 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev = p
            p = p.next
