"""
File: interface_abc.py
Author: Khyati Sharma

Purpose:
This file demonstrates how to implement INTERFACES
in Python using Abstract Base Classes (ABC).

It explains:
- How interfaces define rules
- How child classes must follow structure
- Real-world payment gateway example

Key Concepts:
- Interface design
- Loose coupling
- Dependency inversion
- Runtime enforcement of methods

Usage:
Run this file to see how multiple payment apps
(Paytm, GooglePay) follow the same interface.
"""


from abc import ABC, abstractmethod

"""
INTERFACE USING ABSTRACT BASE CLASS (ABC)

What is an interface?
→ It only defines WHAT methods should exist
→ It does NOT define HOW they work

Rules:
1. We use ABC to create interface
2. All methods must be abstract
3. Child classes MUST implement all methods
"""


class PaymentGateway(ABC):
    """
    This is our INTERFACE

    Any payment app MUST follow this structure
    """

    @abstractmethod
    def pay(self, amount):
        """
        Abstract method
        No implementation allowed here
        """
        pass

    @abstractmethod
    def refund(self, amount):
        """
        Abstract method
        """
        pass


# ---------------- IMPLEMENTATION 1 ----------------

class Paytm(PaymentGateway):
    """
    This class IMPLEMENTS the interface

    If we don't implement ALL methods
    → Python will throw ERROR
    """

    def pay(self, amount):
        print(f"Paid ₹{amount} using Paytm")

    def refund(self, amount):
        print(f"Refunded ₹{amount} to Paytm")


# ---------------- IMPLEMENTATION 2 ----------------

class GooglePay(PaymentGateway):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Google Pay")

    def refund(self, amount):
        print(f"Refunded ₹{amount} to Google Pay")


# ---------------- DRIVER CODE ----------------

if __name__ == "__main__":
    """
    We are creating objects of concrete classes
    NOT of interface
    """

    payment1 = Paytm()
    payment2 = GooglePay()

    payment1.pay(500)
    payment2.pay(1000)

    payment1.refund(200)
    payment2.refund(300)
