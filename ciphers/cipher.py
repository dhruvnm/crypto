#Copyright 2017 Dhruv Mehta
from abc import ABC, abstractmethod
from sys import path
path.append("..")
from text import Text

class Cipher(ABC):
    """An abstract class that serves as a template for the other ciphers."""
    @abstractmethod
    def encrypt(self, plaintext, key):
        """A method to encrypt the plaintext.

        Parameters
        ----------
        plaintext : Text
            The message to be encrypted.
        key : list
            The key used to encrypt the message.
        """
        pass

    @abstractmethod
    def decrypt(self, ciphertext, key):
        """A method to decrypt the ciphertext.

        Parameters
        ----------
        ciphertext : str
            The message to be decrypted.
        key : str
            The key used to encrypt the message.
        """
        pass
