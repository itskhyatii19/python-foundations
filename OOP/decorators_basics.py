"""
File: decorators.py
Author: Khyati Sharma

Purpose:
This file explains DECORATORS in Python.

Decorators are used to:
- Add logging
- Measure execution time
- Check permissions
- Modify function behavior
WITHOUT changing original function code.
"""


# ---------------- BASIC DECORATOR ----------------
def my_decorator(func):
    """
    This is a DECORATOR FUNCTION

    func -> function passed to decorator
    """

    def wrapper():
        """
        This wraps the original function
        Runs BEFORE and AFTER func()
        """

        print("Before function execution")
        func()   # calling original function
        print("After function execution")

    return wrapper


# ---------------- USING DECORATOR ----------------
@my_decorator
def say_hello():
    print("Hello, World!")


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":
    say_hello()

"""
Demonstrates decorator with function arguments
"""

def smart_divide(func):

    def wrapper(a, b):

        print("Checking before dividing...")

        if b == 0:
            print("Cannot divide by zero")
            return

        return func(a, b)

    return wrapper


@smart_divide
def divide(a, b):
    print(a / b)


if __name__ == "__main__":

    divide(10, 2)
    divide(10, 0)
    divide(15, 3)