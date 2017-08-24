# Copyright 2017 Dhruv Mehta

class Text:
    """A class to hold the text of a file."""
    def __init__(self, source):
        """Reads the text of a file and stores it in a string.

        Parameters
        ----------
        source : str
            The path of the source file.
        """
        with open(source, 'r') as f:
            r = f.read()

        self.text = list()

        for c in r:
            self.text.append(c)


    def record(self, destination):
        """Record data stored in this object in a file.

        Parameters
        ----------
        destination : str
            The path of the destination file.
        """
        with open(destination, 'w') as f:
            for c in self.text:
                f.write(c)
