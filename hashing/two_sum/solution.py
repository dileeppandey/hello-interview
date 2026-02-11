"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target. You may assume that each input
would have exactly one solution, and you may not use the same element twice.

Example: nums = [2, 7, 11, 15], target = 9 → [0, 1] (because 2 + 7 = 9)
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # ------------------------------------------------------------------
        # HASH MAP INSIGHT: For each number, we need its "complement"
        # (target - num). A hash map lets us check in O(1) whether
        # we've already seen the complement.
        # ------------------------------------------------------------------

        # Step 1: Create a hash map to store {value: index} as we go
        seen = {}

        # Step 2: Single pass through the array
        for i, num in enumerate(nums):
            # Step 3: Calculate the complement we need
            complement = target - num

            # Step 4: Check if the complement is already in our map
            if complement in seen:
                # Found! Return both indices
                return [seen[complement], i]

            # Step 5: Otherwise, record this number and its index
            #         for future lookups
            seen[num] = i

        # Step 6: Problem guarantees a solution, but return empty for safety
        return []


# ---- Quick verification ----
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))   # Expected: [0, 1]
print(s.twoSum([3, 2, 4], 6))        # Expected: [1, 2]
print(s.twoSum([3, 3], 6))           # Expected: [0, 1]
