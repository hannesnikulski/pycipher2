# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

from pycipher2.util import interleave


class Railfence:
    """
    The Railfence Cipher is a transposition cipher.

    For more information see https://en.wikipedia.org/wiki/Rail_fence_cipher.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.period = 2 * (self.key - 1)

    def decrypt(self, ciphertext: str) -> str:
        length = len(ciphertext)
        remainder = length % self.period
        plaintext = ["_"] * length

        L0 = length // self.period + min(1, remainder)
        plaintext[::self.period] = ciphertext[:L0]

        offset = L0
        for index in range(1, self.key - 1):
            railLength = 2 * (length // self.period)

            if index < remainder:
                railLength += 1

            if index > (self.period - remainder):
                railLength += 1

            chunk = ciphertext[offset:offset + railLength]
            offset += railLength

            evens, odds = chunk[::2], chunk[1::2]

            plaintext[index::self.period] = evens
            plaintext[self.period - index::self.period] = odds

        plaintext[self.key - 1::self.period] = ciphertext[offset::]

        return "".join(plaintext)

    def encrypt(self, plaintext: str) -> str:
        ciphertext = plaintext[::self.period]

        for index in range(1, self.key - 1):
            ciphertext += interleave(plaintext[index::self.period], plaintext[self.period - index::self.period])

        ciphertext += plaintext[self.key - 1::self.period]

        return ciphertext
