# 4Sum — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Find all unique quadruplets that sum to a target.

## 2. Key Insight (Reduce to 2Sum)
Sort first. Fix two elements with nested loops, then use two-pointer technique for the remaining pair. Skip duplicates at each level.

Generalization: nSum reduces to (n-1)Sum recursively, bottoming out at 2Sum with two pointers.

## 3. Building the Solution
```
Sort nums
For i in range(len(nums)):
    For j in range(i+1, len(nums)):
        Use two pointers (left=j+1, right=end) to find pairs
        Skip duplicates at all three levels
```

## 4. Complexity
**Time**: O(n³) — two loops × two-pointer scan.
**Space**: O(1) extra (excluding result).
