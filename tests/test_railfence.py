import unittest

from pycipher2 import Railfence


class TestRailfence(unittest.TestCase):

    def test_encrypt(self):
        keys = (3, 6, 7, 8)
        plaintext = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        ciphertext = ('aeimquycgkoswbdfhjlnprtvxzbdfhjlnprtvxzcgkoswaeimquy',
                      'akueoybjltvdfnpxzcimswcgmqwdhnrxbhlrvegoqyaiksufpzjt',
                      'amykwblnxzjlvxckowaimuydjpvbhntzeiqucgosfhrtdfprgseq',
                      'aocqbnpbdprcmqaeosdlrzfnteksygmufjtxhlvzgiuwikwyhvjx')

        for i, key in enumerate(keys):
            enc = Railfence(key).encrypt(plaintext)
            self.assertEqual(enc, ciphertext[i])

    def test_decrypt(self):
        keys = (3, 6, 7, 8)
        ciphertext = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        plaintext = ('annobpoqcrpsdtquevrwfxsygztahbucidvejfwgkhxiljykmlzm',
                     'agrblvmcshbitdnwoeujckvfpxqgwldmxhrysiyneozjtzukapfq',
                     'afoxgowphypgbhqziqxrjaricjsbksytlctkdludmuzvnevmenwf',
                     'aelszgowphatmfbgnubiqxrjcvohcipwdksytlexqjdkryfmuzvn')

        for i, key in enumerate(keys):
            dec = Railfence(key).decrypt(ciphertext)
            self.assertEqual(dec, plaintext[i])


if __name__ == '__main__':
    unittest.main()
