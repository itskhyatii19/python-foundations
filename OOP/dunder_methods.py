"""
File: dunder_methods.py
Purpose: Learn Python special(dunder) methods
Author: Khyati Sharma
"""

class Book:
    """
    Book class demonstrating magic methods.
    """

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        """
        Controls what gets printed
        when you do: print(object)
        """
        return f"Book Title: {self.title}, Pages: {self.pages}"

    def __len__(self):
        """
        Controls what happens when
        len(object) is called.
        """
        return self.pages

    def __add__(self, other):
        """
        Allows adding two objects
        using + operator.
        """
        return self.pages + other.pages


def main():
    book1 = Book("Python Basics", 250)
    book2 = Book("Machine Learning", 300)

    # __str__ method
    print(book1)

    # __len__ method
    print("Pages in book1:", len(book1))

    # __add__ method
    total_pages = book1 + book2
    print("Total pages of both books:", total_pages)


if __name__ == "__main__":
    main()
