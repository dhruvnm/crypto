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
        print("(3) Columnar Transposition")
        try:
            choice = int(input("Please choose a cipher: "))
        except ValueError:
            choice = -1
        if choice < 0 or choice > 3:
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

def get_file(active):
    """Get the file the program will work on.

    Parameters
    ----------
    active : bool
        Determines whether there is an active file or not.

    Returns
    -------
    str
        The file path the user provided.
        None will be returned if chaining the previous output.
    """
    while True:
        print("Enter the path for your file or enter 0 to quit.")
        my_file = input("You can also just press enter to chain the previous output: ")
        if my_file is '0':
            exit()
        elif my_file is '' and active:
            return None

        path = Path(my_file)
        if path.is_file():
            return my_file
        else:
            print("That isn't a file. Try again.")

def get_int_key():
    """Get a numerical key.

    Returns
    -------
    str
        The key value.
    """
    while True:
        key = input("Enter an integer key value: ")
        try:
            key = int(key)
            break
        except ValueError:
            print("Invalid option. Try again.")

    return key

def get_unique_str_key():
    """Get a key with unique ASCII values.

    Returns
    -------
    str
        The key value.
    """
    while True:
        key = input("Enter a key phrase: ")
        if len(key) > 0:
            i = 1
            t = True
            key_alpha = sorted(key)
            while i < len(key):
                if key_alpha[i] is key_alpha[i - 1]:
                    print("Your key cannot repeat ASCII characters")
                    t = False
                    break
                i += 1
            if t:
                break
        else:
            print("The key must be at least one character.")
    return key

def get_pad():
    """Get a pad character.

    Returns
    -------
    chr
        The pad character.
    """
    while True:
        pad = input("Enter a pad character: ")
        if len(pad) == 1:
            break
        else:
            print("The pad must be one character.")
    return pad
