# Copyright 2017 Dhruv Mehta
import interface
from text import Text
from ciphers.rot import ROT47
from ciphers.caesar import Caesar
from ciphers.column import Column

print("Welcome to crypto")

active = False

while True:
    cipher = interface.get_cipher()
    direction = interface.get_direction()
    my_file = interface.get_file(active)

    if my_file is not None:
        text = Text(my_file)
        active = True

    if cipher is 1:
        #Handle ROT47
        method = ROT47()
        key = None

    elif cipher is 2:
        #Handle Caesar Cipher
        method = Caesar()
        key = [interface.get_int_key()]

    elif cipher is 3:
        #Handle Columnar Transposition
        method = Column()
        key = [interface.get_unique_str_key()]
        if direction is 1:
            key.append(interface.get_pad())

    if direction is 1:
        method.encrypt(text, key)
        text.record("ciphertext")
        print("Encryption complete!")
        print("Look at ciphertext for the results.")
    else:
        method.decrypt(text, key)
        text.record("plaintext")
        print("Decryption complete!")
        print("Look at plaintext for the results.")
