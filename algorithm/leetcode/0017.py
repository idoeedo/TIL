from typing import List


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def letterCombinations(self, digits: str) -> List[str]:
        def combine(characters, result):
            if not result:
                result = characters
            else:
                new_result = []
                for r in result:
                    for c in characters:
                        new_result.append(r + c)
                result = new_result

            return result

        letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        result = []
        for d in digits:
            result = combine(letter[d], result)

        return result


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return []

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        dfs(0, "")

        return result
