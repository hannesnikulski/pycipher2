# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

class Caesar:
    """
    The Caesar Cipher is a substitution cipher where all letters are replaced by letters from a shifted alphabet.

    For more information see https://en.wikipedia.org/wiki/Caesar_cipher.
    """

    def __init__(self, key: int, alphabet) -> None:
        self.alphabet = alphabet
        self.length = len(self.alphabet)
        self.key = key % self.length

    def decrypt(self, ciphertext: str) -> str:
        return "".join([self.alphabet[(self.alphabet.index(char) - self.key)] for char in ciphertext])

    def encrypt(self, plaintext: str) -> str:
        return "".join([self.alphabet[(self.alphabet.index(char) + self.key) - self.length] for char in plaintext])
