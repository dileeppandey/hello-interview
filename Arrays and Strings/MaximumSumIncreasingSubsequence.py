"""
Maximum Sum Increasing Subsequence
https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence/0/?ref=self
"""


def maximum_sum_increasing_subsequence(numbers, size):
    """
    Given an array of n positive integers. Write a program to find the sum of
    maximum sum subsequence of the given array such that the integers in the 
    subsequence are sorted in increasing order.
    """
    results = [numbers[i] for i in range(size)]
    for i in range(1, size):
        for j in range(i):
            if numbers[i] > numbers[j] and results[i] < results[j] + numbers[i]:
                results[i] = results[j] + numbers[i]
    return max(results)


def main():
    """
    driver function
    """
    test_cases = int(input())
    while test_cases > 0:
        size = int(input())
        numbers = list(map(int, input().strip().split(" ")))
        print(maximum_sum_increasing_subsequence(numbers, size))
        test_cases -= 1


main()