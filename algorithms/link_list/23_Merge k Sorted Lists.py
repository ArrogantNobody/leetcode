# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # if not lists:
        #     return
        s = []
        for item in lists:
            while item:
                s.append(item.val)
                item = item.next
        if not s:
            return
        s.sort()
        newhead = ListNode(s[0])
        p = newhead
        for i in s[1:]:
            p.next = ListNode(i)
            p = p.next

        return newhead
