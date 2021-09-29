import string
import unittest

from pycipher2 import Autokey


class TestAutokey(unittest.TestCase):

    def test_encrypt(self):
        keys = ('german',
                'ciphers')
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba')
        ciphertext = ('gftpesgikmoqsuwyacegikmoqsuwyacegikmoqsuwyacegikmoqs',
                      'bgmdzllrpnljhfdbzxvtrpnljhfdbzxvtrpnljhfdbzxvtrpnljh')

        for i, key in enumerate(keys):
            enc = Autokey(key, string.ascii_lowercase).encrypt(plaintext[i])
            self.assertEqual(enc, ciphertext[i])

    def test_decrypt(self):
        keys = ('german',
                'ciphers')
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba')
        ciphertext = ('gftpesgikmoqsuwyacegikmoqsuwyacegikmoqsuwyacegikmoqs',
                      'bgmdzllrpnljhfdbzxvtrpnljhfdbzxvtrpnljhfdbzxvtrpnljh')

        for i, key in enumerate(keys):
            enc = Autokey(key, string.ascii_lowercase).decrypt(ciphertext[i])
            self.assertEqual(enc, plaintext[i])


if __name__ == '__main__':
    unittest.main()
