"""
Leaders in an array
https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0/?ref=self
"""


def leaders_in_array(numbers, size):
    """
    Write a program to print all the LEADERS in the array. An element is leader
    if it is greater than all the elements to its right side. The rightmost 
    element is always a leader. 
    """
    if size == 1:
        return numbers
    leaders = []
    for i in range(size - 1):
        flag = True
        for j in range(i + 1, size):
            if numbers[i] > numbers[j]:
                continue
            else:
                flag = False
        if flag:
            leaders.append(numbers[i])
    leaders.append(numbers[size - 1])
    return leaders

def main():
    """
    driver function
    """
    test_cases = int(input())
    while test_cases > 0:
        size = int(input())
        numbers = list(map(int, input().strip().split(" ")))
        res = leaders_in_array(numbers, size)
        for x in res:
            print(x, end = " ")
        print()
        test_cases -= 1


main()