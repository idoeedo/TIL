import itertools
from typing import List


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        results = []
        dfs([], 1, k)

        return results
