# Copyright 2017 Dhruv Mehta
from shutil import copyfile

def rot47(my_file, direction):
    """Executes the ROT47 cipher.

    Parameters
    ----------
    my_file : str
        The file path for the source file.
    direction : int
        A variable that tells if the program should encrypt(1) or decrypt(2).
    """
    if direction is 1:
        output = "ciphertext"
    else:
        output = "plaintext"

    with open(my_file, "r") as f:
        with open(output, "w") as o:
            while True:
                c = f.read(1)
                if not c:
                    break
                n = ord(c)
                if 33 <= n <= 126:
                    n += 47
                    if n > 126:
                        n -= 94
                    c = chr(n)
                o.write(c)

    copyfile(output, ".chain")

    if direction is 1:
        print("Encryption complete!")
    else:
        print("Decryption complete!")
    print("Check " + output + " for the result")
