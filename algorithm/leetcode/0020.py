from typing import List


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def isValid(self, s: str) -> bool:
        remain = ""
        s_list = list(s)
        for _ in range(len(s)):
            char = s_list.pop()
            if char in set(["(", "[", "{"]) and not remain:
                return False
            elif (
                (char == "(" and remain[0] == ")")
                or (char == "[" and remain[0] == "]")
                or (char == "{" and remain[0] == "}")
            ):
                remain = remain[1:]
            else:
                remain = char + remain

        if not remain:
            return True
        else:
            return False


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0
