# Maximum Depth of Binary Tree — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Find the longest root-to-leaf path (counted in nodes).

## 2. Building Intuition

**Trees are recursive structures**: A tree is either empty or a node with two sub-trees. This naturally suggests recursion.

**Subproblem**: The max depth of a tree = 1 + max(depth of left subtree, depth of right subtree).

## 3. Base Case

**Empty tree** → depth 0. This stops the recursion.

## 4. Building the Solution

```
maxDepth(node):
    If node is None: return 0
    return 1 + max(maxDepth(node.left), maxDepth(node.right))
```

**Dry-run**:
```
      3
     / \
    9  20
      /  \
     15   7

maxDepth(3): 1 + max(maxDepth(9), maxDepth(20))
  maxDepth(9): 1 + max(0, 0) = 1
  maxDepth(20): 1 + max(maxDepth(15), maxDepth(7))
    maxDepth(15): 1 + max(0, 0) = 1
    maxDepth(7): 1 + max(0, 0) = 1
  maxDepth(20): 1 + max(1, 1) = 2
maxDepth(3): 1 + max(1, 2) = 3 ✓
```

## 5. Complexity Analysis

**Time**: O(n) — visit every node once.
**Space**: O(h) — recursion stack depth, where h = height. O(log n) for balanced, O(n) for skewed.
