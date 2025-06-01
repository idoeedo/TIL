from typing import List


class Solution1:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left_index = 0
        right_index = len(height) - 1
        left_max = height[left_index]
        right_max = height[right_index]

        while left_index < right_index:
            left_max = max(height[left_index], left_max)
            right_max = max(height[right_index], right_max)

            if left_max <= right_max:
                volume += left_max - height[left_index]
                left_index += 1
            else:
                volume += right_max - height[right_index]
                right_index -= 1
        return volume


class Solution2:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 현재 높이가 이전 높이들보다 높을 때
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)

        return volume
