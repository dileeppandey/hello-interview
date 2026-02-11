# Pow(x, n) — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Compute `x^n` efficiently. `n` can be negative.

## 2. Building Intuition

**Brute force**: Multiply x by itself n times → O(n).

**Key insight (binary exponentiation)**: `x^10 = (x^5)^2 = (x * (x^2)^2)^2`. Each step halves the exponent → O(log n).

**This is divide and conquer**: Split the problem in half, solve the half, combine by squaring.

## 3. Building the Solution

```
If n < 0: x = 1/x, n = -n     ← handle negative

fast_pow(base, exp):
    If exp == 0: return 1
    half = fast_pow(base, exp // 2)
    If exp is even: return half * half
    If exp is odd:  return half * half * base
```

## 4. Complexity

**Time**: O(log n) — halving the exponent each step.
**Space**: O(log n) — recursion stack depth.
