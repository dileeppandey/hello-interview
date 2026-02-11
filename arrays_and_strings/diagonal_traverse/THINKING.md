# Diagonal Traverse — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Return all elements of an M×N matrix in diagonal order, alternating direction: up-right for even diagonals, down-left for odd diagonals.

## 2. Building Intuition
**Pattern**: Elements on the same diagonal have the same sum of indices (i+j). Diagonal 0 has sum=0, diagonal 1 has sum=1, etc.

**Direction alternation**: Even diagonals go up-right (decreasing row), odd diagonals go down-left (increasing row).

## 3. Building the Solution
```
For each diagonal d from 0 to (rows + cols - 2):
    Collect all (i, j) where i + j == d
    If d is odd → traverse top-to-bottom (natural order)
    If d is even → traverse bottom-to-top (reversed)
```

**Alternative (BFS)**: Use a queue with level-by-level processing (like the existing solution). Each level is a diagonal; reverse odd-numbered levels.

## 4. Complexity
**Time**: O(m × n) — visit every element once.
**Space**: O(min(m, n)) — at most min(m,n) elements per diagonal.
