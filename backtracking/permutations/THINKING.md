# Permutations — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Given n distinct numbers, generate all n! orderings.

## 2. Building Intuition

**Decision tree**: At position 0, we have n choices. At position 1, n-1 choices. At position 2, n-2 choices... This branching structure is a tree — and we need to explore every path.

**Backtracking template**: CHOOSE → EXPLORE → UNCHOOSE. Make a choice, recurse, undo the choice, try the next one.

## 3. Building the Solution

```
backtrack(current, remaining):
    If remaining is empty:
        Add current to result
        return
    For each number in remaining:
        current.append(number)         ← CHOOSE
        backtrack(current, remaining - number)  ← EXPLORE
        current.pop()                  ← UNCHOOSE
```

## 4. Complexity

**Time**: O(n · n!) — n! permutations, each takes O(n) to copy.
**Space**: O(n) recursion depth + O(n · n!) to store results.
