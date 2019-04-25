"""
Subarray with given sum
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0/?ref=self
"""


def subarray_with_given_sum(numbers, size, required_sum):
    """
    Given an unsorted array of non-negative integers,
    find a continuous sub-array which adds to a given number.
    """
    start = 0
    current_sum = numbers[0]

    for i in range(1, size + 1):
        while current_sum > required_sum and start < i - 1:
            current_sum -= numbers[start]
            start += 1
        if current_sum == required_sum:
            return (start + 1, i)
        if i < size:
            current_sum += numbers[i]
    return -1


def main():
    """
    driver function
    """
    test_cases = int(input())
    while test_cases > 0:
        size, required_sum = list(map(int, input().strip().split(" ")))
        numbers = list(map(int, input().strip().split(" ")))
        res = subarray_with_given_sum(numbers, size, required_sum)
        if res == -1:
            print(res)
        else:
            print(res[0], res[1])
        test_cases -= 1

main()
