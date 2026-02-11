# First Missing Positive — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Given an unsorted array, find the smallest missing positive integer. Must run in O(n) time and O(1) extra space.

## 2. Key Insight
The answer must be in range [1, n+1]. We can use the array itself as a hash map by placing each number `i` at index `i-1`.

## 3. Building the Solution
```
For each index i:
    While nums[i] is in [1, n] and nums[i] != nums[nums[i]-1]:
        Swap nums[i] to its correct position

Scan array: first index where nums[i] != i+1 is the answer
If all match: answer is n+1
```

## 4. Complexity
**Time**: O(n) — each element swapped at most once.
**Space**: O(1) — in-place rearrangement.
