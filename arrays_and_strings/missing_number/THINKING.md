# Missing Number in Array — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Array of size n-1 contains numbers 1 to n with one missing. Find it.

## 2. Key Insight (Math)
Expected sum of 1..n = n(n+1)/2. Actual sum = sum of array. Missing = expected - actual.

**Alternative**: XOR all numbers 1..n with all array elements. Result is the missing number (all pairs cancel out).

## 3. Building the Solution
```
return n * (n + 1) // 2 - sum(array)
```

## 4. Complexity
**Time**: O(n).
**Space**: O(1).
