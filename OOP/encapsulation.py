"""
File: encapsulation.py
Purpose: Understand encapsulation in Python
Author: Khyati Sharma
"""

class BankAccount:
    """
    BankAccount class demonstrates encapsulation.
    Some variables are kept private to protect data.
    """

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder   # public variable
        self.__balance = balance               # private variable (__)

    def show_balance(self):
        """
        Public method to safely access private balance
        """
        print(f"Current Balance: ₹{self.__balance}")

    def deposit(self, amount):
        """
        Add money to account
        """
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        """
        Withdraw money safely
        """
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")


def main():
    # Creating object
    acc1 = BankAccount("Khyati", 5000)

    # Accessing public variable
    print("Account Holder:", acc1.account_holder)

    # Accessing private variable directly (NOT allowed)
    # print(acc1.__balance)   => This will cause error

    # Accessing private variable safely
    acc1.show_balance()

    # Performing transactions
    acc1.deposit(2000)
    acc1.show_balance()

    acc1.withdraw(3000)
    acc1.show_balance()

    acc1.withdraw(10000)  # Trying to withdraw more than balance


if __name__ == "__main__":
    main()
