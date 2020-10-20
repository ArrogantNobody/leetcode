#dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        i = self.ite(p)
        j = self.ite(q)
        return i == j

    def ite(self, t: TreeNode):
        if not t:
            return
        vale = []
        queue = [t]
        while queue:
            currentNode = queue.pop()
            vale.append(currentNode.val)

            if currentNode.left:
                queue.append(currentNode.left)
            elif not currentNode.left:
                vale.append(None)
            if currentNode.right:
                queue.append(currentNode.right)
        return vale

#recursion1
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
#recursion2
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p:
            return not q
        if not q:
            return not p
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)