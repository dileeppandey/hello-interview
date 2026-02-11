"""
https://leetcode.com/problems/jump-game/

Given an integer array nums, you are initially positioned at the first index
of the array. Each element in the array represents your maximum jump length
at that position. Return True if you can reach the last index, or False otherwise.

Example 1: nums = [2,3,1,1,4] -> True  (jump 1 to index 1, then 3 to last)
Example 2: nums = [3,2,1,0,4] -> False (always arrive at index 3, stuck)
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # ------------------------------------------------------------------
        # GREEDY INSIGHT: Track the farthest index we can reach so far.
        # As we walk forward, if the current index is beyond our farthest
        # reach, we are stuck. Otherwise, update the farthest reach.
        # ------------------------------------------------------------------

        # Step 1: Initialize the farthest position we can reach
        farthest = 0

        for i in range(len(nums)):
            # Step 2: If the current index is beyond our farthest reach,
            #         we can never get here — return False
            if i > farthest:
                return False

            # Step 3: Update the farthest position we can reach from index i
            #         farthest = max(farthest, i + nums[i])
            farthest = max(farthest, i + nums[i])

            # Step 4 (early exit): If farthest already reaches or passes
            #         the last index, we're done
            if farthest >= len(nums) - 1:
                return True

        # Step 5: If we finish the loop without returning False,
        #         we can reach the end
        return True


# ---- Quick verification ----
s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))   # Expected: True
print(s.canJump([3, 2, 1, 0, 4]))   # Expected: False
print(s.canJump([0]))                # Expected: True  (already at last index)
print(s.canJump([1, 0, 1, 0]))      # Expected: False
