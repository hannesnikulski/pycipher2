# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

from pycipher2.util import invertDict


class Substitution:
    """
    A simple substitution cipher that substitutes letters according to a given alphabet.

    For more information see https://en.wikipedia.org/wiki/Substitution_cipher.
    """

    def __init__(self, alphabet: dict) -> None:
        self.alphabet = alphabet
        self.invAlph = invertDict(self.alphabet)

    def decrypt(self, ciphertext: str) -> str:
        return "".join([self.invAlph[char] if char in self.invAlph else char for char in ciphertext])

    def encrypt(self, plaintext: str) -> str:
        return "".join([self.alphabet[char] if char in self.alphabet else char for char in plaintext])
