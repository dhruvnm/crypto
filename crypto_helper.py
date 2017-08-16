# Copyright 2017 Dhruv Mehta
from pathlib import Path
import sys

def exit():
    """Exit the program"""
    print("Goodbye!")
    sys.exit()

def get_cipher():
    """Get the cipher the user wants to use.

    Returns
    -------
    int
        The choice the user made.
    """
    while True:
        print("(0) Quit")
        print("(1) ROT47")
        print("(2) Caesar Cipher")
        try:
            choice = int(input("Please choose a cipher: "))
        except ValueError:
            choice = -1
        if choice < 0 or choice > 2:
            print("Invalid option. Try again.")
        elif choice is 0:
            exit()
        else:
            return choice

def get_direction():
    """Determine whether the user wants to encrypt or decrypt.

    Returns
    -------
    int
        The choice the user made.
    """
    while True:
        print("(0) Quit")
        print("(1) Encrypt")
        print("(2) Decrypt")
        try:
            choice = int(input("Choose a direction: "))
        except ValueError:
            choice = -1
        if choice < 0 or choice > 2:
            print("Invalid option. Try again.")
        elif choice is 0:
            exit()
        else:
            return choice

def get_file():
    """Get the file the program will work on.

    Returns
    -------
    str
        The file path the user provided.
    """
    while True:
        my_file = input("Enter the path for your file (0 to quit): ")
        if my_file is '0':
            exit()

        path = Path(my_file)
        if path.is_file():
            return my_file
        else:
            print("That isn't a file. Try again.")
