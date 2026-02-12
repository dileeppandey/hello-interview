# Master Python's `doctest` to Ace Your Technical Interview

In a high-pressure coding interview, you often spend 20 minutes implementing a solution, only to realize you have no easy way to test it without writing boilerplate `unittest` or `pytest` code. 

Enter **`doctest`**. This built-in library allows you to write test cases directly inside your docstrings. It not only documents your code but also makes it instantly testable.

---

## 🚀 Introduction to `doctest`

The `doctest` module searches for pieces of text that look like interactive Python sessions and سپس executes those sessions to verify that they work exactly as shown.

### Why use it in an interview?
1. **Zero Setup**: No extra libraries needed. It's part of the Python Standard Library.
2. **"Living" Documentation**: Your tests serve as clear examples for the interviewer.
3. **Immediate Verification**: Shows you've considered edge cases before the interviewer even asks.
4. **Professionalism**: It demonstrates a "test-first" mindset and mastery of Python's ecosystem.

---

## 🛠️ How to Use `testmod()`

The most common way to run these tests within a script is using `doctest.testmod()`.

### 1. Simple Function Testing
Instead of just describing what a function does, show it in action.

```python
def add(a, b):
    """
    Returns the sum of a and b.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b
```

### 2. Class Method Testing
You can use `doctest` for classes as well.

```python
class Calculator:
    """
    A simple calculator class.

    >>> calc = Calculator()
    >>> calc.multiply(10, 5)
    50
    """
    def multiply(self, x, y):
        return x * y
```

### 3. Running the Tests
At the bottom of your file, add this snippet:

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

When you run `python your_script.py`, it will produce **no output** if all tests pass. This is the "no news is good news" philosophy.

---

## ✨ Pro Tips for the Interview

### Tip 1: The "Verbose" Reveal
If you want to impress the interviewer by showing the tests actually running, run your script with the `-v` flag:
`python your_script.py -v`

This will print a detailed report of every test executed and its result.

### Tip 2: Handling Exceptions
Show that you've thought about error handling by "expecting" an exception in your docstring.

```python
def divide(a, b):
    """
    >>> divide(10, 2)
    5.0
    >>> divide(10, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    return a / b
```
*Note: The `...` is a wildcard that matches any text, which is useful for ignoring the stack trace details.*

### Tip 3: The "Aha!" Moment
When you finish your implementation, say:
> "I've included some inline examples in the docstrings. Should we run them using `testmod` to verify the logic?"

This shows confidence and proactive testing.

---

## ⚠️ Common Pitfalls
- **Trailing Whitespace**: `doctest` is very sensitive. Ensure there are no extra spaces after your expected output.
- **Dict/Set Ordering**: Python 3.7+ preserves insertion order for dicts, but be careful with sets or older versions where order might vary. It's often safer to test against sorted results.
