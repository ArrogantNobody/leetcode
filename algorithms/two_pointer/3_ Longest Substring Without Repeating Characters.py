# sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = dict()
        res = 0
        start = 0
        for end in range(len(s)):
            if s[end] in dic:
                #if continuous str like pww, start will jump to end's position, else, like abcabc, start + 1
                start = max(start, dict[s[end]]+1)
            dic[s[end]] = end
            res = max(res, end - start + 1)
        return res