class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        mapping = dict()
        for index, item in enumerate(pattern):
            if item in mapping:
                if mapping[item] != s[index]:
                    return False
            else:
                if s[index] in mapping.values():
                    return False
            mapping[item] = s[index]
        return True