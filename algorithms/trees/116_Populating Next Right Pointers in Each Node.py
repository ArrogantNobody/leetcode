"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = [root]
        while queue:
            next_queue = []
            for i, node in enumerate(queue):
                if not node:
                    continue
                if i != len(queue) - 1:
                    node.next = queue[i+1]
                next_queue.append(node.left)
                next_queue.append(node.right)
            queue = next_queue[:]
        return root
#==================================================
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 先排除掉不需要处理的情况
        if not root or (not root.left and not root.right):
            return root

        # 某一个节点的左孩子的next一定是指向这个节点的右孩子
        root.left.next = root.right

        # 当某一个节点的next不为空的时候，这个节点的右孩子的next一定是指向该节点next的left
        if root.next:
            root.right.next = root.next.left

        # 递归处理下一层
        self.connect(root.left)
        self.connect(root.right)

        return root