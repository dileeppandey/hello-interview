"""
Given an unsorted integer array, find the smallest missing positive integer.

https://leetcode.com/problems/first-missing-positive/
"""

import sys


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minPos = sys.maxsize
        maxPos = -sys.maxsize
        count = 0
        length = len(nums)
        for i in range(length):
            if nums[i] > 0 and nums[i] <= length:
                minPos = min(minPos, nums[i])
                maxPos = max(maxPos, nums[i])
            else:
                nums[i] = 1

        if minPos > 1:
            return 1

        result = [-1] * (length)

        for i, j in enumerate(nums):
            if j > 0:
                result[j-minPos] = 1
        print(result)
        for i, j in enumerate(result):
            if j == -1:
                return i + minPos
        return maxPos + 1
