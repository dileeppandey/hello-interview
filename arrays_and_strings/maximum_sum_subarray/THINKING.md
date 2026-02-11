# Maximum Sum Subarray (Kadane's) — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Find the contiguous subarray with the largest sum.

## 2. Key Insight (Kadane's Algorithm)
At each position, decide: **extend** the current subarray or **start fresh**?

`max_ending_here = max(nums[i], max_ending_here + nums[i])`

If adding the current element makes the running sum negative, it's better to start a new subarray from the current element.

## 3. Building the Solution
```
max_overall = -infinity
max_ending_here = 0

For each element:
    max_ending_here += element
    max_overall = max(max_overall, max_ending_here)
    If max_ending_here < 0: reset to 0, update start index
```

## 4. Complexity
**Time**: O(n) — single pass.
**Space**: O(1) — only tracking sums and indices.
