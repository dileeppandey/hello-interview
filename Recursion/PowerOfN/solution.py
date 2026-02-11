"""
https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n.

Example: x = 2.0, n = 10 → 1024.0
Example: x = 2.0, n = -2 → 0.25
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ------------------------------------------------------------------
        # DIVIDE AND CONQUER INSIGHT (Fast Exponentiation):
        # Instead of multiplying x by itself n times (O(n)), use:
        #   x^n = (x^(n/2))^2          if n is even
        #   x^n = x * (x^(n/2))^2      if n is odd
        # This halves the problem at each step → O(log n)
        # ------------------------------------------------------------------

        # Step 1: Handle negative exponent
        #         x^(-n) = 1 / x^n
        if n < 0:
            x = 1 / x
            n = -n

        # Step 2: Recursive fast exponentiation
        def fast_pow(base: float, exp: int) -> float:
            # Base case
            if exp == 0:
                return 1.0

            # Step 3: Compute half the power
            half = fast_pow(base, exp // 2)

            # Step 4: Combine — square the half result
            if exp % 2 == 0:
                return half * half         # Even: x^n = (x^(n/2))^2
            else:
                return half * half * base  # Odd:  x^n = x * (x^(n/2))^2

        return fast_pow(x, n)


# ---- Quick verification ----
s = Solution()
print(s.myPow(2.0, 10))    # Expected: 1024.0
print(s.myPow(2.1, 3))     # Expected: 9.261
print(s.myPow(2.0, -2))    # Expected: 0.25
print(s.myPow(0.0, 5))     # Expected: 0.0
