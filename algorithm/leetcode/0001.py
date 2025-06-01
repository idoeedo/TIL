from typing import List


class MyAnswer:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, x in enumerate(nums):
            y = target - x
            if y in nums:
                i2 = len(nums) - 1 - nums[::-1].index(y)
                if i1 != i2:
                    return [i1, i2]


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
