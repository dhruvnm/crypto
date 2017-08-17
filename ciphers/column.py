# Copyright 2017 Dhruv Mehta
from collections import OrderedDict
from shutil import copyfile

def get_key():
    """Get the numerical key for Columnar Transposition.

    Returns
    -------
    str
        The key value.
    """
    while True:
        key = input("Enter a key phrase: ")
        if len(key) > 0:
            r = range(1, len(key))
            t = True
            key_alpha = sorted(key)
            for x in r:
                if key_alpha[x] is key_alpha[x - 1]:
                    print("Your key cannot repeat ASCII characters")
                    t = False
                    break
            if t:
                break
        else:
            print("The key must be at least one character.")
    return key

def get_pad():
    """Get the pad character for Columnar Transposition.

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

def encrypt(my_file, key, pad):
    """Encrypt the plaintext using Columnar Transposition.

    Parameters
    ----------
    my_file : str
        The plaintext file.
    key : str
        The key phrase.
    pad : chr
        The pad character.
    """
    key_alpha = sorted(key)
    matrix = OrderedDict()
    for c in key_alpha:
        matrix[c] = list()

    with open(my_file, "r") as f:
        plaintext = f.read()

    extra = len(plaintext) % len(key)
    if extra is not 0:
        for _ in range(len(key) - extra):
            plaintext += pad

    rows = int(len(plaintext) / len(key))
    i = 0
    for _ in range(rows):
        for c in key:
            matrix[c].append(plaintext[i])
            i += 1

    with open("ciphertext", "w") as o:
        for k, v in matrix.items():
            for c in v:
                o.write(c)

    copyfile("ciphertext", ".chain")
    print("Encryption complete!")
    print("Check ciphertext for the result")

def decrypt(my_file, key):
    """Decrypt the ciphertext encrypted with Columnar Transposition.

    Parameters
    ----------
    my_file : str
        The ciphertext file.
    key : str
        The key phrase.
    """
    key_alpha = sorted(key)
    matrix = OrderedDict()
    for c in key_alpha:
        matrix[c] = list()

    with open(my_file, "r") as f:
        ciphertext = f.read()

    rows = int(len(ciphertext) / len(key))
    i = 0
    for c in key_alpha:
        for _ in range(rows):
            matrix[c].append(ciphertext[i])
            i += 1

    i = 0
    with open("plaintext", "w") as o:
        for _ in range(rows):
            for c in key:
                o.write(matrix[c][i])
            i += 1

    copyfile("plaintext", ".chain")
    print("Decryption complete!")
    print("Check plaintext for the result")
