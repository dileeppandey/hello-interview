"""
Maximum of all subarrays of size k
https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k/0

Given an array and an integer K, find the maximum for each contiguous
subarray of size K.

Example: arr = [1, 2, 3, 1, 4, 5, 2, 3, 6], K = 3
Output:  [3, 3, 4, 5, 5, 5, 6]
"""
from collections import deque


def max_of_subarrays(arr: list[int], k: int) -> list[int]:
    # ------------------------------------------------------------------
    # MONOTONIC DEQUE INSIGHT:
    # Maintain a deque of indices in decreasing order of their values.
    # The front of the deque is always the index of the maximum in the
    # current window. When sliding the window:
    #   1. Remove front if it's out of the window
    #   2. Remove back elements smaller than the new element (they can
    #      never be the maximum while the new element is in the window)
    #   3. Add the new element's index to the back
    # ------------------------------------------------------------------

    result = []
    dq = deque()  # Stores indices, not values

    for i in range(len(arr)):
        # Step 1: Remove elements outside the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Step 2: Remove smaller elements from the back
        #         (they'll never be the max while arr[i] is in the window)
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()

        # Step 3: Add current index
        dq.append(i)

        # Step 4: Once we've filled the first window, start recording maxes
        if i >= k - 1:
            result.append(arr[dq[0]])  # Front is always the max

    return result


# ---- Quick verification ----
print(max_of_subarrays([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
# Expected: [3, 3, 4, 5, 5, 5, 6]

print(max_of_subarrays([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4))
# Expected: [10, 10, 10, 15, 15, 90, 90]
