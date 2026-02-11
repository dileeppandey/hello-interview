# Moving Average from Data Stream — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Given a stream of integers and window size, calculate the moving average of the last k elements.

## 2. Key Insight (Queue + Running Sum)
Use a queue of size k. When a new value arrives: if full, dequeue the oldest and subtract from sum, then enqueue new and add to sum. Average = sum / queue size.

## 3. Building the Solution
```
init: queue = deque(), current_sum = 0, max_size = k

next(val):
    If len(queue) == max_size:
        current_sum -= queue.popleft()
    queue.append(val)
    current_sum += val
    Return current_sum / len(queue)
```

## 4. Complexity
**Time**: O(1) per call.
**Space**: O(k) — queue.
