"""
https://leetcode.com/problems/linked-list-cycle/

Given head, determine if the linked list has a cycle in it.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        FLOYD'S TORTOISE AND HARE:
        Use two pointers — slow (1 step) and fast (2 steps).
        If there's a cycle, fast eventually catches slow.
        If no cycle, fast reaches None.
        """
        # Step 1: Handle edge cases
        if head is None or head.next is None:
            return False

        # Step 2: Initialize slow and fast pointers
        slow = head
        fast = head

        # Step 3: Move pointers until they meet or fast reaches end
        while fast is not None and fast.next is not None:
            slow = slow.next        # Move slow by 1
            fast = fast.next.next   # Move fast by 2

            # Step 4: If they meet, there's a cycle
            if slow == fast:
                return True

        # Step 5: Fast reached end → no cycle
        return False
