# Longest Substring Without Repeating — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Find the length of the longest substring where all characters are unique.

## 2. Key Insight (Sliding Window)
Use a window [left, right]. Expand right. When a duplicate is found, shrink left past the previous occurrence of that character.

**Hash map optimization**: Store the last index of each character to jump `left` directly.

## 3. Building the Solution
```
char_index = {}
left = 0, max_len = 0

For right in range(len(s)):
    If s[right] in char_index and char_index[s[right]] >= left:
        left = char_index[s[right]] + 1
    char_index[s[right]] = right
    max_len = max(max_len, right - left + 1)
```

## 4. Complexity
**Time**: O(n) — each character visited once.
**Space**: O(min(n, alphabet_size)) — hash map for character positions.
