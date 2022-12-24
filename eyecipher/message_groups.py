from eyecipher.cipher_message import CipherMessage


class MessageGroup():
    """
    A class representing a group of messages
    """
    def __init__(self, messages = []):
        """
        Args:
            messages(list[CipherMessage])
        """
        self.messages = messages

    def __add__(self, other):
        pass

def main():
    pass

if __name__ == "__main__":
    main()