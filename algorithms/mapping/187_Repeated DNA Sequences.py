class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict
        n = len(s)
        res = defaultdict(int)

        for i in range(n - 9):
            res[s[i:i + 10]] += 1

        return [key for key, value in res.items() if value > 1]

#second
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        repeated = set()
        res = set()
        for i in range(n - 9):
            sub = s[i:i + 10]
            if sub in repeated:
                res.add(sub)
            else:
                repeated.add(sub)

        return list(res)

