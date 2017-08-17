# crypto

## Overview
A program that allows you to encrypt and decrypt messages with various different ciphers

## Run crypto
To run crypto make sure you have the latest version of Python 3.
Make sure you are in the `crypto` directory and then run
```
python3 crypto.py
```

## Supported Ciphers
1. ROT47

    ROT47 will take every character as ASCII and shift its value by 47 places. Since there are 94 valid ASCII characters, an encrypted   message can be decrypted by running ROT47 a second time.

2. Caesar Cipher

    The Caesar Cipher takes every character as ASCII and shifts its value by the designated key. To decrypt, it will shift in the opposite direction.

3. Columnar Transposition

    Columnar Transposition involves placing every letter of the key as the top row of a matrix and then filling the rest of the matrix with the rest of the message. For example for the message `My name is Dhruv`, the key `mehta`, and the pad character `x` it would look like the following:
    ```
    m|e|h|t|a
    M|y| |n|a
    m|e| |i|s
     |D|h|r|u
    v|x|x|x|x
    ```
    Notice that the pad character is used to complete the matrix. The columns are then reordered to be in order of lowest ASCII value to largest.
    ```
    a|e|h|m|t
    a|y| |M|n
    s|e| |m|i
    u|D|h| |r
    x|x|x|v|x
    ```
    Finally the values are read off the columns to get a final ciphertext of:
    ```
    asuxyeDx  hxMm vnirx
    ```
    Decryption occurs by reversing the process
