# Course Schedule — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Can we topologically order courses given prerequisites? Equivalently: does the prerequisite graph contain a cycle?

**Key insight**: This is a **cycle detection** problem on a **directed graph**.

## 2. Building Intuition

**Why directed graph?** "Must take B before A" is a directed edge B → A. If there's a cycle (A requires B, B requires C, C requires A), it's impossible.

**Two approaches**:
1. **DFS with 3-coloring** — detect back edges
2. **Kahn's algorithm (BFS)** — topological sort via in-degree counting

## 3. DFS 3-Coloring

**Colors**:
- **WHITE (0)**: Unvisited
- **GRAY (1)**: Currently in the DFS path (being explored)
- **BLACK (2)**: Fully explored (all descendants processed)

**Cycle detection**: If DFS hits a GRAY node, we've found a back edge → cycle!

## 4. Building the Solution Step-by-Step

```
Build adjacency list from prerequisites
color = [WHITE] * numCourses

DFS(node):
    If GRAY → cycle! return True
    If BLACK → already done, return False
    Mark GRAY
    For each neighbor: if DFS(neighbor) → cycle
    Mark BLACK
    return False

For each course: if DFS(course) → return False
return True
```

**Dry-run**: `prerequisites = [[1,0], [0,1]]`
```
Graph: 0→1, 1→0
DFS(0): color[0]=GRAY, visit 1
  DFS(1): color[1]=GRAY, visit 0
    DFS(0): color[0]==GRAY → CYCLE! → False ✓
```

## 5. Complexity Analysis

**Time**: O(V + E) — visit each node and edge once.
**Space**: O(V + E) — adjacency list + color array + recursion stack.
