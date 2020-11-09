class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for item in strs:
            t = str(sorted(item))
            if t in res:
                res[t].append(item)
            else:
                res[t] = [item]

        return res.values()