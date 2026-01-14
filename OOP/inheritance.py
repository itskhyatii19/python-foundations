"""
File: inheritance.py
Purpose: Understand inheritance in Python
Author: Khyati Sharma
"""

# Parent class
class Person:
    """
    This is a base (parent) class.
    Other classes can inherit from it.
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_basic_info(self):
        """Display common details"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Child class inheriting from Person
class Student(Person):
    """
    Student class inherits from Person.
    This means Student gets all properties of Person.
    """

    def __init__(self, name, age, course):
        # Calling parent class constructor
        super().__init__(name, age)
        self.course = course

    def display_student_info(self):
        """Display student specific info"""
        self.display_basic_info()  # using parent method
        print(f"Course: {self.course}")


def main():
    # Creating object of child class
    student1 = Student("Khyati", 19, "BTech AI")

    print("\nStudent Details:")
    student1.display_student_info()


# This ensures main() runs only when file is executed directly
if __name__ == "__main__":
    main()
# Child class inheriting from Person
class Student(Person):
    """
    Student class inherits from Person.
    This means Student gets all properties of Person.
    """

    def __init__(self, name, age, course):
        # Calling parent class constructor
        super().__init__(name, age)
        self.course = course

    def display_student_info(self):
        """Display student specific info"""
        self.display_basic_info()  # using parent method
        print(f"Course: {self.course}")