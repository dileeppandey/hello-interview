# 4Sum II — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Four arrays, each of length n. Count how many 4-tuples (one element from each array) sum to zero.

**Inputs**: Four integer arrays of equal length.
**Output**: Integer count of valid tuples.

## 2. Building Intuition

**What category?** This is a "meet in the middle" problem — split the work into two halves and combine.

**Key observation**: `a + b + c + d = 0` means `a + b = -(c + d)`. If we precompute all possible `a + b` sums, then for each `c + d` sum, we just look up how many `a + b` sums equal its negation.

## 3. Brute Force First

**Naive**: Four nested loops → O(n⁴). For `n = 500`, that's ~62 billion operations.

## 4. Identifying the Optimization

**Split into two halves**:
- Half 1: All `a + b` sums → O(n²) sums, stored in a hash map with counts
- Half 2: For each `c + d` sum, look up `-(c+d)` in the hash map → O(n²) lookups

**Total**: O(n²) time + O(n²) space.

**This is the "Meet in the Middle" paradigm**: reduce exponential to its square root by splitting the problem, solving each half independently, and combining via hash lookup.

## 5. Building the Solution Step-by-Step

```
sum_ab = Counter of all (a + b) values

count = 0
For each c in nums3, d in nums4:
    count += sum_ab[-(c + d)]

return count
```

**Dry-run**: `[1,2], [-2,-1], [-1,2], [0,2]`
```
sum_ab: {-1: 1, 0: 1, 0: +1=2, 1: 1} → {-1:1, 0:1, 1:1, 0:already counted}
Actually: 1+(-2)=-1, 1+(-1)=0, 2+(-2)=0, 2+(-1)=1 → {-1:1, 0:2, 1:1}

c=-1,d=0: need 1. sum_ab[1]=1. count=1
c=-1,d=2: need -1. sum_ab[-1]=1. count=2
c=2,d=0:  need -2. sum_ab[-2]=0. count=2
c=2,d=2:  need -4. sum_ab[-4]=0. count=2
Result: 2 ✓
```

## 6. Complexity Analysis

**Time**: O(n²) — two double loops.
**Space**: O(n²) — hash map of first-half sums.
