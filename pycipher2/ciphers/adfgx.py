# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

from pycipher2 import ColTrans
from pycipher2 import Polybius


class ADFGX:
    """
    The ADFGX Cipher uses the Polybius square and columnar transposition to encrypt or decrypt text.

    For more information see https://en.wikipedia.org/wiki/ADFGVX_cipher.
    """

    def __init__(self, keySquare: str, keyword: str) -> None:
        self.keySquare = keySquare
        self.keyword = keyword
        self.pbcipher = Polybius(self.keySquare, "ADFGX")

    def decrypt(self, ciphertext: str) -> str:
        pbEnc = ColTrans(self.keyword).decrypt(ciphertext)
        return self.pbcipher.decrypt(pbEnc)

    def encrypt(self, plaintext: str) -> str:
        pbEnc = self.pbcipher.encrypt(plaintext)
        return ColTrans(self.keyword).encrypt(pbEnc)
