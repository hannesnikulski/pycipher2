# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

class ColTrans:
    """
    The Columnar Transposition Cipher is a cipher where the plaintext is written in columns that are permuted using the keyword.

    For more information see https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition.
    """

    def __init__(self, key: str) -> None:
        self.key = key
        self.keyLength = len(self.key)

        assert self.keyLength > 0, "key of length zero is not allowed"

        self.encIdx = self.getEncIdx()
        self.decIdx = self.getDecIdx()

    def getEncIdx(self):
        charIdxPairs = [(self.key[i], i) for i in range(self.keyLength)]
        swapPairs = [(k[1], i) for i, k in enumerate(sorted(charIdxPairs))]
        return [q[1] for q in sorted(swapPairs)]

    def getDecIdx(self):
        charIdxPairs = [(self.key[i], i) for i in range(self.keyLength)]
        return [q[1] for q in sorted(charIdxPairs)]

    def decrypt(self, ciphertext: str) -> str:
        length = len(ciphertext)
        plaintext = ["_"] * length

        tailLength = length % self.keyLength
        index = 0

        for i in range(self.keyLength):
            rowNum = length // self.keyLength
            if self.decIdx[i] < tailLength:
                rowNum += 1

            plaintext[self.decIdx[i]::self.keyLength] = ciphertext[index:index + rowNum]
            index += rowNum

        return "".join(plaintext)

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""

        for index in range(self.keyLength):
            ciphertext += plaintext[self.encIdx.index(index)::self.keyLength]

        return ciphertext
