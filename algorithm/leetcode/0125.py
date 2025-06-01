import re


class MyAnswer:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if c.isalnum()])
        s = s.lower()
        return s == s[::-1]


class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)
        return s == s[::-1]
