# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        res = []
        self.generate(root, res)
        return res

    def generate(self, root, res):
        if not root:
            return

        self.generate(root.left, res)
        res.append(root.val)
        self.generate(root.right, res)
