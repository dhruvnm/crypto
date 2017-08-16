# Copyright 2017 Dhruv Mehta

def rot47(my_file, direction):
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
                if n in range(33, 127):
                    n += 47
                    if n > 126:
                        n -= 94
                    c = chr(n)
                o.write(c)

    if direction is 1:
        print("Encryption complete!")
    else:
        print("Decryption complete!")
    print("Check " + output + " for the result")