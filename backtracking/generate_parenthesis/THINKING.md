# Generate Parentheses — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Given n, generate all valid combinations of n pairs of parentheses.

## 2. Key Insight (Constrained Backtracking)
At each position, we can add `(` if we haven't used all n, and `)` if the count of `)` is less than `(`. These constraints guarantee validity.

## 3. Building the Solution
```
backtrack(current, open_count, close_count):
    If len(current) == 2n: add to result
    If open_count < n: backtrack(current + "(", open_count + 1, close_count)
    If close_count < open_count: backtrack(current + ")", open_count, close_count + 1)
```

## 4. Complexity
**Time**: O(4ⁿ / √n) — Catalan number of valid sequences.
**Space**: O(n) — recursion depth.
