# Designing an LRU Cache — First-Principles Thinking Guide

## 1. Understanding the Problem
**Goal**: Create a data structure that discards the least recently used items first when it reaches its capacity.

**Constraints**: O(1) time for both search and insertion/update.

## 2. Choosing the Right Data Structures
- **Why a Hash Map?**: We need O(1) lookup for `get(key)`.
- **Why a Doubly Linked List?**:
    - We need to maintain order of usage.
    - Moving a node to the front (most recently used) or removing a node from the back (least recently used) is O(1) *if* we have a pointer to the node.
    - A doubly linked list allows O(1) removal of any node once we have it.

## 3. Building the Solution
**The Map-List Link**: The hash map stores keys as keys, and the values are pointers to the corresponding nodes in the doubly linked list.

**The "MRU" (Most Recently Used) logic**:
- Every time a key is accessed (`get`) or updated (`put`), move its node to the "head".
- Every time a new key is added, check capacity. If full, remove the "tail" node.

## 4. Edge Cases to Handle
- **Cache Capacity = 1**: The head and tail are the same node.
- **Updating an existing key**: Ensure the value is updated *and* the node is moved to head.
- **Duplicate items**: The problem usually assumes unique keys.
