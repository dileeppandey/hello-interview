# Add Two Numbers — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Two numbers are stored as reversed linked lists. Add them and return the result as a linked list.

## 2. Key Insight (Elementary Addition)
Simulate digit-by-digit addition with carry, just like manual addition. Process both lists simultaneously, creating result nodes.

## 3. Building the Solution
```
dummy = ListNode(0), carry = 0
While l1 or l2 or carry:
    val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
    carry = val // 10
    Create node with val % 10
    Advance l1, l2, current
Return dummy.next
```

## 4. Complexity
**Time**: O(max(m, n)).
**Space**: O(max(m, n)) — new list.
