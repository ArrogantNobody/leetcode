class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = ""
        for char in s.lower():
            if char.isalpha() or char.isdigit():
                tmp += char
        return tmp == tmp[::-1]
