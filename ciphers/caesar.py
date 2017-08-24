# Copyright 2017 Dhruv Mehta
from .cipher import Cipher

class Caesar(Cipher):
    """A class used to encrypt messages with the Caesar Cipher."""
    def encrypt(self, plaintext, key):
        """Encrypt the plaintext with the Caesar cipher.

        Parameters
        ----------
        plaintext : Text
            The message to be encrypted
        key : list
            Should be a list containing one element:
                (0) An integer.
        """
        self._caesar(plaintext, int(key[0]))

    def decrypt(self, ciphertext, key):
        """Decrypt the ciphertext with the Caesar cipher.

        Parameters
        ----------
        ciphertext : Text
            The message to be decrypted.
        key : list
            Should be a list containing one element:
                (0) An integer.
        """
        self._caesar(ciphertext, -int(key[0]))

    def _caesar(self, text, key):
        i = 0
        while i < len(text.text):
            n = ord(text.text[i])
            if 33 <= n <= 126:
                n += key
                while n > 126:
                    n -= 94
                while n < 33:
                    n += 94
            text.text[i] = chr(n)
            i += 1
