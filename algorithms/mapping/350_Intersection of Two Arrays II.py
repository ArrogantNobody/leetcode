class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res, record = [], {}
        for num in nums1:
            record[num] = record.get(num, 0) + 1

        for num in nums2:
            if num in record and record[num]:
                res.append(num)
                record[num] -= 1
        return res
