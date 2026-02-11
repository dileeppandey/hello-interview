"""
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t, return the minimum window substring of s such
that every character in t (including duplicates) is included in the window.
If there is no such window, return the empty string "".

Example: s = "ADOBECODEBANC", t = "ABC" → "BANC"
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ------------------------------------------------------------------
        # SLIDING WINDOW INSIGHT (Variable Size):
        # Use two pointers (left, right) to define a window.
        # 1. Expand right to include more characters until the window
        #    contains all characters of t.
        # 2. Then shrink left to find the smallest valid window.
        # 3. Repeat until right reaches the end of s.
        # ------------------------------------------------------------------

        if not s or not t:
            return ""

        # Step 1: Count the required characters from t
        required = Counter(t)
        needed = len(required)  # Number of unique chars we still need

        # Step 2: Track characters in our current window
        window_counts = {}
        formed = 0  # Number of unique chars in window with desired frequency

        # Step 3: Initialize pointers and result tracking
        left = 0
        min_len = float('inf')
        min_left = 0

        # Step 4: Expand the window by moving right
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # Step 5: Check if current char's count matches the required count
            if char in required and window_counts[char] == required[char]:
                formed += 1

            # Step 6: Try to shrink the window from the left while it's valid
            while formed == needed:
                # Update the result if this window is smaller
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    min_left = left

                # Shrink: remove leftmost character
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in required and window_counts[left_char] < required[left_char]:
                    formed -= 1
                left += 1

        # Step 7: Return the minimum window, or "" if none found
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]


# ---- Quick verification ----
sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Expected: "BANC"
print(sol.minWindow("a", "a"))                 # Expected: "a"
print(sol.minWindow("a", "aa"))                # Expected: ""
