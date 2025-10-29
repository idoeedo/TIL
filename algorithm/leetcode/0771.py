from collections import Counter, defaultdict


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = Counter(stones)

        result = 0
        for j in jewels:
            result += counter[j]

        return result


# ==============================================================================
# Solution 1
# ==============================================================================
class Solution1:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = defaultdict(int)
        count = 0

        for s in stones:
            freqs[s] += 1

        for j in jewels:
            count += freqs[j]

        return count


# ==============================================================================
# Solution 2
# ==============================================================================
class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
