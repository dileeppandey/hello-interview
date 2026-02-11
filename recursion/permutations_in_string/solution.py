"""
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1.
In other words, one of s1's permutations is a substring of s2.

Example: s1 = "ab", s2 = "eidbaooo" → True ("ba" is a permutation of "ab")
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # ------------------------------------------------------------------
        # FIXED-SIZE SLIDING WINDOW + FREQUENCY MATCH INSIGHT:
        # A permutation of s1 has exactly the same character frequencies.
        # Slide a window of size len(s1) over s2 and compare frequency maps.
        # ------------------------------------------------------------------

        if len(s1) > len(s2):
            return False

        # Step 1: Count character frequencies in s1
        s1_count = Counter(s1)
        window_size = len(s1)

        # Step 2: Initialize the first window in s2
        window_count = Counter(s2[:window_size])

        # Step 3: Check if the first window matches
        if s1_count == window_count:
            return True

        # Step 4: Slide the window across s2
        for i in range(window_size, len(s2)):
            # Add the new character entering the window
            window_count[s2[i]] += 1

            # Remove the character leaving the window
            left_char = s2[i - window_size]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

            # Step 5: Check if current window matches s1's frequencies
            if s1_count == window_count:
                return True

        return False


# ---- Quick verification ----
s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))  # Expected: True
print(s.checkInclusion("ab", "eidboaoo"))  # Expected: False
print(s.checkInclusion("adc", "dcda"))      # Expected: True
print(s.checkInclusion("a", "a"))           # Expected: True
