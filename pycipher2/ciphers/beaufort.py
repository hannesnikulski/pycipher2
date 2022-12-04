# -*- coding: utf-8 -*-
# Author: Hannes Nikulski


class Beaufort:
    """
    The Beaufort Cipher is a polyalphabetic cipher and similar to the Vigenère cipher.

    For more information see https://en.wikipedia.org/wiki/Beaufort_cipher.
    """

    def __init__(self, key: str, alphabet: list | str) -> None:
        self.key = key
        self.alphabet = alphabet

        self.alphLength = len(self.alphabet)
        self.keyLength = len(self.key)

    def decrypt(self, ciphertext: str) -> str:
        return self.encrypt(ciphertext)

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""

        for index, char in enumerate(plaintext):
            ciphertext += self.alphabet[self.alphabet.index(self.key[index % self.keyLength]) - self.alphabet.index(char)]

        return ciphertext
