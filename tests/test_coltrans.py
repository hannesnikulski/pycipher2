import unittest

from pycipher2 import ColTrans


class TestColtrans(unittest.TestCase):

    def test_encrypt(self):
        keys = ('german',
                'ciphers')
        plaintext = ('abcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyz')
        ciphertext = ('ekqwbhntzagmsydjpvflrxciou',
                      'ahovelszdkrybipwcjqxfmtgnu')

        for i, key in enumerate(keys):
            enc = ColTrans(key).encrypt(plaintext[i])
            self.assertEqual(enc, ciphertext[i])

    def test_decrypt(self):
        keys = ('german',
                'ciphers')
        plaintext = ('abcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyz')
        ciphertext = ('ekqwbhntzagmsydjpvflrxciou',
                      'ahovelszdkrybipwcjqxfmtgnu')

        for i, key in enumerate(keys):
            dec = ColTrans(key).decrypt(ciphertext[i])
            self.assertEqual(dec, plaintext[i])


if __name__ == '__main__':
    unittest.main()
