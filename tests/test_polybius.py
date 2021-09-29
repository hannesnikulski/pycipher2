import unittest

from pycipher2 import Polybius


class TestPolybius(unittest.TestCase):

    def test_encrypt(self):
        keys = (('phqgiumeaylnofdxkrcvstzwb', 'ABCDE'),
                ('uqfigkydlvmznxephrswaotcb', 'BCDEF'))
        plaintext = ('abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz',
                     'abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz')
        ciphertext = ('BDEEDDCEBCCDADABAEAEDBCABBCBCCAAACDCEAEBBADEEDDABEECBDEEDDCEBCCDADABAEAEDBCABBCBCCAAACDCEAEBBADEEDDABEEC',
                      'FBFFFECDDFBDBFECBEBECBCEDBDDFCEBBCEDEEFDBBCFEFDECCDCFBFFFECDDFBDBFECBEBECBCEDBDDFCEBBCEDEEFDBBCFEFDECCDC')

        for i, key in enumerate(keys):
            enc = Polybius(*key).encrypt(plaintext[i])
            self.assertEqual(enc, ciphertext[i])

    def test_decrypt(self):
        keys = (('phqgiumeaylnofdxkrcvstzwb', 'ABCDE'),
                ('uqfigkydlvmznxephrswaotcb', 'BCDEF'))
        plaintext = ('abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz',
                     'abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz')
        ciphertext = ('BDEEDDCEBCCDADABAEAEDBCABBCBCCAAACDCEAEBBADEEDDABEECBDEEDDCEBCCDADABAEAEDBCABBCBCCAAACDCEAEBBADEEDDABEEC',
                      'FBFFFECDDFBDBFECBEBECBCEDBDDFCEBBCEDEEFDBBCFEFDECCDCFBFFFECDDFBDBFECBEBECBCEDBDDFCEBBCEDEEFDBBCFEFDECCDC')

        for i, key in enumerate(keys):
            dec = Polybius(*key).decrypt(ciphertext[i])
            self.assertEqual(dec, plaintext[i])


if __name__ == '__main__':
    unittest.main()
