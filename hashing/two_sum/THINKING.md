# Two Sum — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Given an array of numbers and a target, find two numbers that add up to the target. Return their indices.

**Inputs**: Integer array `nums`, integer `target`.
**Output**: Two indices `[i, j]` where `nums[i] + nums[j] == target`.
**Constraints**: Exactly one solution exists. Can't use the same element twice.

**Manual walkthrough**:
```
nums = [2, 7, 11, 15], target = 9
Check each pair: 2+7=9 ✓ → return [0, 1]
```

## 2. Building Intuition

**What category?** This is a **lookup/search** problem. For each element, we need to find if its partner exists.

**Simpler version**: If the array were sorted, could I use two pointers? Yes — start pointers at both ends, move inward. But that loses the original indices.

**Key insight**: For each number `x`, I need to know if `target - x` exists *and where*. This is a **complement lookup** — exactly what hash maps excel at.

## 3. Brute Force First

**Naive approach**: Check every pair of elements.
```
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            return [i, j]
```

**Complexity**: O(n²) time, O(1) space.

**Why insufficient?** For `n = 10^4`, this is 50 million comparisons. We can do much better.

## 4. Identifying the Optimization

**Repeated work**: For each element, we're scanning the entire array to find its complement. But checking "does value X exist?" is exactly what hash maps do in O(1).

**The trade-off**: We spend O(n) space on a hash map to reduce time from O(n²) to O(n). This is the classic **space-time trade-off**.

**Single-pass trick**: We don't need to build the entire map first. As we iterate, we check if the complement is already in the map. If not, add the current element. This handles duplicates correctly — by the time we reach the second copy, the first is already stored.

## 5. Building the Solution Step-by-Step

```
seen = {}    ← maps value → index

For each index i, value num:
    complement = target - num
    If complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

**Dry-run**: `nums = [3, 2, 4], target = 6`
```
i=0, num=3: complement=3, not in {}. seen={3:0}
i=1, num=2: complement=4, not in {3:0}. seen={3:0, 2:1}
i=2, num=4: complement=2, found in seen! Return [1, 2] ✓
```

**Edge cases**:
- Duplicate values: `[3, 3], target=6` → works because second 3 finds first 3 in map
- Negative numbers: `[-1, 2], target=1` → complement of -1 is 2, works normally

## 6. Complexity Analysis

**Time**: O(n) — single pass, O(1) hash map lookups.
**Space**: O(n) — hash map stores up to n elements.

This is optimal for time since we must read each element at least once.
