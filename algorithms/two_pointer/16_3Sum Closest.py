class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if not nums or n < 3:
            return
        nums.sort()
        res = float("inf")
        for i in range(n):
            l = i + 1
            r = n - 1
            while (l < r):
                cur_num = nums[i] + nums[l] + nums[r]

                if cur_num == target:
                    return target
                if abs(cur_num - target) < abs(res - target):
                    res = cur_num
                if cur_num < target:
                    l += 1
                else:
                    r -= 1
        return res