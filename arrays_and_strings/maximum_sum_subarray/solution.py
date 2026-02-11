"""
Kadane's Algorithm — Maximum Sum Contiguous Subarray
https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

Given an array containing both negative and positive integers,
find the contiguous sub-array with maximum sum.

Example: [2, 3, -5, 3, 4, -2, 0, -1, 5] → sum=9, subarray=[3, 4, -2, 0, -1, 5]
"""
from sys import maxsize


def max_subarray(scores):
    """
    KADANE'S ALGORITHM:
    At each position, decide: extend the current subarray or start fresh?
    If the running sum becomes negative, it's better to start over.
    """
    # Step 1: Initialize tracking variables
    start = end = temp = 0
    max_overall = -maxsize - 1  # Global maximum sum
    max_till_here = 0           # Current subarray sum

    for i in range(len(scores)):
        # Step 2: Extend the current subarray
        max_till_here += scores[i]

        # Step 3: Update global max if current sum is larger
        if max_overall < max_till_here:
            start = temp    # Update start of best subarray
            end = i         # Update end of best subarray
            max_overall = max_till_here

        # Step 4: If current sum drops negative, reset
        #         (starting fresh from next element is better)
        if max_till_here < 0:
            temp = i + 1    # Next potential start
            max_till_here = 0

    return (start, end, max_overall)


# ---- Quick verification ----
print(max_subarray([2, 3, -5, 3, 4, -2, 0, -1, 5]))
# Expected: (3, 8, 9)

print(max_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))
# Expected: (2, 6, 7)

print(max_subarray([-1, -2, -3]))
# Expected: (0, 0, -1)
