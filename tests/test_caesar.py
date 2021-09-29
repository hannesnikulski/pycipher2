import string
import unittest

from pycipher2 import Caesar


class TestCaesar(unittest.TestCase):

    def test_decrypt(self):
        ciphertext = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        plaintexts = ['xyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvw',
                      'vwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstu',
                      'stuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqr',
                      'pqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmno',
                      'lmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijk',
                      'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                      'bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza']

        for i, key in enumerate((3, 5, 8, 11, 15, 0, 25)):
            dec = Caesar(key, string.ascii_lowercase).decrypt(ciphertext)
            self.assertEqual(dec, plaintexts[i])

    def test_encrypt(self):
        plaintext = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        ciphertexts = ['bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza',
                       'cdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzab',
                       'efghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd',
                       'hijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg',
                       'jklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghi',
                       'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                       'zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy']

        for i, key in enumerate((1, 2, 4, 7, 9, 0, 25)):
            enc = Caesar(key, string.ascii_lowercase).encrypt(plaintext)
            self.assertEqual(enc, ciphertexts[i])


if __name__ == '__main__':
    unittest.main()
