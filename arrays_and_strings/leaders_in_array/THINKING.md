# Leaders in an Array — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: An element is a leader if it is greater than all elements to its right. The rightmost element is always a leader.

## 2. Key Insight (Scan Right-to-Left)
**Brute force**: For each element, check all elements to its right → O(n²).

**Optimized**: Scan from right to left, tracking the maximum so far. If current > max_from_right, it's a leader.

## 3. Building the Solution
```
max_from_right = arr[-1]
leaders = [max_from_right]

For i from n-2 down to 0:
    If arr[i] > max_from_right:
        leaders.append(arr[i])
        max_from_right = arr[i]

Reverse leaders (to maintain original order)
```

## 4. Complexity
**Time**: O(n) — single pass from right.
**Space**: O(k) — where k is the number of leaders.
