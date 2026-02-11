"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

Example: n = 3 → ["((()))","(()())","(())()","()(())","()()()"]
"""


class Solution(object):
    def generateParanthesisHelper(self, left, right, current, result, n):
        """
        CONSTRAINED BACKTRACKING:
        - left = remaining '(' to place
        - right = remaining ')' to place
        - We can place '(' if left > 0
        - We can place ')' only if right > left (more '(' placed than ')')
        """
        # Step 1: Base case — used all closing parens → valid combination
        if right == 0:
            result.append(current)
            return

        # Step 2: Try adding '(' if we have any left
        if left > 0:
            self.generateParanthesisHelper(
                left - 1, right, current + '(', result, n)

        # Step 3: Try adding ')' only if it won't create invalid nesting
        #         (more ')' used means right count is less, so right > left
        #          means we've placed more '(' than ')')
        if right > left:
            self.generateParanthesisHelper(
                left, right - 1, current + ')', result, n)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n:
            # Start with n opening and n closing parens available
            self.generateParanthesisHelper(n, n, "", result, n)
        return result


# ---- Quick verification ----
s = Solution()
print(s.generateParenthesis(3))
# Expected: ['((()))', '(()())', '(())()', '()(())', '()()()']
print(s.generateParenthesis(1))
# Expected: ['()']