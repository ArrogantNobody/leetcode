class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex in [0, 1]:
            return [1] * (rowIndex + 1)
        else:
            nums = [1, 1]
            for num in range(2, rowIndex + 1):
                list1 = []
                for i in range(num - 1):
                    list1.append(nums[i] + nums[i + 1])
                nums = [1] + list1 + [1]
            return nums


