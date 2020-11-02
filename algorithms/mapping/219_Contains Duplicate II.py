class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tmp = dict()
        for index, item in enumerate(nums):
            if item in tmp:
                if abs(tmp[item] - index) <= k:
                    return 1
            tmp[item] = index

        return 0

