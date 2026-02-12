# Design an LRU Cache

## Problem Statement
Design a data structure for a Least Recently Used (LRU) cache. It should support two operations: `get` and `put`.

- `get(key)`: Get the value of the key if the key exists in the cache, otherwise return -1.
- `put(key, value)`: Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

Both operations must run in **O(1)** time complexity.

## Requirements

### Functional
- **Capacity Management**: Fixed maximum number of items.
- **Eviction Policy**: Remove the least recently used item when full.
- **Fast Access**: O(1) time complexity for both `get` and `put`.

## Key Components
- **Hash Map**: Provides O(1) lookup for keys.
- **Doubly Linked List**: Maintains the order of usage. The most recently used item is at the head, and the least recently used is at the tail.

## Data Model
- **Node**: contains `key`, `value`, `prev`, `next`.
- **LRUCache**: contains `capacity`, `hash_map`, `head`, `tail`.

## High-Level Workflow
1. **get(key)**:
    - If key in hash map:
        - Move the corresponding node to the head of the list.
        - Return the value.
    - Else, return -1.
2. **put(key, value)**:
    - If key in hash map:
        - Update value and move node to head.
    - Else:
        - Add new node to head and hash map.
        - If capacity exceeded, remove tail node and its key from hash map.
