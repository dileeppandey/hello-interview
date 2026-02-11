# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        if head.next == head:
            return True
        slow = head
        fast = head
        while True:
            if fast is None or fast.next is None:
                return False
            if fast.next.next == slow.next:
                return True
            slow = slow.next
            fast = fast.next.next
