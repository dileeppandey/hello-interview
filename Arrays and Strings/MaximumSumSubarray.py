"""
Kadane's Algorithm for Maximum Array Subsequence
https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
"""
from sys import maxsize


def max_subarray(scores):
    """
    # Given an array containing both negative and positive integers.
    # Find the contiguous sub-array with maximum sum.
    # Input: [2, 3, -5, 3, 4, -2, 0, -1, 5]
    # Output: [3, 4, -2, 0, -1, 5]
    """
    # start and end for indexes of the returned array, temp will capture intermediate
    # max subarray's start index
    start = end = temp = 0
    # max_till_here = sum + scores[current], max_overall = largest sum encountered
    max_overall = -maxsize - 1
    max_till_here = 0
    for i in range(0, len(scores)):
        max_till_here += scores[i]
        if max_overall < max_till_here:
            start = temp
            end = i
            max_overall = max_till_here
        if max_till_here < 0:
            temp = i + 1
            max_till_here = 0
    return (start, end, max_overall)


def main():
    """
    driver function
    """
    test_cases = int(input("No. of test cases: "))
    while test_cases > 0:
        scores = list(map(int, input().strip().split(" ")))
        print(max_subarray(scores))
        test_cases -= 1


main()
