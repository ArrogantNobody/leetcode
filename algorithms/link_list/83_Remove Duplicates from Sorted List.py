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


