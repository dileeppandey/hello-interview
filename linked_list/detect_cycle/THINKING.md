# Detect Cycle in Linked List — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Determine if a linked list has a cycle.

## 2. Key Insight (Floyd's Tortoise and Hare)
Use two pointers: slow (moves 1 step) and fast (moves 2 steps). If there's a cycle, fast will eventually meet slow inside the cycle. If no cycle, fast reaches null.

## 3. Building the Solution
```
slow = fast = head
While fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    If slow == fast: return True
Return False
```

**Why it works**: In a cycle, the gap between fast and slow decreases by 1 each step, so they must meet.

## 4. Complexity
**Time**: O(n).
**Space**: O(1).
