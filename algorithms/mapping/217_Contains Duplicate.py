class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return 0 if len(nums) == len(set(nums)) else 1
#==========================================================
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return 0
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return 0
#=======================================