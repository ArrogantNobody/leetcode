# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return 1
        queue = [root]

        while queue:
            layer = []
            in_queue = []
            for item in queue:
                if not item:
                    layer.append(None)
                    continue
                layer.append(item.val)
                in_queue.append(item.left)
                in_queue.append(item.right)

            queue = in_queue
            if layer != layer[::-1]:
                return False
        return True
#recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def recur_helper(p, q):
            if not p:
                return not q
            if not q:
                return not p

            return p.val == q.val and recur_helper(p.left, q.right) and recur_helper(p.right, q.left)

        return recur_helper(root, root)