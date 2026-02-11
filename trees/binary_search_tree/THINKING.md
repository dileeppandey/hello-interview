# Binary Search Tree — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Implement a BST supporting insert and search operations.

## 2. Key Insight (Sorted Structure)
BST invariant: for every node, all left descendants < node < all right descendants. This enables O(h) search by comparing the target with the current node and going left or right.

## 3. Operations

### Search
```
search(node, val):
    If node is None: return False
    If val == node.val: return True
    If val < node.val: search(node.left, val)
    Else: search(node.right, val)
```

### Insert
```
insert(node, val):
    If node is None: return TreeNode(val)
    If val < node.val: node.left = insert(node.left, val)
    Else: node.right = insert(node.right, val)
    Return node
```

## 4. Complexity
**Time**: O(h) per operation — O(log n) balanced, O(n) worst case (skewed).
**Space**: O(h) — recursion stack.
