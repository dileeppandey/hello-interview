"""
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum
element in constant time.

Operations:
  - push(val)  — Push element val onto stack
  - pop()      — Remove the element on top of the stack
  - top()      — Get the top element
  - getMin()   — Retrieve the minimum element in the stack (O(1))
"""


class MinStack:
    def __init__(self):
        # ------------------------------------------------------------------
        # KEY INSIGHT: Maintain TWO stacks in parallel:
        #   1. `stack`     — holds all values, normal stack behavior
        #   2. `min_stack` — holds the running minimum at each level
        #
        # When we push a value, we also push the current minimum onto
        # min_stack. When we pop, we pop from both. This way, getMin()
        # is always just peeking at the top of min_stack.
        # ------------------------------------------------------------------

        # Step 1: Initialize both stacks
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Step 2: Push the value onto the main stack
        self.stack.append(val)

        # Step 3: Push the new minimum onto the min stack
        #         If min_stack is empty, val is the minimum
        #         Otherwise, it's the smaller of val and the current min
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self) -> None:
        # Step 4: Pop from both stacks to keep them in sync
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Step 5: Return the top of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Step 6: The top of min_stack is always the current minimum — O(1)!
        return self.min_stack[-1]


# ---- Quick verification ----
ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print(ms.getMin())   # Expected: -3
ms.pop()
print(ms.top())      # Expected: 0
print(ms.getMin())   # Expected: -2
