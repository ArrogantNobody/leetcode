class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        length1, length2 = 0, 0
        p = l1
        while p:
            length1 += 1
            p = p.next
        p = l2
        while p:
            length2 += 1
            p = p.next
        if length1 < length2:
            l1, l2 = l2, l1

        p1, p2 = l1, l2
        c = 0
        while p2:
            p1.val += p2.val
            p1 = p1.next
            p2 = p2.next
        p1 = l1
        while p1:
            p1.val += c
            c = 0
            if p1.val > 9:
                p1.val -= 10
                c = 1
            if not p1.next and c:
                p1.next = ListNode(1)
                break
            p1 = p1.next
        return l1