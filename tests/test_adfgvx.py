import unittest

from pycipher2 import ADFGVX


class TestADFGVX(unittest.TestCase):

    def test_encrypt(self):
        keys = (('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8', 'GERMAN'),
                ('dxkr3cvs5zw7bj9uti8ph0qg64mea1yl2nof', 'german'),
                ('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8', 'ciphers'))
        plaintext = 'abcdefghijklmnopqrstuvwxyz0123456789'
        ciphertext = ('GFXFFGXGAGAXGXVADAAXXVAVDFAXDAVGDDDVXFDDFGGGFDDXVVVAGFFAFGXDVDAGFAXVVFVX',
                      'AXFXXAFAGAVFVAXDFDDAAXDXVAGFVGDDXVVDAGFFGVVVGFFAXXXDVGGDGVAFFVGAXGFDDXDG',
                      'DXADFFGXFDXGVXDAGGFDVXFVDAXGAGVGDDFGVXVDADVFXAAAVFGXVAAFGXADAXFVGFGFDVVX')

        for i, key in enumerate(keys):
            enc = ADFGVX(*key).encrypt(plaintext)
            self.assertEqual(enc, ciphertext[i])

    def test_decrypt(self):
        keys = (('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8', 'GERMAN'),
                ('dxkr3cvs5zw7bj9uti8ph0qg64mea1yl2nof', 'german'),
                ('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8', 'ciphers'))
        plaintext = 'abcdefghijklmnopqrstuvwxyz0123456789'
        ciphertext = ('GFXFFGXGAGAXGXVADAAXXVAVDFAXDAVGDDDVXFDDFGGGFDDXVVVAGFFAFGXDVDAGFAXVVFVX',
                      'AXFXXAFAGAVFVAXDFDDAAXDXVAGFVGDDXVVDAGFFGVVVGFFAXXXDVGGDGVAFFVGAXGFDDXDG',
                      'DXADFFGXFDXGVXDAGGFDVXFVDAXGAGVGDDFGVXVDADVFXAAAVFGXVAAFGXADAXFVGFGFDVVX')

        for i, key in enumerate(keys):
            dec = ADFGVX(*key).decrypt(ciphertext[i])
            self.assertEqual(dec, plaintext)


if __name__ == '__main__':
    unittest.main()
