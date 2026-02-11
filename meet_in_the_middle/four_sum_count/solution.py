"""
https://leetcode.com/problems/4sum-ii/

Given four integer arrays nums1, nums2, nums3, and nums4, all of length n,
return the number of tuples (i, j, k, l) such that:
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example:
    nums1 = [1, 2], nums2 = [-2, -1], nums3 = [-1, 2], nums4 = [0, 2]
    Output: 2  →  (0,0,0,1) and (1,1,0,0)
"""
from collections import Counter


class Solution:
    def fourSumCount(
        self, nums1: list[int], nums2: list[int],
        nums3: list[int], nums4: list[int]
    ) -> int:
        # ------------------------------------------------------------------
        # MEET IN THE MIDDLE INSIGHT:
        # Instead of checking all n^4 combinations, split into two halves:
        #   Half A: all possible sums of nums1[i] + nums2[j]  → O(n²)
        #   Half B: all possible sums of nums3[k] + nums4[l]  → O(n²)
        # Then for each sum_a, count how many sum_b = -sum_a exist.
        # Total: O(n²) instead of O(n⁴).
        # ------------------------------------------------------------------

        # Step 1: Compute all pairwise sums from the first two arrays
        #         and count the frequency of each sum
        sum_ab = Counter()
        for a in nums1:
            for b in nums2:
                sum_ab[a + b] += 1

        # Step 2: For each pairwise sum from the last two arrays,
        #         check how many first-half sums are its complement
        count = 0
        for c in nums3:
            for d in nums4:
                # We need sum_ab + (c + d) == 0, so look up -(c + d)
                complement = -(c + d)
                count += sum_ab.get(complement, 0)

        return count


# ---- Quick verification ----
s = Solution()
print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))  # Expected: 2
print(s.fourSumCount([0], [0], [0], [0]))                   # Expected: 1
