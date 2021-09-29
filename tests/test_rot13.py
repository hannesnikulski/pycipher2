import string
import unittest

from pycipher2 import Rot13


class TestRot13(unittest.TestCase):

    def test_decrypt(self):
        plaintext = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        ciphertext = 'nopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklm'

        dec = Rot13(string.ascii_lowercase).decrypt(ciphertext)
        self.assertEqual(dec, plaintext)

    def test_encrypt(self):
        plaintext = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        ciphertext = 'nopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklm'

        enc = Rot13(string.ascii_lowercase).encrypt(plaintext)
        self.assertEqual(enc, ciphertext)


if __name__ == '__main__':
    unittest.main()
