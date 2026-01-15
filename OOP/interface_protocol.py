"""
File: interface_protocol.py
Author: Khyati Sharma

Purpose:
This file demonstrates modern INTERFACE implementation
using typing.Protocol (Python 3.8+).

It explains:
- Duck typing
- Structural subtyping
- Flexible interface design
- Industry-level best practices

Key Concepts:
- Protocol
- Type hints
- Interface without inheritance
- Clean architecture

Usage:
Run this file to see how different payment apps
follow the same interface WITHOUT inheritance.
"""


from typing import Protocol

"""
INTERFACE USING PROTOCOL (Modern Python way)

No inheritance required
We only care about METHOD STRUCTURE
"""


class PaymentInterface(Protocol):
    """
    This defines expected behavior
    Any class having these methods
    automatically follows this interface
    """

    def pay(self, amount: int) -> None:
        ...

    def refund(self, amount: int) -> None:
        ...


# ---------------- IMPLEMENTATION 1 ----------------

class PhonePe:
    """
    Notice:
    ❌ No inheritance
    ✔ Still valid interface
    """

    def pay(self, amount):
        print(f"Paid ₹{amount} using PhonePe")

    def refund(self, amount):
        print(f"Refunded ₹{amount} to PhonePe")


# ---------------- IMPLEMENTATION 2 ----------------

class AmazonPay:

    def pay(self, amount):
        print(f"Paid ₹{amount} using Amazon Pay")

    def refund(self, amount):
        print(f"Refunded ₹{amount} to Amazon Pay")


# ---------------- FUNCTION USING INTERFACE ----------------

def process_payment(gateway: PaymentInterface):
    """
    We don't care what class it is
    We only care:
    Does it have pay() and refund() ?
    """

    gateway.pay(1000)
    gateway.refund(500)


# ---------------- DRIVER CODE ----------------

if __name__ == "__main__":

    p1 = PhonePe()
    p2 = AmazonPay()

    process_payment(p1)
    process_payment(p2)
