from collections import Counter


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def removeDuplicateLetters(self, s: str) -> str:
        pass


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []

        for char in s:
            counter[char] -= 1

            if char in stack:
                continue

            # 뒤에 붙일 문자가 남아 있다면 stack에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()

            stack.append(char)

        return "".join(stack)
