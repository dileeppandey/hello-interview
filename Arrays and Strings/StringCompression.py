"""
Given an array of characters, compress it in-place.

https://leetcode.com/problems/string-compression/
"""


class Solution:
    
    def compress(self, chars) -> int:
        start = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while i + 1 < len(chars) and char == chars[i+1]:
                length, i = length + 1, i + 1
            chars[start] = char
            if length > 1:
                len_str = str(length)
                chars[start+1:start+ len(len_str) + 1] = len_str
                start += len(len_str)
            start, i = start + 1, i + 1
        return start
s = Solution()
print(s.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(s.compress(["a", "b", "b", "c", "c", "c"]))
print(s.compress(["a", "a", "b", "b", "c"]))
