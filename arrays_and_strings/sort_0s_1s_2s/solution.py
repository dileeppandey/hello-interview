"""
Sort an array of 0s, 1s and 2s
https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0/?ref=self
"""


def sort_0_1_2s(numbers):
    """
    Write a program to sort an array of 0's,1's and 2's in ascending order.
    """
    count_zeros = count_ones = count_twos = 0
    for number in numbers:
        if number == 0:
            count_zeros += 1
        elif number == 1:
            count_ones += 1
        elif number == 2:
            count_twos += 1
    return (count_zeros, count_ones, count_twos)


def main():
    """
    driver function
    """
    test_cases = int(input())
    while test_cases > 0:
        size = int(input())
        numbers = list(map(int, input().strip().split(" ")))
        (count_zeros, count_ones, count_twos) = sort_0_1_2s(numbers)
        counter = count_zeros + count_ones + count_twos
        i = 0
        while i < counter:
            if i < count_zeros:
                print(0, end=" ")
            elif i < count_zeros + count_ones:
                print(1, end=" ")
            else:
                print(2, end=" ")
            i += 1

        test_cases -= 1
        print("")


main()
