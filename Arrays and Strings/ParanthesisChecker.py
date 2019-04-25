"""
Paranthesis Checker
https://practice.geeksforgeeks.org/problems/parenthesis-checker/0
"""


def parantesis_checker(text):
    """
    Given an expression string exp, examine whether the pairs and the orders 
    of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
    """
    text_stack = []
    for x in text:
        if x == '(' or x == '{' or x == '[':
            text_stack.append(x)
        else:
            if len(text_stack) > 0:
                popped = text_stack.pop()
            else:
                return "not balanced"
            if x == ')' and popped == '(':
                continue
            elif x == '}' and popped == '{':
                continue
            elif x == ']' and popped == '[':
                continue
            else:
                return "not balanced"
    if len(text_stack) == 0:
        return "balanced"
    else:
        return "not balanced"


def main():
    test_cases = int(input())
    while test_cases > 0:
        text = input().strip()
        print(parantesis_checker(text))
        test_cases -= 1


main()