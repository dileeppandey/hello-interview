# Python

## Collections

Functions to work with different collections

### Stack

Lists in python can act as a stack.

`stack = []`

| Operation | Function | Description |
| --------- | -------- | ----------- |
| PUSH | `append(item)`| Adds element to the top of stack |
| POP |  `pop()`| Removes and returns last element of stack |
| TOP |  `len(stack) - 1` | Points to last element of the stack |
| PEEK | `stack[-1]`|  Look at the last element of the stack |


### Queue

Python provides Queue class in collections library for working with Queue.

`from collections import queue`

`Q = queue.Queue(maxsize=0)` // Q is a FIFO Queue

`lifo_Q = queue.LifoQueue()` // lifo_Q is a LIFO Queue

`PQ = queue.PriorityQueue()` // Uses heapq module to maintain priority of elements


| Operation | Function | Description |
| --------- | -------- | ----------- |
| SIZE | `Q.qsize()` | Return the approximate size of the queue. |
| EMPTY | `Q.empty()` | Return True if the queue is empty, False otherwise.|
| FULL | `Q.full()` | Return True if the queue is full, False otherwise.|
| PUT | `Q.put(item)` | Put item into the queue|
| GET | `Q.get()` | Remove and return item from the queue.|


k### Priority Queue using `heap`

To create a list, use a list initialized to `[]`, or call `heapify` on a list to transform it into a heap.

`from collections import heapq`

| Operation | Function | Description |
| --------- | -------- | ----------- |
| PUSH | `heapq.heappush(heap, item)` | Push the value item onto the heap, maintaining the heap invariant. |
| POP |  `heapq.heappop(heap)` | Pop and return the smallest element from the heap, maintaining the heap invariant. |
| PEEK | | Access smallest element using `heap[0]` |
| N SMALLEST | `heapq.nsmallest(n, iterable[, key])` | Return a list with the n smallest elements from the dataset defined by iterable.  |
| N LARGEST | `heapq.nlargest(n, iterable[, key])` | Return a list with the n largest elements from the dataset defined by iterable. |
| PUSHPOP | `heapq.pushpop(heap, item)`  | Push item to the heap, then pop and return the smallest item. More efficient than  heappush() followed by heappop(). || HEAPIFY |  `heapq.heapify(x)`   | Transform list x into a heap, in-place and in linear time. |
| HEAPREPLACE | `heapq.heapreplace(heap, item)` | Pop and return the smallest item from the heap and also push the new item. Heap size unchanged. `IndexError` if heap is empty |

### Deque

Deques are generalization of stacks and queues. Supports memory efficient approximately O(1) pop and append at both ends.

`collections.deque([iterable[, maxlen]])`

Returns a new deque object initialized left-to-right (using `append()`) with data from iterable. If iterable is not specified, the new deque is empty.

If `maxlen` is specified, the deque is bounded. If a new items is added in a bounded deque which is full at the moment, a corresponding number of items are removed from the other end.

| Operation | Function | Description |
| --------- | -------- | ----------- |
| APPEND | `append(x)` | Add x to the right side of the deque. |
| APPENDLEFT | `appendleft(x)` | Add x to left side of the deque |
| POP | `pop()` | Remove and return an element from the right side of the deque. If no elements are present, raises an `IndexError`.|
| POPLEFT | `popleft()` | Remove and return an element from the left side of the deque. If no elements are present, raises an `IndexError`. |
| CLEAR | `clear()` | Remove all elements of deque, leaving it with length = 0 |
| COUNT | `count(x)` | Count the number of elements in deque with value x |

## String

| Operation | Function | Description |
| --------- | -------- | ----------- |
| START WITH | `str1.startswith(str2)` | Return `True` if `str1` starts with `str2`, else `False` |
