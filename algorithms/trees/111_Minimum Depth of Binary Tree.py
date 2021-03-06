# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            if root.left and root.right:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            if root.left:
                return 1 + self.minDepth(root.left)
            if root.right:
                return 1 + self.minDepth(root.right)
            else:
                return 1
        else:
            return 0
#===============================================================