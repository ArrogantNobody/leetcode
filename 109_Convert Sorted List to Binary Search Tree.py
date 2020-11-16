# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        tmp = []
        cur = head
        while cur:
            tmp.append(cur.val)
            cur = cur.next
        root = TreeNode(tmp[len(tmp) // 2])
        root_index = tmp.index(root.val)

        def initList(data):
            if not data:
                return
            head = ListNode(data[0])
            p = head
            for i in data[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
            return head

        l_tree = tmp[:root_index]
        ll_tree = initList(l_tree)
        r_tree = tmp[root_index + 1:]
        lr_tree = initList(r_tree)

        root.left = self.sortedListToBST(ll_tree)
        root.right = self.sortedListToBST(lr_tree)

        return root
#=========================================================
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.sortedArrayToBST(nums)

    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


#=========================================================
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        l_part = head
        r_part = slow.next

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(l_part)
        root.right = self.sortedListToBST(r_part)

        return root