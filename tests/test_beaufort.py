import string
import unittest

from pycipher2 import Beaufort


class TestBeaufort(unittest.TestCase):

    def test_encrypt(self):
        keys = ('german',
                'ciphers')
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('gdpjwiaxjdqcurdxkwolxreqifrlykczlfsewtfzmyqnztgskhtn',
                      'chneammvagxtffotzqmyyhmsjfrraflcykktyevrddmrxokwwfkq')

        for i, key in enumerate(keys):
            enc = Beaufort(key, string.ascii_lowercase).encrypt(plaintext[i])
            self.assertEqual(enc, ciphertext[i])

    def test_decrypt(self):
        keys = ('german',
                'ciphers')
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('gdpjwiaxjdqcurdxkwolxreqifrlykczlfsewtfzmyqnztgskhtn',
                      'chneammvagxtffotzqmyyhmsjfrraflcykktyevrddmrxokwwfkq')

        for i, key in enumerate(keys):
            dec = Beaufort(key, string.ascii_lowercase).decrypt(ciphertext[i])
            self.assertEqual(dec, plaintext[i])


if __name__ == '__main__':
    unittest.main()
