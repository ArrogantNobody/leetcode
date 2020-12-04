# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        tmp = dict()
        nodeL = []
        while head:
            if head.val in tmp:
                tmp[head.val] += 1
            else:
                tmp[head.val] = 1
            head = head.next

        for i in tmp.keys():
            if tmp[i] == 1:
                nodeL.append(i)
        if not nodeL:
            return
        else:
            nodeL.sort()
            newhead = ListNode(nodeL[0])
            p = newhead
            for i in nodeL[1:]:
                p.next = ListNode(i)
                p = p.next
            return newhead
#====================================================================
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:  # 0个或者1个元素不用去重
            return head
        newhead = ListNode(-1)  # 设置dummyhead
        newhead.next = head
        if head.val != head.next.val:  # 如果前两个节点不同，说明第一个节点一定有效
            head.next = self.deleteDuplicates(head.next)
        else:  # 如果前两个节点相同，就一直往后找，直到找到链表结束或者找到跟头节点值不同的节点p
            p = head
            while p and p.val == head.val:
                p = p.next
            newhead.next = self.deleteDuplicates(p)

        return newhead.next