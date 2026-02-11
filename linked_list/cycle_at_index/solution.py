"""
https://leetcode.com/problems/linked-list-cycle-ii/

Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return None.

Uses Floyd's Algorithm Phase 2: after detecting the meeting point,
a second pointer from head meets the cycle pointer at the cycle start.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersection(self, head):
        """Phase 1: Find the meeting point inside the cycle using slow/fast."""
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            # Step 1: Slow and fast meet inside the cycle
            if slow is fast:
                return slow
        return None  # No cycle

    def detectCycle(self, head):
        """
        Phase 2: Find where the cycle begins.

        MATH INSIGHT: If distance from head to cycle start = a,
        and cycle start to meeting point = b, then a = c (remaining cycle).
        So starting from head and meeting point simultaneously leads to
        convergence at the cycle start.
        """
        # Step 2: Get the meeting point from Phase 1
        intersect = self.getIntersection(head)
        if intersect is None:
            return None

        # Step 3: Two pointers — one from head, one from meeting point
        ptr1 = head
        ptr2 = intersect

        # Step 4: Advance both by 1 → they meet at cycle start
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
