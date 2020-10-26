# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        l_inorder = inorder[: inorder.index(root.val)]
        r_inorder = inorder[inorder.index(root.val) + 1:]

        len_ltree = len(l_inorder)
        l_preorder = preorder[1: len_ltree + 1]
        r_preorder = preorder[len_ltree + 1:]

        root.left = self.buildTree(l_preorder, l_inorder)
        root.right = self.buildTree(r_preorder, r_inorder)

        return root
