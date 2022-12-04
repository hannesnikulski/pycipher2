# -*- coding: utf-8 -*-
# Author: Hannes Nikulski


class Gronsfeld:
    """
    The Gronsfeld Cipher is a polyalphabetic cipher that uses a list of numbers as a key.

    For more information see https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Gronsfeld_cipher.
    """

    def __init__(self, key: list[int], alphabet: list | str) -> None:
        self.key = key
        self.alphabet = alphabet

        self.alphLength = len(self.alphabet)
        self.keyLength = len(self.key)

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""

        for index, char in enumerate(ciphertext):
            plaintext += self.alphabet[(self.alphabet.index(char) - self.key[index % self.keyLength]) % self.alphLength]

        return plaintext

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""

        for index, char in enumerate(plaintext):
            ciphertext += self.alphabet[(self.alphabet.index(char) + self.key[index % self.keyLength]) % self.alphLength]

        return ciphertext
