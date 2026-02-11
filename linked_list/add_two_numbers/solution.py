"""
https://leetcode.com/problems/add-two-numbers/

Two non-negative integers are stored as reversed linked lists. Each node
contains a single digit. Add the two numbers and return the sum as a
linked list.

Example: (2→4→3) + (5→6→4) = 7→0→8  (342 + 465 = 807)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        ELEMENTARY ADDITION WITH CARRY:
        Process digits from both lists simultaneously, carrying over
        values >= 10—just like manual addition.
        """
        # Step 1: Initialize pointers and a dummy head for the result
        c1, c2 = l1, l2
        res = ListNode(0)  # Dummy head simplifies edge cases
        current = res
        carry = 0

        # Step 2: Process both lists digit by digit
        while c1 is not None or c2 is not None:
            # Get values (0 if one list is shorter)
            v1 = 0 if c1 is None else c1.val
            v2 = 0 if c2 is None else c2.val

            # Step 3: Compute digit sum + carry
            total = v1 + v2 + carry
            carry = total // 10           # Carry for next digit
            current.next = ListNode(total % 10)  # Current digit

            # Step 4: Advance all pointers
            if c1 is not None:
                c1 = c1.next
            if c2 is not None:
                c2 = c2.next
            current = current.next

        # Step 5: Don't forget a final carry (e.g., 99 + 1 = 100)
        if carry > 0:
            current.next = ListNode(carry)

        # Step 6: Return the result (skip the dummy head)
        return res.next
