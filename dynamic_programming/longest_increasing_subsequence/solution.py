"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

Example: nums = [10, 9, 2, 5, 3, 7, 101, 18] → 4 ([2, 3, 7, 101])
"""


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # ------------------------------------------------------------------
        # DP INSIGHT: dp[i] = length of longest increasing subsequence
        # ending at index i. For each i, look back at all j < i where
        # nums[j] < nums[i], and take the best dp[j] + 1.
        # ------------------------------------------------------------------

        if not nums:
            return 0

        n = len(nums)

        # Step 1: Initialize dp array — every element is an LIS of length 1
        dp = [1] * n

        # Step 2: For each position i, check all previous positions j
        for i in range(1, n):
            for j in range(i):
                # Step 3: If nums[j] < nums[i], we can extend the subsequence
                #         ending at j by appending nums[i]
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # Step 4: The answer is the maximum value in the dp array
        #         (the LIS could end at any position)
        return max(dp)


# ---- Quick verification ----
s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Expected: 4
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))              # Expected: 4
print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))           # Expected: 1
