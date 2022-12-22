import unittest

from eyecipher.cipher_message import CipherMessage

class TestStringMethods(unittest.TestCase):

    def test_sting_to_eye(self):
        test_string = ("Rb%P^-k=8]Jfb^@.q(/n\"=-Q!prH_q5" \
                       "3 HSa:.5fOLPJ3P-O3Qh?%8#K[cAQI\\" \
                       "5:>%94g+jX$j3g$SIKphV_oq/0L?>,AY<-`KP")

        # Convert string to eyes and back to string
        eyes = CipherMessage._str_to_eyes(test_string)
        message = CipherMessage(eyes = eyes)
        self.assertEqual(test_string, message.string)

if __name__ == '__main__':
    unittest.main()