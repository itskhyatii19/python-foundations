"""
File: polymorphism.py
Purpose: Understand polymorphism in Python
Author: Khyati Sharma
"""

# Parent class
class Animal:
    """
    Base class for all animals.
    """

    def sound(self):
        """
        This method will be overridden
        in child classes.
        """
        print("Animal makes a sound")


# Child class 1
class Dog(Animal):
    def sound(self):
        """
        Same method name, different behavior.
        """
        print("Dog barks")


# Child class 2
class Cat(Animal):
    def sound(self):
        """
        Same method name, different behavior.
        """
        print("Cat meows")


def main():
    # Creating objects
    animal = Animal()
    dog = Dog()
    cat = Cat()

    # Same method call, different outputs
    print("\nPolymorphism in action:")
    animal.sound()
    dog.sound()
    cat.sound()


if __name__ == "__main__":
    main()
