from typing import List


class MyAnswer:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_sum = 0
        for i, n in enumerate(nums):
            if i % 2 != 0:
                continue
            max_sum += n

        return max_sum


class Solution1:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
