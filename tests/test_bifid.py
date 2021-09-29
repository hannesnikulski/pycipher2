import unittest

from pycipher2 import Bifid


class TestBifid(unittest.TestCase):

    def test_encrypt(self):
        keys = (('phqgmeaylnofdxkrcvszwbuti', 4),
                ('ezrxdkuatgvncmiwhsqpyfblo', 5))
        plaintext = ('abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz',
                     'zyxwvutsrqponmlkiihgfedcbazyxwvutsrqponmlkiihgfedcba')
        ciphertext = ('nvayyphcifithoipgzostudglnkavyyhpicifhtiogpoztsdulgk',
                      'dxnxeuwhsmpcofqamkogyrfdckyskwntetcqbmotfcqdfgeikbfc')

        for i, key in enumerate(keys):
            enc = Bifid(*key).encrypt(plaintext[i])
            self.assertEqual(enc, ciphertext[i])

    def test_decrypt(self):
        keys = (('phqgmeaylnofdxkrcvszwbuti', 4),
                ('ezrxdkuatgvncmiwhsqpyfblo', 5))
        plaintext = ('abcdefghiiklmnopqrstuvwxyzabcdefghiiklmnopqrstuvwxyz',
                     'zyxwvutsrqponmlkiihgfedcbazyxwvutsrqponmlkiihgfedcba')
        ciphertext = ('nvayyphcifithoipgzostudglnkavyyhpicifhtiogpoztsdulgk',
                      'dxnxeuwhsmpcofqamkogyrfdckyskwntetcqbmotfcqdfgeikbfc')

        for i, key in enumerate(keys):
            dec = Bifid(*key).decrypt(ciphertext[i])
            self.assertEqual(dec, plaintext[i])


if __name__ == '__main__':
    unittest.main()
