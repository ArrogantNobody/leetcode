class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = set()
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i == 0 or nums[i] > nums[i - 1]:
                l, r = i + 1, n - 1
                while l < r:
                    target = nums[i] + nums[l] + nums[r]
                    if target == 0:
                        col = [nums[i], nums[l], nums[r]]
                        if (nums[r], nums[i]) not in tmp:
                            res.append(col)
                            tmp.add((nums[r], nums[i]))
                    elif target > 0:
                        r -= 1
                    else:
                        l += 1
        return res

