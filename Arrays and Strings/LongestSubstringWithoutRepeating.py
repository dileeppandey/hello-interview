"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.


"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0
        longest_substr = ""

        for ch in s:
            if ch not in longest_substr:
                longest_substr += ch
            else:
                if len(longest_substr) > longest:
                    longest = len(longest_substr)
                longest_substr = longest_substr[(longest_substr.find(ch)+1):] + ch
        return max(longest, len(longest_substr))

s=Solution()
print(s.lengthOfLongestSubstring("umvejcuuk"))
