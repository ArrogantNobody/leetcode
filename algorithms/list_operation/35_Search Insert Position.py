# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#
#         for index, item in enumerate(nums):
#             if target <= item:
#                 nums.insert(index, target)
#                 return nums.index(target)
#             elif target > nums[-1]:
#                 return len(nums)

#optimized one
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for index, item in enumerate(nums):
            if target <= item:
                return index
        return len(nums)