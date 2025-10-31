import collections
import heapq
from typing import List


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        most_common = counter.most_common(k)
        return [x[0] for x in most_common]


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)

        freqs_heap = []
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk


# ==============================================================================
# Solution 2
# ==============================================================================
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
