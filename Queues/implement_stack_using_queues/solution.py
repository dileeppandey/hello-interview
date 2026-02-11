"""
https://leetcode.com/problems/implement-stack-using-queues/

Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support push, top, pop, and empty.

Key Insight: After each push, rotate the queue so the newest element
is at the front. This makes pop and top O(1) at the cost of O(n) push.
"""
from collections import deque


class MyStack:
    def __init__(self):
        # Step 1: We only need a single queue
        self.queue = deque()

    def push(self, x: int) -> None:
        # Step 2: Add the new element to the back of the queue
        self.queue.append(x)

        # Step 3: Rotate all previous elements behind the new one
        #         This puts the newest element at the front (LIFO order)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        # Step 4: The front of the queue is the "top" of the stack
        return self.queue.popleft()

    def top(self) -> int:
        # Step 5: Peek at the front
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# ---- Quick verification ----
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())    # Expected: 2
print(stack.pop())    # Expected: 2
print(stack.empty())  # Expected: False
print(stack.pop())    # Expected: 1
print(stack.empty())  # Expected: True
