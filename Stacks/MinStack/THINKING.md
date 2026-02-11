# Min Stack — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Build a stack with all normal operations, but also support `getMin()` in O(1) time.

**Inputs**: Sequence of push/pop/top/getMin operations.
**Output**: Correct return values for top() and getMin() at every point.
**Constraints**: All operations must be O(1).

**Why is this interesting?** A normal stack gives O(1) push/pop/top, but finding the minimum normally requires scanning all elements — O(n). We need to do better.

## 2. Building Intuition

**The core tension**: The minimum can change when we push (new value might be smaller) or pop (we might remove the current minimum). How do we track the minimum without scanning?

**Simpler version**: What if we only pushed and never popped? We'd just keep a running `min_so_far` variable. But popping breaks this — when we pop the minimum, what's the *previous* minimum?

**Key insight**: We need to remember not just the *current* minimum, but the **entire history of minimums**. What data structure stores a history that we add to and remove from in LIFO order? A stack!

## 3. Brute Force First

**Naive approach**: Store a single `min_value`. On push, update it. On pop, if we popped the minimum, scan the remaining stack to find the new minimum.

**Complexity**: push O(1), pop O(n), getMin O(1).

**Why insufficient?** Pop is O(n). The problem requires all operations to be O(1).

## 4. Identifying the Optimization

**Repeated work**: When we pop the minimum, we re-scan to find the next minimum. But we *already knew* the next minimum at the time we pushed the current one!

**Solution — auxiliary min stack**:
- Maintain a second stack (`min_stack`) in parallel
- On each push, also push `min(val, current_min)` onto min_stack
- On each pop, also pop from min_stack
- getMin() is just `min_stack[-1]`

**Why this works**: Each level of the min_stack records "what was the minimum when this many elements existed." When we pop, we revert to the previous minimum automatically.

## 5. Building the Solution Step-by-Step

```
push(val):
    stack.push(val)
    min_stack.push(min(val, min_stack.top()))

pop():
    stack.pop()
    min_stack.pop()

top():     return stack.top()
getMin():  return min_stack.top()
```

**Dry-run**: push(-2), push(0), push(-3), getMin, pop, top, getMin
```
push(-2): stack=[-2], min_stack=[-2]
push(0):  stack=[-2,0], min_stack=[-2,-2]
push(-3): stack=[-2,0,-3], min_stack=[-2,-2,-3]
getMin:   min_stack top = -3 ✓
pop:      stack=[-2,0], min_stack=[-2,-2]
top:      stack top = 0 ✓
getMin:   min_stack top = -2 ✓  ← minimum correctly reverted!
```

## 6. Complexity Analysis

**Time**: O(1) for all operations.
**Space**: O(n) — the min_stack doubles the space usage.

**Space optimization**: Instead of storing a min for every push, only push onto min_stack when the new value is ≤ current min. But this complicates the logic and the asymptotic space is still O(n).
