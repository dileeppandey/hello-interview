"""
https://leetcode.com/problems/merge-k-sorted-lists/

Merge k sorted linked lists and return it as one sorted list.

Example:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
"""
import heapq


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # ------------------------------------------------------------------
        # MIN-HEAP INSIGHT:
        # Maintain a heap of size k with one node from each list.
        # Repeatedly extract the minimum, add it to result, and push
        # that node's next into the heap.
        # ------------------------------------------------------------------

        # Step 1: Initialize heap with the head of each non-empty list
        #         Use (value, index) tuples — index breaks ties
        heap = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        # Step 2: Build the merged list using a dummy head
        dummy = ListNode(0)
        current = dummy

        while heap:
            # Step 3: Extract the smallest node
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            # Step 4: Push the next node from the same list (if exists)
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next


# ---- Quick verification ----
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

s = Solution()
lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6)),
]
print(to_list(s.mergeKLists(lists)))  # Expected: [1, 1, 2, 3, 4, 4, 5, 6]
print(to_list(s.mergeKLists([])))     # Expected: []
print(to_list(s.mergeKLists([None]))) # Expected: []
