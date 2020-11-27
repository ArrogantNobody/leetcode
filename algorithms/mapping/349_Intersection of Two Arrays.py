class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        res = set()
        for item in nums1:
            if self.isexist(nums2, item):
                res.add(item)
        return list(res)

    def isexist(self, nums, i):
        l, r = 0, len(nums) - 1
        while (l <= r):
            mid = (l + r) // 2
            if nums[mid] > i:
                r = mid - 1
            elif nums[mid] < i:
                l = mid + 1
            else:
                return True
        return False
#==========================================================
        nums1 = set(nums1)
        result = set()
        for i in nums2:
            if i in nums1:
                result.add(i)
        return list(result)
#==========================================================
        return list(set(nums1) & set(nums2))