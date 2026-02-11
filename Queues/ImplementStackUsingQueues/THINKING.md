# Implement Stack Using Queues — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Simulate LIFO behavior using only FIFO operations.

**Core tension**: Queue gives us the *oldest* element first. Stack needs the *newest* first.

## 2. Building Intuition

**Key trick**: After pushing a new element to the back, rotate all other elements behind it. Now the newest element is at the front — achieving LIFO order.

**Trade-off**: Push becomes O(n) but pop/top become O(1). Alternatively, we could make push O(1) and pop O(n).

## 3. Building the Solution

```
push(x):
    queue.enqueue(x)
    Rotate (len-1) times: dequeue from front, enqueue to back

pop():   return queue.dequeue()
top():   return queue.front()
```

**Dry-run**: push(1), push(2), pop
```
push(1): queue=[1]
push(2): queue=[1,2] → rotate 1: queue=[2,1]
pop():   dequeue → 2 ✓ (LIFO!)
```

## 4. Complexity

**Push**: O(n), **Pop/Top**: O(1), **Space**: O(n).
