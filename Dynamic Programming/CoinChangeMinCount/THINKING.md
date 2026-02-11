# Coin Change — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Given coin denominations and a target amount, find the minimum number of coins needed. If impossible, return -1.

**Inputs**: `coins = [1, 2, 5]`, `amount = 11`.
**Output**: `3` (5 + 5 + 1).

## 2. Building Intuition

**What category?** This is an optimization (minimum) over choices → **Dynamic Programming**.

**Why not greedy?** Greedy (always take the largest coin) fails: coins `[1, 3, 4]`, amount `6`. Greedy: 4+1+1=3 coins. Optimal: 3+3=2 coins.

**Subproblem**: `dp(amount)` = minimum coins to make `amount`.

## 3. Brute Force First

**Naive recursion**: Try each coin, recurse on the remaining amount.
```
coinChange(amount) = 1 + min(coinChange(amount - coin)) for each coin
```
**Complexity**: O(S^n) where S = amount, n = number of coins — exponential.

## 4. Identifying the Optimization

**Overlapping subproblems**: `coinChange(11)` calls `coinChange(6)` (via coin 5), and `coinChange(9)` (via coin 2) also eventually calls `coinChange(6)`. Memoize!

**Recurrence**: `dp[a] = 1 + min(dp[a - coin])` for all coins where `coin <= a`.
**Base case**: `dp[0] = 0` (zero coins needed for amount 0).

## 5. Building the Solution Step-by-Step

**Dry-run**: `coins = [1, 2, 5], amount = 5`
```
dp[0]=0
dp[1]=min(dp[0]+1)=1
dp[2]=min(dp[1]+1, dp[0]+1)=1
dp[3]=min(dp[2]+1, dp[1]+1)=2
dp[4]=min(dp[3]+1, dp[2]+1)=2
dp[5]=min(dp[4]+1, dp[3]+1, dp[0]+1)=1
Result: 1 ✓ (just one 5-coin)
```

## 6. Complexity Analysis

**Time**: O(amount × len(coins)) — fill each cell, checking each coin.
**Space**: O(amount) — the dp table.
