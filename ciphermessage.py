
import os

class CipherMessage():
    def __init__(self, file_name = None):
        self.eyes = None
        if file_name != None:
            f = open(file_name)
            self.eyes = f.readline()
            f.close()

    @property
    def eye_list(self):
        return [ i for i in self.eyes ]

    @property
    def trigram_list(self):
        # NOTE: This is assuming input is mod 3. If not, it truncates the last off
        return [ self.eyes[i:i+3] for i in range(0, len(self.eyes), 3) ]

    @property
    def base_10(self):
        return [ int(i, 5) for i in self.trigram_list ]
    
    @property
    def string(self):
        return ''.join([ chr(i+32) for i in self.base_10])
    


if __name__ == "__main__":
    # Define cipher file locations
    east1 =  os.path.join("cipher_data", "interleaved", "east1")
    #west1 =
    print(east1)

    message = CipherMessage(file_name = east1)
    #import pdb; pdb.set_trace()
    print(message.eyes)
    print(message.trigram_list)
    print(message.base_10)
    print(message.string)