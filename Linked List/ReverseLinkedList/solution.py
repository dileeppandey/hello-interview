# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        new_head = None
        while current is not None:
            temp = current.next
            current.next = new_head
            new_head = current
            current = temp
        return new_head