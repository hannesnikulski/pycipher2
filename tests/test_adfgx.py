import unittest

from pycipher2 import ADFGX


class TestADFGX(unittest.TestCase):

    def test_encrypt(self):
        keys = (('ypgknveqzxmdhwcblfisrauto', 'GERMAN'),
                ('haoqkzdmpieslycbwvgufntrx', 'ciphers'))
        plaintext = 'abcdefghiklmnopqrstuvwxyz'
        ciphertext = ('FGGFAGDADDFGXFGGGXFAAADXFDADFDXAFXXFGADXAAGDFGXXXD',
                      'ADAFDDGAFAADXXFAXXXGGXDFADGXDGADFAFXXGXAGGGDGFFFFD')

        for i, key in enumerate(keys):
            enc = ADFGX(*key).encrypt(plaintext)
            self.assertEqual(enc, ciphertext[i])

    def test_decrypt(self):
        keys = (('ypgknveqzxmdhwcblfisrauto', 'GERMAN'),
                ('haoqkzdmpieslycbwvgufntrx', 'ciphers'))
        plaintext = 'abcdefghiklmnopqrstuvwxyz'
        ciphertext = ('FGGFAGDADDFGXFGGGXFAAADXFDADFDXAFXXFGADXAAGDFGXXXD',
                      'ADAFDDGAFAADXXFAXXXGGXDFADGXDGADFAFXXGXAGGGDGFFFFD')

        for i, key in enumerate(keys):
            dec = ADFGX(*key).decrypt(ciphertext[i])
            self.assertEqual(dec, plaintext)


if __name__ == '__main__':
    unittest.main()
