class Solution1:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(len(s) - 1):  # 슬라이딩 윈도우가 오른쪽으로 이동
            result = max(
                result,
                expand(i, i + 1),  # 2칸짜리 two pointers
                expand(i, i + 2),  # 3칸짜리 two pointers
                key=len,
            )

        return result
