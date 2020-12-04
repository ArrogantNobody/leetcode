# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        nodeList = []
        while head:
            nodeList.append(head.val)
            head = head.next

        node = list(set(nodeList))
        node.sort()
        newhead = ListNode(node[0])
        p = newhead
        for i in node[1:]:
            p.next = ListNode(i)
            p = p.next
        return newhead
#===================================================
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return p
#==========================================================
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = head
        while p and p.val == head.val:
            p = p.next
        head.next = self.deleteDuplicates(p)

        return head

