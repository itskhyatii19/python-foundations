"""
File: diamond_problem.py
Author: Khyati Sharma

Purpose:
Demonstrates the DIAMOND PROBLEM
and how Python resolves it using MRO.
"""

class GrandParent:
    def show(self):
        print("GrandParent method")


class Parent1(GrandParent):
    def show(self):
        print("Parent1 method")
        super().show()


class Parent2(GrandParent):
    def show(self):
        print("Parent2 method")
        super().show()


class Child(Parent1, Parent2):
    def show(self):
        print("Child method")
        super().show()


if __name__ == "__main__":

    c = Child()
    c.show()

    print("\nMRO:", Child.mro())

"""MRO(Order in which Python searches methods) order:
Child → Parent1 → Parent2 → GrandParent → object

So execution:
Child.show()
 → Parent1.show()
   → Parent2.show()
     → GrandParent.show()

If you DON'T use super():
-Methods may run twice
-Infinite loops
-Bugs 
    
"""