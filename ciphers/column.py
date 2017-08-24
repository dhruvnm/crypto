# Copyright 2017 Dhruv Mehta
from .cipher import Cipher
from collections import OrderedDict

class Column(Cipher):
    """A class used to encrypt messages with the Columnar Transposition Cipher"""
    def encrypt(self, plaintext, key):
        """Encrypt the plaintext with Columnar Transposition.

        Parameters
        ----------
        plaintext : Text
            The message to be encrypted
        key : list
            Should be a list containing two elements:
                (0) A unique ASCII key.
                (1) A pad character.
        """
        key_alpha = sorted(key[0])
        matrix = OrderedDict()
        for c in key_alpha:
            matrix[c] = list()

        extra = len(plaintext.text) % len(key[0])
        if extra is not 0:
            i = 0
            while i < (len(key[0]) - extra):
                plaintext.text.append(key[1])
                i += 1

        rows = int(len(plaintext.text) / len(key[0]))
        i = 0
        j = 0
        while i < rows:
            for c in key[0]:
                matrix[c].append(plaintext.text[j])
                j += 1
            i += 1

        i = 0
        for k, v in matrix.items():
            for c in v:
                plaintext.text[i] = c
                i += 1


    def decrypt(self, ciphertext, key):
        """ Decrypt the ciphertext with Columnar Transposition.

        Parameters
        ----------
        ciphertext : Text
            The message to be decrypted.
        key : list
            Should be a list containing one element:
                (0) A unique ASCII key.
        """
        key_alpha = sorted(key[0])
        matrix = OrderedDict()
        for c in key_alpha:
            matrix[c] = list()

        rows = int(len(ciphertext.text) / len(key[0]))
        j = 0
        for c in key_alpha:
            i = 0
            while i < rows:
                matrix[c].append(ciphertext.text[j])
                j += 1
                i += 1

        i = 0
        j = 0
        while i < rows:
            for c in key[0]:
                ciphertext.text[j] = matrix[c][i]
                j += 1
            i += 1
