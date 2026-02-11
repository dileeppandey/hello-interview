# Word Search II — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: Find all words from a dictionary that can be spelled by traversing adjacent cells on a grid (each cell used at most once per word).

## 2. Building Intuition

**Naive per-word search**: For each word, run a separate DFS → O(words × m × n × 4^L). Very slow for many words.

**Key insight**: Multiple words share prefixes ("oath" and "oat" share "oat"). A **Trie** lets us search for all words simultaneously during one DFS traversal.

## 3. The Trie Advantage

Without Trie: Check each word independently → redundant traversals.
With Trie: One DFS traversal checks ALL words at once by following Trie branches.

**Pruning**: If the current path doesn't match any Trie prefix → stop exploring.

## 4. Building the Solution

```
1. Build Trie from all words
2. DFS from every cell:
    - If char not in Trie children → prune
    - If found a word → add to results
    - Mark cell visited, explore neighbors, backtrack
3. Optimization: remove empty Trie branches after finding words
```

## 5. Complexity

**Time**: O(m × n × 4^L) where L = max word length (worst case, but pruning makes it much faster in practice).
**Space**: O(sum of all word lengths) for the Trie + O(L) recursion stack.
