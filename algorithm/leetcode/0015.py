from typing import List


class MyAnswer:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for index_1 in range(len(nums)):
            x = nums[index_1]
            if x > 0:
                break
            for index_2 in range(index_1 + 1, len(nums)):
                y = nums[index_2]
                z = -(x + y)
                if y > z:
                    break
                if z in nums[index_2 + 1 :]:
                    result.append([x, y, z])

        result = list(set(tuple(sorted(item)) for item in result))
        return result


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                if total_sum < 0:
                    left += 1
                elif total_sum > 0:
                    right -= 1
                else:  # total_sum == 0
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results
