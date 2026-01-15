"""
File: composition.py
Author: Khyati Sharma

Purpose:
Demonstrates COMPOSITION in Python.

Composition means:
→ "HAS-A" relationship
→ One class USES another class
→ Preferred over inheritance in real-world projects
"""


# ---------------- HELPER CLASS 1 ----------------
class Engine:
    """
    Engine class
    This class will be USED by Car
    """

    def start(self):
        print("Engine started")


# ---------------- HELPER CLASS 2 ----------------
class MusicSystem:
    """
    MusicSystem class
    Car will also USE this class
    """

    def play_music(self):
        print("Playing music...")


# ---------------- MAIN CLASS ----------------
class Car:
    """
    Car HAS:
    - Engine
    - MusicSystem

    This is COMPOSITION
    """

    def __init__(self, brand):
        self.brand = brand

        # Creating objects of helper classes
        self.engine = Engine()
        self.music = MusicSystem()

    def drive(self):
        print(f"{self.brand} car is ready to drive")
        self.engine.start()

    def enjoy_drive(self):
        """
        Uses MusicSystem object
        """
        self.music.play_music()


# ---------------- DRIVER CODE ----------------
if __name__ == "__main__":

    car1 = Car("Tesla")

    car1.drive()
    car1.enjoy_drive()
    car2 = Car("BMW")
    car2.drive()