import collections


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        min_idx_curr = 0
        min_idx_next = 0
        ls = collections.defaultdict(list)
        for i, char in enumerate(s):
            for j in range(min_idx_curr, i + 1):
                if char in ls[j]:
                    min_idx_next += 1
                else:
                    ls[j].append(char)

            min_idx_curr = min_idx_next

        length = {k: len(v) for k, v in ls.items()}
        return max(length.values())


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = 0
        start = 0

        for index, char in enumerate(s):
            if (char in used) and (start <= used[char]):
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length
