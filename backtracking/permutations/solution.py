"""
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example: nums = [1, 2, 3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # ------------------------------------------------------------------
        # BACKTRACKING INSIGHT: Build permutations one element at a time.
        # At each position, try every unused number. When we've placed all
        # numbers, we've found a complete permutation. Then backtrack
        # (undo the last choice) and try the next option.
        # ------------------------------------------------------------------

        result = []

        def backtrack(current: list[int], remaining: list[int]) -> None:
            """
            current:   the permutation we're building so far
            remaining: numbers we haven't placed yet
            """
            # Step 1: Base case — all numbers placed → found a permutation
            if not remaining:
                result.append(current[:])  # append a COPY
                return

            # Step 2: Try each remaining number at the current position
            for i in range(len(remaining)):
                # Step 3: CHOOSE — pick remaining[i]
                current.append(remaining[i])

                # Step 4: EXPLORE — recurse with the remaining numbers
                #         (exclude the one we just picked)
                backtrack(current, remaining[:i] + remaining[i + 1:])

                # Step 5: UNCHOOSE (backtrack) — remove the last pick
                #         so we can try the next option
                current.pop()

        backtrack([], nums)
        return result


# ---- Quick verification ----
s = Solution()
print(s.permute([1, 2, 3]))
# Expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

print(s.permute([0, 1]))
# Expected: [[0,1],[1,0]]

print(s.permute([1]))
# Expected: [[1]]
