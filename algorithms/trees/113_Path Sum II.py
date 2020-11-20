# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        res = list()

        def dfs(node, tmp):
            if not node:
                return

            tmp.append(node.val)
            if not node.left and not node.right and sum(tmp) == s:
                res.append(tmp[:])

            dfs(node.left, tmp)
            dfs(node.right, tmp)
            tmp.pop()

        dfs(root, list())
        return res