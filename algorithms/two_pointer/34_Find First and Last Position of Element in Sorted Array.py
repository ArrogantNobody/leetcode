class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        if target >= nums[0] and target <= nums[-1]:
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if target == nums[mid]:
                    print(mid)
                    l = mid
                    r = mid
                    while l - 1 >= 0 and nums[l - 1] == nums[l]:
                        l -= 1
                        print(l)

                    while r + 1 <= len(nums) - 1 and nums[r] == nums[r + 1]:
                        r += 1
                    return [l, r]
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return [-1, -1]

