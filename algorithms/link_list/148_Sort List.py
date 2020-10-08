#there are several ways to solve this question, due to the limited time, I will only introduce one function
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #main idea of this function is to store val in a list and return them to linklist
        if not head or not head.next:
            return head

        p = head
        node_list = []
        while head:
            node_list.append(head.val)
            head = head.next

        node_list.sort()
        head = p
        for i in node_list:
            head.val = i
            head = head.next

        return p