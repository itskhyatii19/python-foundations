"""
File: basic_file_ops.py
Purpose: Learn file handling in Python
Author: Khyati Sharma
"""

import os


# Writing to a file
def write_file():
    """
    Creates a file and writes content into it.
    'w' mode = write (overwrites existing content)
    """
    with open("sample.txt", "w") as file:
        file.write("Hello, this is a sample file.\n")
        file.write("Learning file handling in Python.\n")

    print("File written successfully!")


# Reading from a file
def read_file():
    """
    Reads entire file content.
    """
    with open("sample.txt", "r") as file:
        content = file.read()

    print("\nFile content:")
    print(content)


# Appending to a file
def append_file():
    """
    Adds new content without deleting old content.
    """
    with open("sample.txt", "a") as file:
        file.write("This line is appended.\n")

    print("Content appended!")


# Reading file line by line
def read_lines():
    """
    Reads file line by line.
    Useful for large files.
    """
    print("\nReading line by line:")
    with open("sample.txt", "r") as file:
        for line in file:
            print("Line:", line.strip())


# Check if file exists
def check_file_exists():
    """
    Checks whether file exists or not.
    """
    if os.path.exists("sample.txt"):
        print("\nFile exists!")
    else:
        print("\nFile does not exist!")


# Read using readlines()
def read_using_readlines():
    """
    Reads file using readlines()
    Returns list of lines.
    """
    with open("sample.txt", "r") as file:
        lines = file.readlines()

    print("\nUsing readlines():")
    print(lines)


# Copy file content
def copy_file():
    """
    Copies content from sample.txt to copy.txt
    """
    with open("sample.txt", "r") as source:
        data = source.read()

    with open("copy.txt", "w") as destination:
        destination.write(data)

    print("\nFile copied successfully!")


# Delete file safely
def delete_file():
    """
    Deletes file only if it exists.
    """
    if os.path.exists("copy.txt"):
        os.remove("copy.txt")
        print("\ncopy.txt deleted!")
    else:
        print("\nFile not found!")


def main():
    write_file()
    read_file()
    append_file()
    read_file()
    read_lines()

    check_file_exists()
    read_using_readlines()
    copy_file()
    delete_file()


if __name__ == "__main__":
    main()
