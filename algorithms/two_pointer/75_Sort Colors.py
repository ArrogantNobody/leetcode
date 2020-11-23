class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a, b = 0, 0
        for item in nums:
            if item == 0:
                a += 1
            if item == 1:
                b += 1
        for i in range(len(nums)):
            if i < a:
                nums[i] = 0
            elif i >= a and i < a + b:
                nums[i] = 1
            else:
                nums[i] = 2
#==================================================
#双指针法，只动1和2
lo, hi = 0, len(nums) - 1
        i = 0
        while i <= hi:
            x = nums[i]
            if x == 0:
                nums[lo], nums[i] = nums[i], nums[lo]
                lo += 1
                i += 1
            elif x == 2:
                nums[hi], nums[i] = nums[i], nums[hi]
                hi -= 1
            else:
                i += 1
