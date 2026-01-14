"""
File: classes_basics.py
Purpose: Learn Python OOP fundamentals
Author: Khyati Sharma
"""

# Creating a class named Student
class Student:
    """A class to represent a student"""

    def __init__(self, name, age, course):
        """
        __init__ is a constructor.
        It runs automatically when an object is created.
        self refers to the current object.
        """
        self.name = name      # storing name
        self.age = age        # storing age
        self.course = course  # storing course

    def display_info(self):
        """
        This method prints student details.
        Methods are functions inside a class.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

    def is_adult(self):
        """
        This method checks if student is adult.
        Returns True or False.
        """
        return self.age >= 18


def main():
    # Creating objects of Student class
    student1 = Student("Khyati", 19, "BTech AI")
    student2 = Student("Rahul", 17, "BSc CS")

    # Calling methods using object
    print("\nStudent 1 Details:")
    student1.display_info()        # calls display_info method
    print("Is Adult?", student1.is_adult())  # calls is_adult method

    print("\nStudent 2 Details:")
    student2.display_info()
    print("Is Adult?", student2.is_adult())


# This ensures main() runs only when file is executed directly
if __name__ == "__main__":
    main()