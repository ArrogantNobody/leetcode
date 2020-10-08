class Solution:
    def twoSum(self, nums, target): #nums: List[int], target: int
        hashmap = {}
        for index, item in enumerate(nums):
            if target - item in hashmap:
                return [hashmap[target - item], index]
            hashmap[item] = index