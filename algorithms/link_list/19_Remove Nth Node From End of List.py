# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res.pop(-n)
        if not res:
            return

        newhead = ListNode(res[0])
        p = newhead
        for i in res[1:]:
            p.next = ListNode(i)
            p = p.next
        return newhead
