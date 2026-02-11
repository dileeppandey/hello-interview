"""
Missing number in array
https://practice.geeksforgeeks.org/problems/missing-number-in-array/0/?ref=self
"""


def missing_number(numbers, size):
    """
  Given an array of size n-1 and given that there are numbers from 1 to n with
  one missing, the missing number is to be found.
  """
    return (size * (size + 1)) // 2 - sum(numbers)


def main():
    """
  driver function
  """
    test_cases = int(input("No. of test cases: "))
    while test_cases > 0:
        size = int(input())
        numbers = list(map(int, input().strip().split(" ")))
        print(missing_number(numbers, size))
        test_cases -= 1


main()
