# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        l_len = self.maxDepth(root.left)
        r_len = self.maxDepth(root.right)

        if abs(l_len - r_len) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def maxDepth(self, root):
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
#===============================================================
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def tree_height(root):
            if not root:
                return 0
            l_len = tree_height(root.left)
            r_len = tree_height(root.right)

            if l_len == -1 or r_len == -1 or abs(l_len - r_len) > 1:
                return -1
            else:
                return max(l_len, r_len) + 1

        return tree_height(root) >= 0
