# Subarray Average of Size K — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Given an array, find the average of every contiguous subarray of size K.

## 2. Key Insight (Fixed-Size Sliding Window)
Same pattern as Maximum Average Subarray: slide a window of size K across the array. For each position, compute average = window_sum / K.

## 3. Building the Solution
```
window_sum = 0, result = []

For i from 0 to n-1:
    window_sum += arr[i]
    If i >= K-1:
        result.append(window_sum / K)
        window_sum -= arr[i - K + 1]
```

## 4. Complexity
**Time**: O(n).
**Space**: O(n - K + 1) for results.
