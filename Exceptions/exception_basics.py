"""
File: exception_basics.py
Purpose: Learn exception handling in Python
Author: Khyati Sharma
"""

import requests


# Basic try-except
def basic_exception():
    """
    Handles division error.
    """
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except ValueError:
        print("Error: Please enter a valid number!")

    else:
        print("Calculation successful!")

    finally:
        print("Execution completed.\n")


# Handling file errors
def file_exception():
    """
    Handles file not found error.
    """
    try:
        with open("data.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("Error: File not found!")


# Multiple exceptions in one block
def multiple_exception():
    """
    Handles multiple exceptions together.
    """
    try:
        arr = [1, 2, 3]
        print(arr[5])      # IndexError
        x = int("abc")    # ValueError

    except (IndexError, ValueError) as e:
        print("Caught error:", e)


# Raising custom exception
def age_validator(age):
    """
    Raises error if age < 18
    """
    if age < 18:
        raise ValueError("Age must be 18 or above!")
    else:
        print("Access granted!")


# Custom exception class
class InvalidMarksError(Exception):
    """Custom exception for marks validation"""
    pass


def marks_validator(marks):
    """
    Uses custom exception.
    """
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100!")
    else:
        print("Valid marks!")


# Using assert
def assert_example(num):
    """
    Assert example.
    """
    assert num > 0, "Number must be positive!"
    print("Valid number:", num)


# Retry logic
def retry_example():
    """
    Retry logic example.
    """
    attempts = 3
    while attempts > 0:
        try:
            num = int(input("Enter a number: "))
            print("You entered:", num)
            break
        except ValueError:
            attempts -= 1
            print("Invalid input! Attempts left:", attempts)


# API exception handling
def api_exception():
    """
    Handles API request errors.
    """
    try:
        response = requests.get("https://invalid-url.com", timeout=3)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("API Error:", e)


def main():
    basic_exception()
    file_exception()
    multiple_exception()

    # Age validation
    try:
        age_validator(16)
    except ValueError as e:
        print("Age Error:", e)

    # Custom exception
    try:
        marks_validator(150)
    except InvalidMarksError as e:
        print("Marks Error:", e)

    # Assert example
    try:
        assert_example(-5)
    except AssertionError as e:
        print("Assertion Error:", e)

    retry_example()
    api_exception()


if __name__ == "__main__":
    main()
