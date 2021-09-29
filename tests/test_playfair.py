import unittest

from pycipher2 import Playfair


class TestPlayfair(unittest.TestCase):

    def test_decrypt(self):
        ciphertext = 'abcdefghiklmnopqrstuvwxyzabcdefghiklmnopqrstuvwxyz'
        keys = ('lsfdpxwirnyveamoqgkchbtzu',
                'dytqplngirabskxcvoemzufwh',
                'ecsyinfmkpdrtuvgwqzbolaxh',
                'xquwfstzgeipboalykdnvrmch',
                'bxuthifmzrweasdovlpgcqnyk')
        plaintext = ['vzkpitotrgpyxcscwdbzwslxkruqfatetxodnpclkwfbbmxnah',
                     'xaazowrfqircgvqtgxyfeubpclavqcotwraivrmtpigfvbhkdu',
                     'hqercnboypafegmbtcrtrbzxqxwinonwbhfxfphnwtamtuzlxu',
                     'opdofhecblkvdatrvtzqcxqlebomngwevaynhkbiryesxmufkt',
                     'wukwfxdkrcauclvyzduxoetqmscoswrvbrngulglkfzyxlebpt']

        for i, key in enumerate(keys):
            dec = Playfair(key, "x").decrypt(ciphertext)
            self.assertEqual(dec, plaintext[i])

    def test_encrypt(self):
        keys = ('czbniwemuorkpdslqfxagthyv',
                'ohnuwkdbtiepyzxcsqamlgrvf',
                'pslqofaiymcnwtuhdxezbkgrv',
                'xqvlpnakrsewfcyhutdbgziom',
                'xbhpuvmiyesdnwlakcrgfzotq')
        plaintext = 'abcdefghiklmnopqrstuvwxyzabcdefghiklmnopqrstuvwxyz'
        ciphertext = ['finrmqtyzsfwiukfkryegoyniqnzkulhvbrqubmslkkvoyultn',
                      'qtskxlhdkdfcuhysgqztfuezavkqkplrwdeoqwhernadtuimzx',
                      'fknhhybxagoiussokqucgueidmphxzibxfgsaupsyqqnzoxgme',
                      'sudowcxgvfporgxvsndtqfpeqwdyhceitgrvgsmllakbtqeqwm',
                      'kxknvqcumcdechutawqpyspvfkhklmqaingdidthtgwfxespmt']

        for i, key in enumerate(keys):
            enc = Playfair(key, "x").encrypt(plaintext)
            self.assertEqual(enc, ciphertext[i])


if __name__ == '__main__':
    unittest.main()
