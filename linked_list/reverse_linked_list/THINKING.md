# Reverse Linked List — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Reverse a singly linked list in-place.

## 2. Key Insight (Three Pointers)
Iterate through the list. At each node, reverse its `next` pointer to point to the previous node. Need three pointers: `prev`, `current`, `next_temp`.

## 3. Building the Solution
```
prev = None, current = head
While current:
    next_temp = current.next   ← save next
    current.next = prev        ← reverse pointer
    prev = current             ← advance prev
    current = next_temp        ← advance current
Return prev  ← new head
```

## 4. Complexity
**Time**: O(n).
**Space**: O(1).
