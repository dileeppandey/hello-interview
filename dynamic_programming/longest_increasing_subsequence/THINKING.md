# Longest Increasing Subsequence — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Find the longest subsequence (not necessarily contiguous) where each element is strictly greater than the previous.

**Key distinction**: *Subsequence* ≠ *subarray*. Elements don't need to be adjacent, just in the original order.

## 2. Building Intuition

**What category?** Optimization over subsequences → **Dynamic Programming**.

**Why DP?** At each element, we make a choice: include it in the LIS or skip it. The optimal choice depends on what came before — this is optimal substructure with overlapping subproblems.

**Subproblem**: `dp[i]` = length of the longest increasing subsequence *ending at* index `i`.

## 3. Brute Force First

**Naive**: Generate all 2^n subsequences, check each for being increasing, return max length.

**Complexity**: O(2^n · n) — totally impractical.

## 4. Identifying the Optimization

**Recurrence**: For each `i`, look at all `j < i`. If `nums[j] < nums[i]`, we can extend the LIS ending at `j`: `dp[i] = max(dp[j] + 1)` for all valid `j`.

**Base case**: `dp[i] = 1` for all `i` (each element alone is an LIS of length 1).

**Answer**: `max(dp)` — the LIS can end anywhere.

## 5. Building the Solution Step-by-Step

**Dry-run**: `[10, 9, 2, 5, 3, 7, 101, 18]`
```
dp starts: [1, 1, 1, 1, 1, 1, 1, 1]

i=1 (9):  no j where nums[j]<9 in valid range except none → dp[1]=1
i=2 (2):  no j where nums[j]<2 → dp[2]=1
i=3 (5):  j=2: nums[2]=2<5 → dp[3]=max(1, 1+1)=2
i=4 (3):  j=2: nums[2]=2<3 → dp[4]=max(1, 1+1)=2
i=5 (7):  j=2: 2<7→dp=2, j=3: 5<7→dp=max(2,2+1)=3, j=4: 3<7→dp=max(3,2+1)=3
i=6 (101): best from j=5 → dp[6]=3+1=4
i=7 (18): best from j=5 → dp[7]=3+1=4

dp = [1, 1, 1, 2, 2, 3, 4, 4] → max = 4 ✓
```

## 6. Complexity Analysis

**Time**: O(n²) — double loop.
**Space**: O(n) — dp array.

**Note**: An O(n log n) solution exists using patience sorting (binary search on a "tails" array), but the O(n²) approach is clearer for learning.
