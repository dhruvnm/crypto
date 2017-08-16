# Copyright 2017 Dhruv Mehta
import helper as cry
from ciphers import *

print("Welcome to Cryto v1.0")

while True:
    cipher = cry.get_cipher()
    direction = cry.get_direction()
    my_file = cry.get_file()

    if cipher is 1:
        #Handle ROT47
        rot.rot47(my_file, direction)

    elif cipher is 2:
        #Handle Caesar Cipher
        key = caesar.get_key()
        caesar.caesar(my_file, direction, key)

    elif cipher is 3:
        #Handle Columnar Transposition
        key = column.get_key()
        pad = column.get_pad()
        if direction is 1:
            column.encrypt(my_file, key, pad)
