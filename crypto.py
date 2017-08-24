# Copyright 2017 Dhruv Mehta
import interface
from text import Text
from ciphers.rot import ROT47
from ciphers.caesar import Caesar
from ciphers.column import Column

print("Welcome to crypto")

while True:
    cipher = interface.get_cipher()
    direction = interface.get_direction()
    my_file = interface.get_file()
    text = Text(my_file)

    if cipher is 1:
        #Handle ROT47
        method = ROT47()
        key = None

    elif cipher is 2:
        #Handle Caesar Cipher
        method = Caesar()
        key = [interface.int_key()]

    elif cipher is 3:
        #Handle Columnar Transposition
        method = Column()
        key = [interface.unique_str_key()]
        if direction is 1:
            key.append(interface.pad())

    if direction is 1:
        method.encrypt(text, key)
        text.record("ciphertext")
    else:
        method.decrypt(text, key)
        text.record("plaintext")
