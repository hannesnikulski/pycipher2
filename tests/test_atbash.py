import string
import unittest

from pycipher2 import Atbash


class TestAtbash(unittest.TestCase):

    def test_decrypt(self):
        ciphertext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        plaintext = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'

        dec = Atbash(string.ascii_uppercase + string.ascii_lowercase).decrypt(ciphertext)
        self.assertEqual(dec, plaintext)

    def test_encrypt(self):
        plaintext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'

        enc = Atbash(string.ascii_uppercase + string.ascii_lowercase).encrypt(plaintext)
        self.assertEqual(enc, ciphertext)


if __name__ == '__main__':
    unittest.main()
