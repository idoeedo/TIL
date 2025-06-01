from collections import defaultdict
from typing import List


class MyAnswer:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log, digit_log = defaultdict(list), []

        for log in logs:
            split_log = log.split(" ")
            if log[-1].isdigit():
                digit_log.append(log)
            else:
                letter_log[" ".join(split_log[1:])].append(split_log[0])

        answer = []

        for log in sorted(letter_log):
            for identifier in sorted(letter_log[log]):
                answer.append(f"{identifier} {log}")

        answer.extend(digit_log)

        return answer


class Solution1:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 두 개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
