"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example: n = 3 → 3 ways: [1+1+1, 1+2, 2+1]
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # ------------------------------------------------------------------
        # DP INSIGHT: To reach step n, you came from either step n-1 (one step)
        # or step n-2 (two steps). So: ways(n) = ways(n-1) + ways(n-2).
        # This is the Fibonacci sequence!
        # ------------------------------------------------------------------

        # Step 1: Handle base cases
        if n <= 2:
            return n

        # Step 2: Initialize the first two values
        #         ways(1) = 1 (only one way: take 1 step)
        #         ways(2) = 2 (two ways: 1+1 or 2)
        prev2 = 1  # ways(1)
        prev1 = 2  # ways(2)

        # Step 3: Build up from the bottom (bottom-up DP)
        #         We only need the last two values, not the full table
        for i in range(3, n + 1):
            current = prev1 + prev2  # ways(i) = ways(i-1) + ways(i-2)
            prev2 = prev1            # Shift the window forward
            prev1 = current

        # Step 4: prev1 now holds ways(n)
        return prev1


# ---- Quick verification ----
s = Solution()
print(s.climbStairs(2))   # Expected: 2
print(s.climbStairs(3))   # Expected: 3
print(s.climbStairs(4))   # Expected: 5
print(s.climbStairs(5))   # Expected: 8
