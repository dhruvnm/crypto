# Copyright 2017 Dhruv Mehta
import crypto_helper as cry
import rot

print("Welcome to Cryto v1.0")

while True:
    cipher = cry.get_cipher()
    direction = cry.get_direction()
    my_file = cry.get_file()

    if cipher is 1:
        #Handle ROT47
        rot.rot47(my_file, direction)
