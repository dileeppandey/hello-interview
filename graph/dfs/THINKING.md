# DFS Graph Traversal — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Explore a graph by going as deep as possible before backtracking.

## 2. Key Insight (Recursion/Stack)
DFS uses implicit recursion (or explicit stack). Visit a node, mark it, recurse into each unvisited neighbor. Edge classification (tree, back, forward, cross) helps detect cycles and compute topological order.

## 3. Building the Solution
```
dfs_visit(node):
    start_time[node] = ++time
    For each neighbor:
        If not visited: dfs_visit(neighbor)  → tree edge
        Elif not finished: → back edge (cycle!)
        Elif start_time[node] < start_time[neighbor]: → forward edge
        Else: → cross edge
    finish_time[node] = ++time
```

## 4. Edge Classification
- **Tree edge**: new discovery
- **Back edge**: ancestor (cycle indicator)
- **Forward edge**: descendant (non-tree)
- **Cross edge**: between unrelated branches

## 5. Properties
- **Topological sort**: reverse of finish order
- **Time**: O(V + E), **Space**: O(V)
