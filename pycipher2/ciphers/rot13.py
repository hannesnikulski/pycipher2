# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

from pycipher2.ciphers.caesar import Caesar


class Rot13:
    """
    The Rot13 Cipher is a special case of the Caesar Cipher with a key of 13.

    For more information see https://en.wikipedia.org/wiki/ROT13.
    """

    def __init__(self, alphabet: list | str) -> None:
        self.alphabet = alphabet
        self.cipher = Caesar(13, self.alphabet)

    def decrypt(self, ciphertext: str) -> str:
        return self.cipher.decrypt(ciphertext)

    def encrypt(self, plaintext: str) -> str:
        return self.cipher.encrypt(plaintext)
