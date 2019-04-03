"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent.
"""


class Solution(object):

    def backtrack(self, current_comb, next_digits, mapping, result):
        if len(next_digits) == 0:
            result.append(current_comb)
        else:
            for ch in mapping[next_digits[0]]:
                self.backtrack(current_comb+ch,
                               next_digits[1:], mapping, result)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
                   "7": "pqrs", "8": "tuv", "9": "wxyz"
                   }
        result = []
        if digits:
            self.backtrack("", digits, mapping, result)

        return result


s = Solution()
print(s.letterCombinations("23"))
