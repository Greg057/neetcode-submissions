class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for char in s.lower():
            if char.isalpha() or char.isnumeric():
                t += char


        return t == t[::-1]
        