"""
File: abstract_classes.py
Author: Khyati Sharma

Purpose:
This file demonstrates the concept of ABSTRACT CLASSES in Python
using the abc module.

It explains:
- What an abstract class is
- How to create abstract methods
- How child classes must implement them
- Real-world example using Bank Account system

Key Concepts:
- ABC (Abstract Base Class)
- @abstractmethod decorator
- Method overriding
- Polymorphism

Usage:
Run this file to see how different account types
(Savings & Current) behave differently
while following the same structure.
"""


from abc import ABC, abstractmethod
"""
abc -> Abstract Base Class module
ABC -> Used to create abstract classes
abstractmethod -> Used to force child classes to implement methods
"""


# -------------------- ABSTRACT CLASS --------------------
class BankAccount(ABC):
    """
    This is an abstract base class.
    It represents a general bank account.

    You CANNOT create an object of this class directly.
    It only provides a blueprint for child classes.
    """

    def __init__(self, name, balance):
        """
        Constructor for BankAccount

        name    -> account holder name
        balance -> initial account balance
        """
        self.name = name
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        """
        Abstract method.
        Every child class MUST implement this method.
        """
        pass

    @abstractmethod
    def account_type(self):
        """
        Abstract method.
        Returns the type of account.
        """
        pass

    def deposit(self, amount):
        """
        Concrete method (normal method)
        Adds money to the account
        """
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def show_balance(self):
        """
        Displays account details
        """
        print(f"Account holder: {self.name}")
        print(f"Current balance: ₹{self.balance}")


# -------------------- CHILD CLASS 1 --------------------
class SavingsAccount(BankAccount):
    """
    Child class of BankAccount
    Represents a savings account
    """

    def calculate_interest(self):
        """
        Savings account earns interest
        Interest rate = 4%
        """
        interest = self.balance * 0.04
        print(f"Interest earned: ₹{interest}")
        return interest

    def account_type(self):
        return "Savings Account"


# -------------------- CHILD CLASS 2 --------------------
class CurrentAccount(BankAccount):
    """
    Child class of BankAccount
    Represents a current account
    """

    def calculate_interest(self):
        """
        Current accounts do NOT earn interest
        """
        print("No interest for current account.")
        return 0

    def account_type(self):
        return "Current Account"


# -------------------- DRIVER CODE --------------------
if __name__ == "__main__":
    """
    This block runs only when this file is executed directly.
    It will NOT run if this file is imported.
    """

    # Creating objects of child classes
    acc1 = SavingsAccount("Rishi", 5000)
    acc2 = CurrentAccount("Rahul", 8000)

    # Savings Account
    print(acc1.account_type())
    acc1.show_balance()
    acc1.deposit(2000)
    acc1.calculate_interest()

    print("\n------------------\n")

    # Current Account
    print(acc2.account_type())
    acc2.show_balance()
    acc2.deposit(1000)
    acc2.calculate_interest()
