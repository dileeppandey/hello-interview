# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersection(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return slow
        return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        intersect = self.getIntersection(head)
        if intersect is None:
            return None
        ptr1 = head
        ptr2 = intersect

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
