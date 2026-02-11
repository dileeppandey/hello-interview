"""
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.
Example: 1→2→3→4→5→NULL becomes 5→4→3→2→1→NULL
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        THREE-POINTER APPROACH:
        Walk through the list, reversing each node's pointer to point
        backward instead of forward.
        """
        # Step 1: Initialize two pointers
        #   current = node we're processing
        #   new_head (prev) = the reversed portion so far (starts as None)
        current = head
        new_head = None

        while current is not None:
            # Step 2: Save the next node (we're about to overwrite the pointer)
            temp = current.next

            # Step 3: Reverse the pointer — current now points backward
            current.next = new_head

            # Step 4: Advance: new_head moves to current, current moves forward
            new_head = current
            current = temp

        # Step 5: new_head is now the head of the fully reversed list
        return new_head


# ---- Quick verification ----
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(to_list(s.reverseList(head)))  # Expected: [5, 4, 3, 2, 1]
print(to_list(s.reverseList(None)))  # Expected: []