class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[m] < nums[r]:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] > nums[r]:
                if target < nums[m] and target >= nums[l]:
                    r = m -1
                else:
                    l = m + 1
            else:
                r -= 1
        return False