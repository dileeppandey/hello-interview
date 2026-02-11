# BFS Graph Traversal — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Visit all reachable nodes from a source, level by level.

## 2. Key Insight (Queue)
BFS uses a FIFO queue. Enqueue the source, then repeatedly dequeue a node, process it, and enqueue its unvisited neighbors. This guarantees shortest-path ordering in unweighted graphs.

## 3. Building the Solution
```
queue = [source]
visited = {source}
level = {source: 0}

While queue not empty:
    node = dequeue
    For each neighbor of node:
        If neighbor not visited:
            visited.add(neighbor)
            level[neighbor] = level[node] + 1
            enqueue neighbor
```

## 4. Properties
- **Shortest path** in unweighted graphs
- **Level-order** traversal of trees
- **Time**: O(V + E), **Space**: O(V)
