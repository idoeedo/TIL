import re
from collections import Counter
from typing import List


class MyAnswer:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub("[^a-z\s]", " ", paragraph)
        paragraph = paragraph.split()
        counter = Counter(paragraph)

        for word, count in counter.most_common():
            if word in set(banned):
                continue
            return word


class Solution1:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [
            word
            for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
            if word not in banned
        ]

        counts = Counter(words)

        # 가장 자주 등장한 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]
