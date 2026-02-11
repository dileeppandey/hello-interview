# Trie (Prefix Tree) — First-Principles Thinking Guide

## 1. Understanding the Problem
**Restate**: Design a data structure that supports efficient insert and search for strings.

## 2. Key Insight (Character-by-Character Tree)
Each node represents a character. A path from root to a marked node spells a word. This enables O(L) operations where L = word length, regardless of how many words are stored.

## 3. Operations

### Insert
```
insert(word):
    node = root
    For each char in word:
        If char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end = True
```

### Search
```
search(word):
    node = root
    For each char in word:
        If char not in node.children: return False
        node = node.children[char]
    Return node.is_end
```

## 4. Advantages Over Hash Sets
- Prefix queries (startsWith)
- Alphabetical ordering
- Memory sharing for common prefixes

## 5. Complexity
**Time**: O(L) per operation.
**Space**: O(total characters across all words).
