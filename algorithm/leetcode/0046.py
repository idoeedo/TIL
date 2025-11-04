import itertools
from typing import List


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        results = []
        prev_elements = []

        dfs(nums)

        return results
