# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        root = TreeNode(nums[len(nums) // 2])
        root_index = nums.index(root.val)

        l_tree = nums[: root_index]
        r_tree = nums[root_index + 1:]

        root.left = self.sortedArrayToBST(l_tree)
        root.right = self.sortedArrayToBST(r_tree)

        return root