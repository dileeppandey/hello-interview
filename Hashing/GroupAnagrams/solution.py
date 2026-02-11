"""
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group the anagrams together. You can return the
answer in any order.

Example: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"], ["nat","tan"], ["ate","eat","tea"]]
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # ------------------------------------------------------------------
        # HASH MAP INSIGHT: Two strings are anagrams if and only if their
        # sorted characters are identical. We use the sorted string as a
        # hash key to group anagrams together.
        # ------------------------------------------------------------------

        # Step 1: Create a hash map where:
        #   key   = canonical form of the word (sorted characters)
        #   value = list of all words that share that canonical form
        groups = defaultdict(list)

        # Step 2: Iterate through each string
        for word in strs:
            # Step 3: Create the canonical key by sorting the characters
            #         "eat" → "aet", "tea" → "aet", "ate" → "aet"
            #         All anagrams produce the same sorted key
            key = tuple(sorted(word))

            # Step 4: Add the original word to its anagram group
            groups[key].append(word)

        # Step 5: Return all the groups as a list of lists
        return list(groups.values())


# ---- Quick verification ----
s = Solution()
result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
for group in result:
    print(sorted(group))
# Expected groups (order may vary):
# ['bat']
# ['nat', 'tan']
# ['ate', 'eat', 'tea']

print(s.groupAnagrams([""]))       # Expected: [[""]]
print(s.groupAnagrams(["a"]))      # Expected: [["a"]]
