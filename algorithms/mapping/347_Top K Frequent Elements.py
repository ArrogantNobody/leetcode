class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp = dict()
        res = []
        for item in nums:
            if item not in tmp:
                tmp[item] = 1
            else:
                tmp[item] += 1
        l = sorted(tmp.items(), key = lambda kv:(kv[1], kv[0]),reverse = True)
        print(l)
        for i in range(k):
            res.append(l[i][0])
        return res