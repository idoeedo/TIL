from typing import List


class MyAnswer:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        product = 1
        for n in nums:
            left.append(product)
            product *= n

        right = []
        product = 1
        for n in nums[::-1]:
            right.append(product)
            product *= n
        right.reverse()

        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])
        return result


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out
