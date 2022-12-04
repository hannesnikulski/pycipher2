# -*- coding: utf-8 -*-
# Author: Hannes Nikulski


class Atbash:
    """
    The Atbash Cipher is a substitution cipher the uses the reversed alphabet to substitute letters.

    For more details see https://en.wikipedia.org/wiki/Atbash.
    """

    def __init__(self, alphabet: list | str) -> None:
        self.alphabet = alphabet

    def decrypt(self, ciphertext: str) -> str:
        return "".join([self.alphabet[-self.alphabet.index(char) - 1] for char in ciphertext])

    def encrypt(self, plaintext: str) -> str:
        return self.decrypt(plaintext)
