class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = dict()
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i == 0 or nums[i] > nums[i - 1]:
                l, r = i + 1, n - 1
                while l < r:
                    target = nums[i] + nums[l] + nums[r]
                    if target == 0:
                        col = [nums[i], nums[l], nums[r]]
                        max_num = max(col)
                        min_num = min(col)
                        if (max_num, min_num) not in tmp:
                            res.append(col)
                            tmp[(max_num, min_num)] = 1
                    elif target > 0:
                        r -= 1
                    elif target < 0:
                        l += 1
        return res

