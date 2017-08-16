# Copyright 2017 Dhruv Mehta

def get_key():
    """Get the numerical key for the Caesar Cipher.

    Returns
    -------
    int
        The key value.
    """
    while True:
        try:
            key = int(input("Enter an integer key value: "))
            break
        except ValueError:
            print("Invalid option. Try again.")

    return key


def caesar(my_file, direction, key):
    """Executes the Caesar Cipher.

    Parameters
    ----------
    my_file : str
        The file path for the source file.
    direction : int
        A variable that tells if the program should encrypt(1) or decrypt(2).
    key : int
        The encryption/decryption key
    """
    if direction is 1:
        output = "ciphertext"
    else:
        output = "plaintext"

    if direction is 2:
        key = -key

    with open(my_file, "r") as f:
        with open(output, "w") as o:
            while True:
                c = f.read(1)
                if not c:
                    break
                n = ord(c)
                if 33 <= n <= 126:
                    n += key
                    while n > 126:
                        n -= 94
                    while n < 33:
                        n += 94
                    c = chr(n)
                o.write(c)

    if direction is 1:
        print("Encryption complete!")
    else:
        print("Decryption complete!")
    print("Check " + output + " for the result")
