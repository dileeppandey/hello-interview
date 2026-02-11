# Equilibrium Point — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Find the position where the sum of elements to the left equals the sum to the right.

## 2. Key Insight
**Prefix sum**: Compute total sum. Scan left-to-right, maintaining a running left_sum. At each index, right_sum = total - left_sum - current_element. If left_sum == right_sum, that's the equilibrium point.

## 3. Building the Solution
```
total = sum(arr)
left_sum = 0

For each index i:
    right_sum = total - left_sum - arr[i]
    If left_sum == right_sum: return i
    left_sum += arr[i]

return -1
```

## 4. Complexity
**Time**: O(n) — two passes (one for total, one for scanning).
**Space**: O(1).
