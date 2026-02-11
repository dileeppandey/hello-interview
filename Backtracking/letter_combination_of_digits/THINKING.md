# Letter Combinations of a Phone Number — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Map digits to their phone keyboard letters. Return all letter combinations for a digit string.

## 2. Key Insight (DFS/Backtracking)
Each digit maps to 3-4 letters. For each digit, try all its letters, then recurse for the next digit. This builds a tree of all combinations.

## 3. Building the Solution
```
mapping = {"2": "abc", "3": "def", ...}

backtrack(index, current):
    If index == len(digits): add current to result
    For each letter in mapping[digits[index]]:
        backtrack(index + 1, current + letter)
```

## 4. Complexity
**Time**: O(4ⁿ) — worst case 4 letters per digit.
**Space**: O(n) — recursion depth.
