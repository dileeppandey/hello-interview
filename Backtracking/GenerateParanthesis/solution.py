"""
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.
"""

class Solution(object):
    def generateParanthesisHelper(self, left, right, current, result, n):
        if right == 0:
            result.append(current)
        if left > 0:
            self.generateParanthesisHelper(
                left-1, right, current+'(', result, n)
        if right > left:
            self.generateParanthesisHelper(
                left, right-1, current+')', result, n)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n:
            left = right = n
            self.generateParanthesisHelper(left, right, "", result, n)
        return result

s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(1))