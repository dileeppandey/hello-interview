# Permutation in String — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Return true if any permutation of s1 is a substring of s2.

## 2. Key Insight (Fixed-Size Sliding Window + Frequency Match)
A permutation of s1 has the same character frequencies. Slide a window of size len(s1) over s2 and compare frequency maps.

## 3. Building the Solution
```
s1_count = Counter(s1)
window_count = Counter(s2[:len(s1)])

If s1_count == window_count: return True

For i from len(s1) to len(s2)-1:
    Add s2[i] to window_count
    Remove s2[i - len(s1)] from window_count
    If s1_count == window_count: return True

Return False
```

**Optimization**: Instead of comparing full frequency maps, track how many characters have matching counts (`matches` counter).

## 4. Complexity
**Time**: O(n) where n = len(s2).
**Space**: O(1) — fixed alphabet size (26).
