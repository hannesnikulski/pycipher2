import string
import unittest

from pycipher2 import Affine


class TestAffine(unittest.TestCase):

    def test_decrypt(self):
        ciphertext = 'pmjgdaxurolifczwtqnkhebyvspmjgdaxurolifczwtqnkhebyvs'
        plaintexts = ['yfmtahovcjqxelszgnubipwdkryfmtahovcjqxelszgnubipwdkr',
                      'onmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqp',
                      'jarizqhypgxofwnevmdulctkbsjarizqhypgxofwnevmdulctkbs',
                      'pmjgdaxurolifczwtqnkhebyvspmjgdaxurolifczwtqnkhebyvs',
                      'tmfyrkdwpibungzslexqjcvohatmfyrkdwpibungzslexqjcvoha',
                      'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz']

        for i, key in enumerate(((7, 3), (3, 25), (9, 12), (1, 0), (19, 18), (23, 15))):
            dec = Affine(key, string.ascii_lowercase + string.ascii_uppercase).decrypt(ciphertext)
            self.assertEqual(dec.upper(), plaintexts[i].upper())

    def test_encrypt(self):
        plaintext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertexts = ['hijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg',
                       'dgjmpsvybehknqtwzcfiloruxadgjmpsvybehknqtwzcfiloruxa',
                       'afkpuzejotydinsxchmrwbglqvafkpuzejotydinsxchmrwbglqv',
                       'ovcjqxelszgnubipwdkryfmtahovcjqxelszgnubipwdkryfmtah',
                       'sbktcludmvenwfoxgpyhqzirajsbktcludmvenwfoxgpyhqziraj',
                       'pmjgdaxurolifczwtqnkhebyvspmjgdaxurolifczwtqnkhebyvs']

        for i, key in enumerate(((1, 7), (3, 3), (5, 0), (7, 14), (9, 18), (23, 15))):
            enc = Affine(key, string.ascii_lowercase + string.ascii_uppercase).encrypt(plaintext)
            self.assertEqual(enc.upper(), ciphertexts[i].upper())


if __name__ == '__main__':
    unittest.main()
