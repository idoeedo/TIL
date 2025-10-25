# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def __init__(self, k: int):
        self.cq = []
        self.length = k

    def enQueue(self, value: int) -> bool:
        if len(self.cq) < self.length:
            self.cq.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if len(self.cq) > 0:
            self.cq = self.cq[1:]
            return True
        else:
            return False

    def Front(self) -> int:
        if len(self.cq) > 0:
            return self.cq[0]
        else:
            return -1

    def Rear(self) -> int:
        if len(self.cq) > 0:
            return self.cq[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.cq) == 0

    def isFull(self) -> bool:
        return len(self.cq) == self.length


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        # rear 포인터 이동
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        # front 포인터 이동
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        if self.q[self.p1] is None:
            return -1
        else:
            return self.q[self.p1]

    def Rear(self) -> int:
        if self.q[self.p2 - 1] is None:
            return -1
        else:
            return self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        return (self.p1 == self.p2) and (self.q[self.p1] is None)

    def isFull(self) -> bool:
        return (self.p1 == self.p2) and (self.q[self.p1] is not None)
