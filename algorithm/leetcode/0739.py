from typing import List


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tmp = []
        idx = []
        answer = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while tmp and tmp[-1] < t:
                answer[idx[-1]] = i - idx[-1]
                idx.pop()
                tmp.pop()

            tmp.append(t)
            idx.append(i)

        return answer


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last

            stack.append(i)

        return answer
