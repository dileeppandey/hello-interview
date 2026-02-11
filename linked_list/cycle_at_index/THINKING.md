# Find Cycle Start (Linked List Cycle II) — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Find the node where a cycle begins in a linked list.

## 2. Key Insight (Floyd's Algorithm — Phase 2)
**Phase 1**: Use slow/fast to detect cycle (meeting point inside cycle).
**Phase 2**: Place one pointer at head, keep other at meeting point. Advance both by 1 step. They meet at the cycle start.

**Mathematical proof**: Let the distance from head to cycle start = a, cycle start to meeting point = b, remaining cycle = c. At meeting: slow traveled a+b, fast traveled a+b+b+c = a+2b+c. Since fast = 2×slow: a+2b+c = 2(a+b), so c = a. Therefore, moving from head and meeting point at equal speed converges at cycle start.

## 3. Building the Solution
```
Phase 1: Find meeting point (slow/fast)
Phase 2: ptr1 = head, ptr2 = meeting_point
While ptr1 != ptr2:
    ptr1 = ptr1.next
    ptr2 = ptr2.next
Return ptr1
```

## 4. Complexity
**Time**: O(n).
**Space**: O(1).
