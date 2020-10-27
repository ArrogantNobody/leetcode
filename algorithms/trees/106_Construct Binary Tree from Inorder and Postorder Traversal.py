# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None

        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])

        l_inorder = inorder[:root_index]
        r_inorder = inorder[root_index + 1:]

        l_postorder = postorder[: len(l_inorder)]
        r_postorder = postorder[len(l_inorder): -1]

        root.left = self.buildTree(l_inorder, l_postorder)
        root.right = self.buildTree(r_inorder, r_postorder)

        return root
