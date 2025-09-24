from typing import List


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_sum = 0
        for i, n in enumerate(nums):
            if i % 2 != 0:
                continue
            max_sum += n

        return max_sum


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
