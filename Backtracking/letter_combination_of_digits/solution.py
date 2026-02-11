"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9, return all possible letter
combinations that the number could represent (phone keyboard mapping).

Example: "23" → ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


class Solution(object):

    def backtrack(self, current_comb, next_digits, mapping, result):
        """
        DFS/BACKTRACKING:
        At each level of recursion, we process one digit and try all
        its possible letters.
        """
        # Step 1: Base case — no more digits to process
        if len(next_digits) == 0:
            result.append(current_comb)
        else:
            # Step 2: Get the letters for the current digit
            current_digit = next_digits[0]

            # Step 3: Try each letter mapped to this digit
            for ch in mapping[current_digit]:
                # Step 4: Recurse with the letter appended
                #         and remaining digits
                self.backtrack(current_comb + ch,
                               next_digits[1:], mapping, result)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Phone keyboard mapping
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []
        if digits:
            self.backtrack("", digits, mapping, result)
        return result


# ---- Quick verification ----
s = Solution()
print(s.letterCombinations("23"))
# Expected: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(s.letterCombinations(""))
# Expected: []
