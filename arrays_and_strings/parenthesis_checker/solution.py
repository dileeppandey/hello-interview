"""
https://practice.geeksforgeeks.org/problems/parenthesis-checker/0 (GFG)
https://leetcode.com/problems/valid-parentheses/ (LeetCode)

Given an expression string exp, examine whether the pairs and the orders 
of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
"""

def parantesis_checker(text: str) -> bool:
    """
    Checks if the parentheses in the given string are balanced.
    """
    # ------------------------------------------------------------------
    # STACK INSIGHT: Use a LIFO stack to store opening brackets.
    # When we see a closing bracket, it MUST match the most recent 
    # (top of stack) opening bracket. This ensures proper nesting.
    # ------------------------------------------------------------------
    
    # Step 1: Initialize an empty stack
    stack = []
    
    # Step 2: Define mapping for easier lookups
    mapping = {')': '(', '}': '{', ']': '['}
    
    # Step 3: Iterate through each character in the text
    for char in text:
        # Step 4: If it's an opening bracket, push to stack
        if char in mapping.values():
            stack.append(char)
        # Step 5: If it's a closing bracket
        elif char in mapping:
            # Step 6: It must match the top of the stack
            if not stack or stack.pop() != mapping[char]:
                return False
        # Optional: Ignore non-bracket characters
        
    # Step 7: Balanced only if the stack is ultimately empty
    return len(stack) == 0


# ---- Quick verification ----
if __name__ == "__main__":
    test_cases = [
        ("{([])}", True),
        ("()", True),
        ("([]", False),
        ("([)]", False),
        ("}", False)
    ]
    
    for text, expected in test_cases:
        result = parantesis_checker(text)
        print(f"Text: {text:10} | Result: {str(result):5} | Expected: {str(expected):5} | {'PASS' if result == expected else 'FAIL'}")