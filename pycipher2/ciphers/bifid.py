# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

import math

from pycipher2 import Polybius


class Bifid:
    """
    The Bifid Cipher...

    For more information see http://practicalcryptography.com/ciphers/bifid-cipher/.
    """

    def __init__(self, keySquare: str, period: int) -> None:
        self.keySquare = keySquare
        self.size = int(math.sqrt(len(self.keySquare)))
        self.period = period

        self.pbcipher = Polybius(self.keySquare, self.keySquare[:self.size])

    def decrypt(self, ciphertext: str) -> str:
        length = len(ciphertext)
        row, col = [], []

        for i in range(0, length, self.period):
            temp = []
            for j in range(self.period):
                if i + j >= length:
                    break

                temp.append(self.keySquare.index(ciphertext[i + j]) // self.size)
                temp.append(self.keySquare.index(ciphertext[i + j]) % self.size)

            halfLength = len(temp) // 2

            row += temp[:halfLength]
            col += temp[halfLength:]

        return "".join(self.keySquare[row[index] * self.size + col[index]] for index in range(len(row)))

    def encrypt(self, plaintext: str) -> str:
        pbEnc = self.pbcipher.encrypt(plaintext)

        evens = pbEnc[::2]
        odds = pbEnc[1::2]

        transposed = ""

        for index in range(0, len(plaintext), self.period):
            transposed += evens[index:index + self.period]
            transposed += odds[index:index + self.period]

        return self.pbcipher.decrypt(transposed)
