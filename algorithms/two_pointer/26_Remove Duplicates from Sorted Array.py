class Solution(object):
    def removeDuplicates(self, nums):
        s = list(set(nums))
        s.sort()
        nums[:len(s)] = s
        return len(s)


class Solution(object):
    def removeDuplicates(self, nums):
        p = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[p] = nums[i]
                p += 1
        return p