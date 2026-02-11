# Design Circular Queue — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Implement a fixed-size circular queue with enqueue, dequeue, front, rear, isEmpty, isFull.

## 2. Key Insight (Circular Array)
Use an array of size k with `front` and `rear` pointers. The circular part: `rear = (rear + 1) % k` wraps around to the beginning when the end is reached.

## 3. Building the Solution
```
init: array[k], front = -1, rear = -1, size = 0

enQueue(val):
    If full: return False
    rear = (rear + 1) % k
    array[rear] = val, size++

deQueue():
    If empty: return False
    front = (front + 1) % k, size--
```

## 4. Complexity
All operations: **O(1) time**, **O(k) space**.
