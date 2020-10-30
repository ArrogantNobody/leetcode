class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return

        hp = dict()
        for item in nums:
            if item not in hp:
                hp[item] = 1
            else:
                hp[item] += 1
        for item in hp:
            if hp[item] == 1:
                return item
        return 0
#method 2
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return

        for item in nums:
            if nums.count(item) == 1:
                return item
        return