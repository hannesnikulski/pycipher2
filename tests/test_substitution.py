import unittest

from pycipher2 import Substitution


class TestSubstitution(unittest.TestCase):

    def test_encrypt(self):
        keys = ({"a": "4", "i": "1"},
                {"e": "3", "b": "a", "a": "b"})
        plaintext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = ('4bcdefgh1jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                      'bacd3fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

        for i, key in enumerate(keys):
            enc = Substitution(key).encrypt(plaintext)
            self.assertEqual(enc, ciphertext[i])

    def test_decrypt(self):
        keys = ({"a": "4", "i": "1"},
                {"e": "3", "b": "a", "a": "b"})
        ciphertext = '4bcd3fgh1jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        plaintext = ('abcd3fghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
                     '4acdefgh1jklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

        for i, key in enumerate(keys):
            dec = Substitution(key).decrypt(ciphertext)
            self.assertEqual(dec, plaintext[i])


if __name__ == '__main__':
    unittest.main()
