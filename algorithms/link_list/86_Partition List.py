# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head

        cur = head
        pre_min = cur_min = ListNode(-1)
        pre_max = cur_max = ListNode(-1)

        while cur:
            if cur.val < x:
                cur_min.next = cur
                cur_min = cur_min.next
            else:
                cur_max.next = cur
                cur_max = cur_max.next

            cur = cur.next

        cur_min.next = pre_max.next
        cur_max.next = None

        return pre_min.next
