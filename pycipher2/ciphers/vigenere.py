# -*- coding: utf-8 -*-
# Author: Hannes Nikulski


class Vigenere:
    """
    The Vigenère Cipher is a polyalphabetic cipher.

    For more information see https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher.
    """

    def __init__(self, key: str, alphabet: list | str) -> None:
        self.key = key
        self.alphabet = alphabet

        self.alphLength = len(self.alphabet)
        self.keyLength = len(self.key)

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""

        for index, char in enumerate(ciphertext):
            plaintext += self.alphabet[(self.alphabet.index(char) - self.alphabet.index(self.key[index % self.keyLength])) % self.alphLength]

        return plaintext

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""

        for index, char in enumerate(plaintext):
            ciphertext += self.alphabet[(self.alphabet.index(char) + self.alphabet.index(self.key[index % self.keyLength])) % self.alphLength]

        return ciphertext
