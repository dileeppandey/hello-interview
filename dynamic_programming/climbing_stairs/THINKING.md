# Climbing Stairs — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Count the number of distinct paths from step 0 to step n, where each move goes up 1 or 2 steps.

**Base cases**: `n=1` → 1 way. `n=2` → 2 ways (1+1 or 2).

## 2. Building Intuition

**What category?** This is a **counting paths** problem. At each step, I have a choice (1 or 2). The number of choices compounds.

**Recursive structure**: To reach step `n`, I must have been at step `n-1` or step `n-2`. So: `ways(n) = ways(n-1) + ways(n-2)`. This is the Fibonacci recurrence!

## 3. Brute Force First

**Naive recursion**: Directly compute `ways(n) = ways(n-1) + ways(n-2)`.

**Complexity**: O(2^n) — the recursion tree branches at every call. Massive redundant computation.

## 4. Identifying the Optimization

**Overlapping subproblems**: `ways(5)` calls `ways(4)` and `ways(3)`. But `ways(4)` also calls `ways(3)`. The same subproblem is solved many times.

**Two DP approaches**:
1. **Top-down (memoization)**: Cache results → O(n) time, O(n) space
2. **Bottom-up (tabulation)**: Build from base cases → O(n) time, O(1) space

Since we only need the last two values, we optimize to O(1) space.

## 5. Building the Solution Step-by-Step

```
prev2 = 1  (ways to reach step 1)
prev1 = 2  (ways to reach step 2)

For i = 3 to n:
    current = prev1 + prev2
    prev2 = prev1
    prev1 = current

return prev1
```

**Dry-run**: `n = 5`
```
i=3: current=2+1=3, prev2=2, prev1=3
i=4: current=3+2=5, prev2=3, prev1=5
i=5: current=5+3=8, prev2=5, prev1=8
Result: 8 ✓ (1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1, 1+2+2, 2+1+2, 2+2+1)
```

## 6. Complexity Analysis

**Time**: O(n) — single loop.
**Space**: O(1) — only two variables.
