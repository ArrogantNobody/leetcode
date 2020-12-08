class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return
        nums = digits[::-1]
        nums[0] += 1
        for i in range(len(nums)):
            if nums[i] >= 10:
                nums[i] -= 10
                if i != len(nums) - 1:
                    nums[i + 1] += 1
                else:
                    nums.append(1)
        return nums[::-1]
