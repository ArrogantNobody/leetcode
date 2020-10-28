class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2[:]
        nums1.sort()
        return nums1

#two pointer
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = []
        p1 = 0
        p2 = 0
        while (p1 < m and p2 < n):
            if (nums1[p1] > nums2[p2]):
                tmp.append(nums2[p2])
                p2 += 1
            else:
                tmp.append(nums1[p1])
                p1 += 1

        while (p1 < m):
            tmp.append(nums1[p1])
            p1 += 1
        while (p2 < n):
            tmp.append(nums2[p2])
            p2 += 1

        for i in range(0, m + n):
            nums1[i] = tmp[i]
        return nums1