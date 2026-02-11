# Activity Selection — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: I have a set of activities, each with a start and end time. I can only do one activity at a time (no overlaps). I want to maximize the number of activities I can do.

**Inputs**: List of `(start, end)` tuples.
**Output**: Maximum subset of non-overlapping activities.
**Constraints**: Activities are non-negative time intervals.

**Manual walkthrough**:
```
Activities: (1,4), (3,5), (5,7), (8,11)
Pick (1,4) → next must start >= 4
Pick (5,7) → next must start >= 7
Pick (8,11) → done. Total = 3
```

## 2. Building Intuition

**What category?** Interval scheduling — a classic greedy problem.

**Simpler version**: What if I only had 2 activities? I'd pick whichever lets me "save more time" for future activities. That means picking the one that **finishes earliest**.

**Key observation**: The activity that ends earliest is always a safe first choice. It maximizes the remaining time for subsequent activities. This greedy choice can be applied repeatedly.

## 3. Brute Force First

**Naive approach**: Try all 2^n subsets of activities, check which ones are non-overlapping, return the largest valid subset.

**Complexity**: O(2^n) — exponential.

**Why insufficient?** Even for 20 activities, 2^20 = 1 million subsets. For larger inputs, completely impractical.

## 4. Identifying the Optimization

**Key insight — the Exchange Argument**: Suppose we have an optimal solution that does NOT start with the earliest-finishing activity. We can swap the first activity in that solution with the earliest-finishing one. Since the replacement finishes earlier (or at the same time), it can't conflict with any activity the original could accommodate. So we lose nothing — the greedy choice is at least as good.

**This is the formal proof that greedy works**: At every step, picking the earliest-finishing compatible activity leads to an optimal solution.

**Data structure**: Just sort by end time, then scan linearly.

## 5. Building the Solution Step-by-Step

```
1. Sort activities by end time
2. Select the first activity (earliest finish)
3. For each remaining activity:
     If its start >= last selected's end:
         Select it, update last_end
4. Return selected activities
```

**Dry-run**: `[(1,4), (3,5), (0,6), (5,7), (8,11), (12,16)]` (sorted by end)
```
Select (1,4), last_end=4
(3,5): 3 < 4 → skip
(0,6): 0 < 4 → skip
(5,7): 5 >= 4 → select, last_end=7
(8,11): 8 >= 7 → select, last_end=11
(12,16): 12 >= 11 → select, last_end=16
Result: 4 activities ✓
```

**Edge cases**:
- Single activity → always select it
- All overlapping → select 1 (the one finishing earliest)
- No overlaps → select all

## 6. Complexity Analysis

**Time**: O(n log n) for sorting + O(n) for scanning = **O(n log n)**.
**Space**: O(n) for the sorted copy (or O(1) if sorting in-place and only counting).

This is optimal — any algorithm must examine all intervals, and sorting is a known lower bound for comparison-based approaches.
