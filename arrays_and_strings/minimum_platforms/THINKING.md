# Minimum Platforms — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Given arrival and departure times of trains, find the minimum platforms needed so no train waits.

## 2. Key Insight (Event Sorting)
Sort arrivals and departures separately. Do a merge-like scan: if next event is an arrival → need +1 platform. If departure → free -1 platform. Track the maximum.

## 3. Building the Solution
```
Sort arrival[] and departure[]
i = j = 0, platforms = 0, max_platforms = 0

While i < n:
    If arrival[i] <= departure[j]:
        platforms++, i++
    Else:
        platforms--, j++
    max_platforms = max(max_platforms, platforms)
```

## 4. Complexity
**Time**: O(n log n) — dominated by sorting.
**Space**: O(1) extra.
