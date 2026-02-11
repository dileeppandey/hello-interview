from sys import maxsize


class Solution:
    def findMaxAverage(self, nums, k):
        result = -maxsize
        windowStart = 0
        windowSum = 0
        if k > len(nums):
            return 0
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            if windowEnd >= k - 1:
                result = max(result, windowSum)
                windowSum -= nums[windowStart]
                windowStart += 1
        return result/k
