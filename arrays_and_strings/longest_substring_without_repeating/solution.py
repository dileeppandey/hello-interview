"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without
repeating characters.

Example: "abcabcbb" → 3 ("abc")
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        SLIDING WINDOW APPROACH:
        Maintain a window [left, right] of unique characters.
        Expand right. When a duplicate is found, shrink left past the
        previous occurrence. Track the maximum window size.
        """
        # Step 1: Hash map to store the last index of each character
        char_index = {}
        left = 0
        max_len = 0

        # Step 2: Expand the window by moving right
        for right in range(len(s)):
            # Step 3: If character is already in window, shrink left
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1

            # Step 4: Update the character's latest position
            char_index[s[right]] = right

            # Step 5: Update the maximum length
            max_len = max(max_len, right - left + 1)

        return max_len


# ---- Quick verification ----
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))   # Expected: 3
print(s.lengthOfLongestSubstring("bbbbb"))       # Expected: 1
print(s.lengthOfLongestSubstring("pwwkew"))      # Expected: 3
print(s.lengthOfLongestSubstring("umvejcuuk"))   # Expected: 7
print(s.lengthOfLongestSubstring(""))             # Expected: 0
