from collections import defaultdict
from typing import List


# ==============================================================================
# My Answer
# ==============================================================================
class MyAnswer:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        return list(anagrams.values())
