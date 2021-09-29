import string
import unittest

from pycipher2 import Gronsfeld


class TestGronsfeld(unittest.TestCase):

    def test_encrypt(self):
        keys = ([2, 7, 8, 1, 3, 9, 3],
                [2, 7, 8, 1, 0, 3, 9, 3])
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('cikehojjprlovqqwysvcxxdfzcjeekmgjqllrtnqxssyauxezzfh',
                      'cikeeipkkqsmmqxssyauuyfaagiccgniioqkkovqqwysswdyyega')

        for i, key in enumerate(keys):
            enc = Gronsfeld(key, string.ascii_lowercase).encrypt(plaintext[i])
            self.assertEqual(enc, ciphertext[i])

    def test_decrypt(self):
        keys = ([2, 7, 8, 1, 3, 9, 3],
                [2, 7, 8, 1, 0, 3, 9, 3])
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('cikehojjprlovqqwysvcxxdfzcjeekmgjqllrtnqxssyauxezzfh',
                      'cikeeipkkqsmmqxssyauuyfaagiccgniioqkkovqqwysswdyyega')

        for i, key in enumerate(keys):
            dec = Gronsfeld(key, string.ascii_lowercase).decrypt(ciphertext[i])
            self.assertEqual(dec, plaintext[i])


if __name__ == '__main__':
    unittest.main()
