# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return
        # flatten the left part
        self.flatten(root.left)
        # flatten the right part
        self.flatten(root.right)

        right = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = right