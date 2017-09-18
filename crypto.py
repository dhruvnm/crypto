# Copyright 2017 Dhruv Mehta
import interface
from text import Text
from ciphers.rot import ROT47
from ciphers.caesar import Caesar
from ciphers.column import Column
from ciphers.sub import Sub

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

    elif cipher is 4:
        # Handle Substitution Cipher
        method = Sub()
        key = interface.get_key_file()
        
        if method.check_key(key) is False:
            print("Your key is invalid. Make sure your key two lines of equal length")
            continue
        else:
            print("NOTE: If your key doesn't cover sufficient characters, your message might be corrupted")


    s = '.'
    if direction is 1:
        method.encrypt(text, key)
        text.record(s.join([text.file_name, "cipher"]))
        print("Encryption complete!")
        print("Look at " + text.file_name + ".cipher for the results.")
    else:
        method.decrypt(text, key)
        text.record(s.join([text.file_name, "plain"]))
        print("Decryption complete!")
        print("Look at " + text.file_name + ".plain for the results.")
