"""
Equilibrium Point
https://practice.geeksforgeeks.org/problems/equilibrium-point/0
"""


def equilibrium_point(numbers, size):
    """
    Given an array A your task is to tell at which position the equilibrium
    first occurs in the array. Equilibrium position in an array is a position
    such that the sum of elements below it is equal to the sum of elements 
    after it.
    """
    if size == 1:
        return 1
    i = 0
    j = size - 1
    left_sum = 0
    right_sum = 0
    while i < j:
        if left_sum < right_sum:
            left_sum += numbers[i]
            i += 1
        else:
            right_sum += numbers[j]
            j -= 1
    if left_sum == right_sum:
        return i + 1
    else:
        return -1



def main():
    """
    driver function
    """
    test_cases = int(input())
    while test_cases > 0:
        size = int(input())
        numbers = list(map(int, input().strip().split(" ")))
        print(equilibrium_point(numbers, size))
        test_cases -= 1

main()
