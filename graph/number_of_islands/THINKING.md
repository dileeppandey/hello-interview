# Number of Islands — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Count connected components of `'1'`s in a 2D grid, where connectivity is horizontal/vertical (not diagonal).

**This is a graph problem in disguise**: Each cell is a node. Edges connect adjacent `'1'` cells. "Number of islands" = number of connected components.

## 2. Building Intuition

**How do we count connected components?** Start from any unvisited `'1'`, explore the entire component (DFS/BFS), mark it visited, increment count. Repeat until no unvisited `'1'`s remain.

**Grid as implicit graph**: We don't need to build an adjacency list. The grid itself defines neighbors: up/down/left/right.

## 3. Brute Force First

There's no simpler approach than DFS/BFS for connected components. The key decision is DFS vs BFS (both work), and whether to use a separate `visited` set or modify the grid in-place.

**In-place trick**: Instead of maintaining a separate visited set, simply change `'1'` to `'0'` when visiting. This "sinks" the island.

## 4. Building the Solution Step-by-Step

```
count = 0
For each cell (r, c):
    If grid[r][c] == '1':
        count += 1
        DFS(r, c)  → marks all connected '1's as '0'
return count
```

**DFS helper**:
```
DFS(r, c):
    If out of bounds or grid[r][c] == '0': return
    grid[r][c] = '0'  ← mark visited
    DFS(r±1, c), DFS(r, c±1)  ← explore 4 directions
```

## 5. Complexity Analysis

**Time**: O(m × n) — each cell visited at most once.
**Space**: O(m × n) worst case for recursion stack (e.g., grid is all `'1'`s, DFS depth = m×n). BFS variant uses O(min(m, n)) queue space.
