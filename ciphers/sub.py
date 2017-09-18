from .cipher import Cipher

class Sub(Cipher):
    """A class used to encrypt messages with the Substitution Cipher."""
    def check_key(self, key):
        """Makes sure that the key is the right format for this cipher.

        Parameters
        ----------
        key : list
            A list of lines from the key file.

        Returns
        -------
        bool
            True if the key is usable. False if not.
        """
        if len(key[0]) is not len(key[1]):
            return False
        return True

    def encrypt(self, plaintext, key):
        self._sub(plaintext, key[0], key[1])

    def decrypt(self, ciphertext, key):
        self._sub(ciphertext, key[1], key[0])

    def _sub(self, text, first, second):
        """The Substitution Cipher algorithm.

        Parameters
        ----------
        text : Text
            The plaintext or ciphertext
        first : string
            The characters to replace
        second: string
            The characters used to replace
        """
        d = dict(zip(first, second))

        i = 0
        while (i < len(text.text)):
            if text.text[i] in d:
                text.text[i] = d[text.text[i]]
            i += 1
