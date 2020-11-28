class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
#=========================================================
if not needle:
    return 0

for i, char in enumerate(haystack):
            if char == needle[0]:
                if haystack[i:i + len(needle)] == needle:
                    return i

return -1