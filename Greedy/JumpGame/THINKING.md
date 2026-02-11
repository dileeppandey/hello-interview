# Jump Game — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: I'm standing at index 0 of an array. The value at each index tells me the *maximum* number of steps I can jump forward. Can I reach the last index?

**Inputs**: An integer array `nums` where `nums[i] >= 0`.
**Output**: Boolean — can I reach `nums[len(nums) - 1]`?
**Constraints**: `1 <= len(nums) <= 10^4`, `0 <= nums[i] <= 10^5`.

**Manual walkthrough**:
```
nums = [2, 3, 1, 1, 4]
Index 0: can jump up to 2 → reachable indices {0, 1, 2}
Index 1: can jump up to 3 → reachable indices {0, 1, 2, 3, 4} ← reached end!
```

## 2. Building Intuition

**What category?** This looks like a reachability/path problem. But the key insight is we don't need to find the *path*, just whether the destination is *reachable*.

**Simpler version**: What if all values were 1? Then we can always reach the end (step by step). What causes us to get stuck? A `0` — because we can't move forward from it. So the real question is: *can we always jump over every zero?*

**Key observation**: If I can reach index `i`, then I can reach every index from `i` to `i + nums[i]`. This means reachability is *monotonically expanding* — a greedy property.

## 3. Brute Force First

**Naive approach**: Try every possible jump from every reachable position (DFS/BFS). At each index, branch into `nums[i]` possible next positions.

**Complexity**: O(2^n) in the worst case — exponential due to branching.

**Why insufficient?** Way too slow for `n = 10^4`. We're doing redundant work: if I've already determined index 5 is reachable, I don't need to prove it again via a different path.

## 4. Identifying the Optimization

**Repeated work**: Multiple paths can reach the same index. We don't care *how* we got there.

**Key insight**: We only need to track a single number — the *farthest index reachable so far*. As we scan left to right:
- If `current_index > farthest`, we're stuck → return False
- Otherwise, update `farthest = max(farthest, i + nums[i])`

**Why greedy works**: Reachability is monotonic. If index `i` is reachable and `i + nums[i] = 7`, then indices 0 through 7 are all reachable. We never need to "undo" a reach.

## 5. Building the Solution Step-by-Step

```
Initialize farthest = 0

For each index i from 0 to n-1:
    If i > farthest:
        return False          ← Can't reach this index
    farthest = max(farthest, i + nums[i])
    If farthest >= n - 1:
        return True           ← Early exit

return True
```

**Dry-run**: `nums = [3, 2, 1, 0, 4]`
```
i=0: farthest = max(0, 0+3) = 3
i=1: farthest = max(3, 1+2) = 3
i=2: farthest = max(3, 2+1) = 3
i=3: farthest = max(3, 3+0) = 3   ← farthest stuck at 3, can't reach index 4
i=4: i(4) > farthest(3) → return False ✓
```

**Edge cases**:
- Single element `[0]` → already at last index → True
- All zeros `[0, 0, 0]` → stuck at index 0 → False
- Very large first value `[10, 0, 0, 0]` → True

## 6. Complexity Analysis

**Time**: O(n) — single pass through the array.
**Space**: O(1) — only one variable (`farthest`).

This is optimal because we must read every element at least once to decide reachability.
