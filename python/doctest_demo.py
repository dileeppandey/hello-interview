import doctest

def add(a, b):
    """
    Returns the sum of a and b.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

class Calculator:
    """
    A simple calculator class.

    >>> calc = Calculator()
    >>> calc.multiply(10, 5)
    50
    """
    def multiply(self, x, y):
        return x * y

def divide(a, b):
    """
    Returns the division of a by b.
    Handles zero division by showing tracebacks in doctest.

    >>> divide(10, 2)
    5.0
    >>> divide(10, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    return a / b

if __name__ == "__main__":
    print("Running doctests...")
    results = doctest.testmod()
    if results.failed == 0:
        print(f"All {results.attempted} tests passed!")
    else:
        print(f"{results.failed} tests failed out of {results.attempted} attempted.")
