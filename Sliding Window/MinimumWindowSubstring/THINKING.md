# Minimum Window Substring — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Find the shortest substring of `s` that contains every character of `t` (with correct frequencies).

## 2. Building Intuition

**What category?** Variable-size sliding window. We need to find the smallest valid window, not a fixed-size one.

**Two-pointer pattern**:
- **Expand** right pointer to make the window valid
- **Shrink** left pointer to find the minimum valid window
- Track character frequencies to know when the window is "valid"

## 3. Brute Force

Check all O(n²) substrings, validate each in O(n) → O(n³). Far too slow.

## 4. Key Optimization

**Expand/shrink sliding window**: Instead of checking all substrings, maintain a window that we expand until valid, then shrink while still valid. We track:
- `required` — frequency map of t
- `window_counts` — frequency map of current window
- `formed` — how many unique chars have met their required count

## 5. Building the Solution

```
required = Counter(t)
left = 0, formed = 0

For right in range(len(s)):
    Add s[right] to window_counts
    If s[right] meets required count → formed++

    While formed == needed:
        Update min window if smaller
        Remove s[left] from window_counts
        If s[left] drops below required → formed--
        left++
```

## 6. Complexity

**Time**: O(|s| + |t|) — each character enters/exits the window at most once.
**Space**: O(|s| + |t|) — hash maps for character frequencies.
