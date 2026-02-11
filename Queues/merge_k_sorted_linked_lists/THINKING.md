# Merge K Sorted Linked Lists — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Merge k sorted linked lists into one sorted list.

## 2. Key Insight (Min-Heap / Priority Queue)
Maintain a min-heap of size k containing one node from each list. Repeatedly extract the minimum, add it to the result, and push that node's next into the heap.

**Alternative**: Divide and conquer — merge lists pairwise, like merge sort.

## 3. Building the Solution (Heap)
```
heap = []
For each list head: push (head.val, list_index, head) into heap

dummy = ListNode(0), current = dummy
While heap:
    val, idx, node = heappop(heap)
    current.next = node
    current = current.next
    If node.next: heappush(heap, (node.next.val, idx, node.next))
Return dummy.next
```

## 4. Complexity
**Time**: O(N log k) — N total nodes, each heap operation is O(log k).
**Space**: O(k) — heap size.
