# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        n = []
        p = head
        while head:
            n.append(head.val)
            head = head.next

        for i in range(0, len(n), 2):
            if i == len(n) - 1:
                break
            n[i], n[i + 1] = n[i + 1], n[i]

        head = p
        for j in n:
            head.val = j
            head = head.next

        return p
#recursion
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        node1, node2 = head, head.next
        tmp = self.swapPairs(node2.next)
        node2.next = node1
        node1.next = tmp

        return node2