# Unique Characters in String — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Determine if a string has all unique characters.

## 2. Approaches (Increasing Optimization)
1. **Brute Force** O(n²): Compare every pair.
2. **Hash Set** O(n): Track seen characters, return False on duplicate.
3. **Boolean Array** O(n): For fixed alphabet (e.g., lowercase), use a 26-element array.
4. **Bit Vector** O(n): Use a single integer as a bitmask for 26 characters.

## 3. Building the Solution (Array approach)
```
seen = [False] * 26
For each char:
    index = ord(char) - ord('a')
    If seen[index]: return False
    seen[index] = True
Return True
```

## 4. Complexity
**Time**: O(n) (or O(1) if alphabet is fixed — max 26 iterations).
**Space**: O(1) — fixed-size array.
