# Maximum Average Subarray I — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Find the contiguous subarray of length k with the maximum average.

## 2. Key Insight (Fixed-Size Sliding Window)
Compute the sum of the first k elements. Slide the window: add the next element, subtract the element leaving the window. Track the maximum sum.

## 3. Building the Solution
```
window_sum = sum(nums[:k])
max_sum = window_sum

For i from k to n-1:
    window_sum += nums[i] - nums[i - k]
    max_sum = max(max_sum, window_sum)

Return max_sum / k
```

## 4. Complexity
**Time**: O(n) — single pass.
**Space**: O(1).
