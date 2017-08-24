# Copyright 2017 Dhruv Mehta
from .cipher import Cipher

class ROT47(Cipher):
    """A class used to encrypt messages with the ROT47 Cipher."""
    def encrypt(self, plaintext, key):
        """Encrypt the plaintext with ROT47.

        Parameters
        ----------
        plaintext : Text
            The message to be encrypted.
        key : list
            Not needed for this cipher. Just pass None.
        """
        self._rot47(plaintext)


    def decrypt(self, ciphertext, key):
        """Decrypt the ciphertext with ROT47

        Parameters
        ----------
        ciphertext : str
            The message to be decrypted.
        key : list
            Not needed for this cipher. Just pass None.
        """
        self._rot47(ciphertext)

    def _rot47(self, text):
        """The ROT47 Cipher algorithm.

        Parameters
        ----------
        text : Text
            The plaintext or ciphertext.
        """
        i = 0
        while i < len(text.text):
            n = ord(text.text[i])
            if 33 <= n <= 126:
                n += 47
                if n > 126:
                    n -= 94
            text.text[i] = chr(n)
            i += 1
