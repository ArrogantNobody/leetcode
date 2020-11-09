# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        queue = [root]
        res = []
        while queue:
            layer = []
            in_queue = []
            for node in queue:
                if node:
                    layer.append(node.val)
                if node.left:
                    in_queue.append(node.left)
                if node.right:
                    in_queue.append(node.right)
            queue = in_queue
            if layer:
                res.append(layer)
        return res[::-1]