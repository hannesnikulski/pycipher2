# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

import math


class Polybius:
    """
    The Polybius Cipher is a substitution cipher where every plaintext character is encoded with two characters.

    For more information see https://en.wikipedia.org/wiki/Polybius_square.
    """

    def __init__(self, keySquare: str, cipherChars: str) -> None:
        self.keySquare = keySquare
        self.size = int(math.sqrt(len(self.keySquare)))
        self.chars = cipherChars

        assert len(self.keySquare) == self.size * self.size, f"Invalid key length {len(self.keySquare)} for size {self.size}"

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""

        length = len(ciphertext)

        for index in range(0, length, 2):
            char1 = ciphertext[index]
            char2 = ciphertext[index + 1]

            i, j = self.chars.index(char1), self.chars.index(char2)
            plaintext += self.keySquare[i * self.size + j]

        return plaintext

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""

        for char in plaintext:
            index = self.keySquare.index(char)
            ciphertext += self.chars[index // self.size] + self.chars[index % self.size]

        return ciphertext
