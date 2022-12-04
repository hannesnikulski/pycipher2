# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

import math


class Playfair:
    """
    The Playfair Cipher.

    For more information see https://en.wikipedia.org/wiki/Playfair_cipher.
    """

    def __init__(self, keySquare: str, replaceChar: str) -> None:
        self.keySquare = keySquare
        self.replaceChar = replaceChar
        self.size = int(math.sqrt(len(self.keySquare)))

        assert len(self.keySquare) == self.size * self.size, f"Invalid key length {len(self.keySquare)} for size {self.size}"

    def decrypt(self, ciphertext: str) -> str:
        length = len(ciphertext)
        plaintext = ""

        for index in range(0, length, 2):
            i, j = self.keySquare.index(ciphertext[index]), self.keySquare.index(ciphertext[index + 1])

            iCol, iRow = i % self.size, i // self.size
            jCol, jRow = j % self.size, j // self.size

            if iRow == jRow:
                iCol = (iCol - 1) % self.size
                jCol = (jCol - 1) % self.size

            elif iCol == jCol:
                iRow = (iRow - 1) % self.size
                jRow = (jRow - 1) % self.size

            else:
                iCol, jCol = jCol, iCol

            plaintext += self.keySquare[iRow * self.size + iCol] + self.keySquare[jRow * self.size + jCol]

        return plaintext

    def encrypt(self, plaintext: str) -> str:
        length = len(plaintext)

        if length % 2 == 1:
            plaintext += self.replaceChar

        ciphertext = ""

        for index in range(0, length, 2):
            char1 = plaintext[index]
            char2 = plaintext[index + 1]

            if char1 == char2:
                char2 = self.replaceChar

            i, j = self.keySquare.index(char1), self.keySquare.index(char2)

            iCol, iRow = i % self.size, i // self.size
            jCol, jRow = j % self.size, j // self.size

            if iRow == jRow:
                iCol = (iCol + 1) % self.size
                jCol = (jCol + 1) % self.size

            elif iCol == jCol:
                iRow = (iRow + 1) % self.size
                jRow = (jRow + 1) % self.size

            else:
                iCol, jCol = jCol, iCol

            ciphertext += self.keySquare[iRow * self.size + iCol] + self.keySquare[jRow * self.size + jCol]

        return ciphertext
