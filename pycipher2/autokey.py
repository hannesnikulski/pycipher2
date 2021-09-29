# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

from typing import Union


class Autokey:
    """
    The Autokey Cipher is a polyalphabetic cipher and a variant of the Vigenère Cipher.

    For more information see https://en.wikipedia.org/wiki/Autokey_cipher.
    """

    def __init__(self, key: str, alphabet: Union[list, str]) -> None:
        self.key = key
        self.alphabet = alphabet

        self.alphLength = len(self.alphabet)

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        key = self.key

        for index, char in enumerate(ciphertext):
            char = self.alphabet[(self.alphabet.index(char) - self.alphabet.index(key[index])) % self.alphLength]
            key += char
            plaintext += char

        return plaintext

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        key = self.key

        for index, char in enumerate(plaintext):
            key += char
            char = self.alphabet[(self.alphabet.index(char) + self.alphabet.index(key[index])) % self.alphLength]
            ciphertext += char

        return ciphertext
