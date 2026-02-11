"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
  1. Open brackets are closed by the same type of brackets.
  2. Open brackets are closed in the correct order.
  3. Every close bracket has a corresponding open bracket of the same type.

Example: s = "()[]{}" → True
Example: s = "(]"    → False
Example: s = "([)]"  → False
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # ------------------------------------------------------------------
        # STACK INSIGHT: When we see an opening bracket, we "expect" a
        # matching close later. The most recently opened bracket must be
        # closed first (LIFO order). This is exactly what a stack models.
        # ------------------------------------------------------------------

        # Step 1: Define a mapping from closing to opening brackets
        matching = {')': '(', '}': '{', ']': '['}

        # Step 2: Initialize an empty stack
        stack = []

        # Step 3: Process each character
        for char in s:
            if char in matching:
                # Step 4a: It's a closing bracket.
                #          Pop the top of the stack and check for a match.
                top = stack.pop() if stack else '#'  # '#' is a sentinel for empty stack
                if top != matching[char]:
                    # Mismatch! Not valid.
                    return False
            else:
                # Step 4b: It's an opening bracket. Push onto stack.
                stack.append(char)

        # Step 5: Valid only if all opening brackets were matched (stack is empty)
        return len(stack) == 0


# ---- Quick verification ----
s = Solution()
print(s.isValid("()"))       # Expected: True
print(s.isValid("()[]{}"))   # Expected: True
print(s.isValid("(]"))       # Expected: False
print(s.isValid("([)]"))     # Expected: False
print(s.isValid("{[]}"))     # Expected: True
print(s.isValid(""))         # Expected: True  (empty string is valid)
