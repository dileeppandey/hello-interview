# Subarray With Given Sum — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Find a contiguous subarray of non-negative integers that sums to a given target.

## 2. Key Insight (Sliding Window)
Since all elements are non-negative, adding an element increases the sum and removing from the left decreases it — perfect for a sliding window.

## 3. Building the Solution
```
left = 0, current_sum = 0

For right in range(n):
    current_sum += arr[right]
    While current_sum > target and left < right:
        current_sum -= arr[left]
        left++
    If current_sum == target:
        return (left, right)
```

## 4. Complexity
**Time**: O(n) — each element added/removed at most once.
**Space**: O(1).
