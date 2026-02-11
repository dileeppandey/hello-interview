"""
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Example: list1 = [1,2,4], list2 = [1,3,4] → [1,1,2,3,4,4]
"""


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # ------------------------------------------------------------------
        # TWO-POINTER MERGE INSIGHT: Use a dummy head to avoid edge cases.
        # Compare current nodes of both lists, append the smaller one.
        # When one list is exhausted, append the remainder of the other.
        # ------------------------------------------------------------------

        # Step 1: Create a dummy node to serve as the head of merged list
        #         This avoids special-casing the first node
        dummy = ListNode(-1)
        current = dummy

        # Step 2: Compare and append the smaller node from each list
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Step 3: Append the remaining nodes (one list may still have elements)
        current.next = list1 if list1 else list2

        # Step 4: Return the merged list (skip the dummy head)
        return dummy.next


# ---- Quick verification ----
def to_list(node):
    """Helper to convert linked list to Python list for printing."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

s = Solution()
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
print(to_list(s.mergeTwoLists(l1, l2)))  # Expected: [1, 1, 2, 3, 4, 4]

print(to_list(s.mergeTwoLists(None, None)))  # Expected: []
print(to_list(s.mergeTwoLists(None, ListNode(0))))  # Expected: [0]
