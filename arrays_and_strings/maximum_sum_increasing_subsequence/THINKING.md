# Maximum Sum Increasing Subsequence — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Find the maximum sum achievable by an increasing subsequence.

## 2. Key Insight (DP)
Similar to LIS but instead of counting length, track sum. `dp[i]` = maximum sum of an increasing subsequence ending at index i.

## 3. Building the Solution
```
dp = copy(arr)  # Each element starts as its own subsequence

For i from 1 to n-1:
    For j from 0 to i-1:
        If arr[j] < arr[i] and dp[j] + arr[i] > dp[i]:
            dp[i] = dp[j] + arr[i]

Return max(dp)
```

## 4. Complexity
**Time**: O(n²).
**Space**: O(n).
