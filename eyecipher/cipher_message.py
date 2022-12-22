import numpy as np
import os
import random

from eyecipher.encoding_utils import numberToBase

class CipherMessage():
    def __init__(self, file_name = None, eyes = None, msg_str = None, name = "Message"):
        """
        A representation of a Noita eye Cipher message. At least one of the three
        arguments must be non-null.

        Args:
            file_name(str): Fully qualified file path with eye data to read in.
            eyes(str): String representation of eye glyphs, with each eye represented
                       by a number between 0-4. 
            msg_str(str): String representation of the message
            name (str): Optional name to be used to label the message 

        Attributes:
            eye_list
            trigram_list
            base_10
            string
        """
        self.name = name

        if file_name != None:
            f = open(file_name)
            self.eyes = f.readline()
            f.close()
        elif eyes != None:
            self.eyes = eyes
        elif msg_str != None:
            self.eyes = self._str_to_eyes(msg_str)
        else:
            raise

    @property
    def eye_list(self):
        return [ i for i in self.eyes ]

    @property
    def trigrams(self):
        # NOTE: This is assuming input is mod 3. If not, it truncates the last off
        return [ self.eyes[i:i+3] for i in range(0, len(self.eyes), 3) ]

    @property
    def base_10(self):
        return [ int(i, 5) for i in self.trigrams ]
    
    @property
    def string(self):
        return ''.join([ chr(i+32) for i in self.base_10])
    
    def __add__(self, other):
        return CipherMessage(eyes = self.eyes + other.eyes)

    def __str__(self):
        return self.string

    @staticmethod
    def _str_to_eyes(msg_str):
        """
        Turns a string representation into an eye pattern

        Args:
            msg_str (string): String representation of the message
        Returns:
            eyes (string): String representation of eye glyphs
        """
        base_10_str = [ord(char)-32 for char in msg_str]
        base_5_trigrams = [np.base_repr(int(num), base = 5) for num in base_10_str]
        # Pad everything to 3 digits
        base_5_trigrams = [format(num, "0>3") for num in base_5_trigrams]
        eyes = ''.join(i for i in base_5_trigrams)
        return eyes

    def shuffle_eyes(self):
        """
        Shuffles the eyes within the message into a pseudo-random order

        Returns: 
            (CipherMessage): A shuffled CipherMessage
        """
        shuffled_eyes = ''.join(random.sample(self.eyes,len(self.eyes)))
        return CipherMessage(eyes = shuffled_eyes)

    def shuffle_trigrams(self):
        """
        Shuffles the trigrams within the message into a pseudo-random order

        Returns: 
            (CipherMessage): A shuffled CipherMessage
        """
        shuffled_eyes = ''.join(random.sample(self.string,len(self.string)))
        return CipherMessage(msg_str = shuffled_eyes)

    def random_eyes(self, length = None):
        """
        generates random set of eye glyphs. If no length is given,
        assumes the length of the current cipher text

        Args:
            len(int): length of eye glyph message to generate
        Returns: 
            (CipherMessage): A shuffled CipherMessage
        """
        if length == None:
                length = len(self.eyes)

        random_eyes = [random.randrange(0,5,1) for i in range(length)]
        random_eyes = ''.join(str(i) for i in random_eyes)
        return CipherMessage(eyes = random_eyes)

if __name__ == "__main__":
    # Define cipher file locations
    east1 =  os.path.join("cipher_data", "interleaved", "east1")
    #west1 =
    print(east1)

    message = CipherMessage(file_name = east1)
    import pdb; pdb.set_trace()
    print(message.eyes)
    print(message.trigrams)
    print(message.base_10)
    print(message.string)