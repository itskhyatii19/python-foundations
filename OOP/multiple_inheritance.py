"""
File: multiple_inheritance.py
Author: Khyati Sharma

Purpose:
This file demonstrates MULTIPLE INHERITANCE in Python
and explains how Python resolves method conflicts
using MRO (Method Resolution Order).

Key Concepts:
- Multiple inheritance
- Diamond problem
- MRO (Method Resolution Order)
- super() behavior
"""

# ---------------- BASE CLASS 1 ----------------
class Father:
    def skills(self):
        print("Father: Business skills")


# ---------------- BASE CLASS 2 ----------------
class Mother:
    def skills(self):
        print("Mother: Cooking skills")


# ---------------- CHILD CLASS ----------------
class Child(Father, Mother):
    """
    Child inherits from BOTH Father & Mother
    This is called MULTIPLE INHERITANCE
    """

    def own_skill(self):
        print("Child: Coding skills")


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":

    c = Child()

    # Which skills() will be called?
    c.skills()      # Father wins (left to right rule)

    c.own_skill()

    # Printing MRO
    print("\nMRO:", Child.mro())
