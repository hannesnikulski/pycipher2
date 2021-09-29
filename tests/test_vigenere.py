import string
import unittest

from pycipher2 import Vigenere


class TestVigenere(unittest.TestCase):

    def test_encrypt(self):
        keys = ('german',
                'ciphers')
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('gftpesmlzvkysrfbqeyxlhwkedrncqkjxtiwqpdzocwvjfuicbpl',
                      'cjrkiwyjqyrpdfqxfywkmxemfdrteltmkyalsatrfhszhaymozgo')

        for i, key in enumerate(keys):
            enc = Vigenere(key, string.ascii_lowercase).encrypt(plaintext[i])
            self.assertEqual(enc, ciphertext[i])

    def test_decrypt(self):
        keys = ('german',
                'ciphers')
        plaintext = ('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
                     'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
        ciphertext = ('gftpesmlzvkysrfbqeyxlhwkedrncqkjxtiwqpdzocwvjfuicbpl',
                      'cjrkiwyjqyrpdfqxfywkmxemfdrteltmkyalsatrfhszhaymozgo')

        for i, key in enumerate(keys):
            dec = Vigenere(key, string.ascii_lowercase).decrypt(ciphertext[i])
            self.assertEqual(dec, plaintext[i])


if __name__ == '__main__':
    unittest.main()
