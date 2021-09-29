# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

import math
from typing import Tuple, Union


class Affine:
    """
    The Affine Cipher is a substitution cipher that maps the index of every letter of the text using an affine function.

    encryption:
    - `x -> a * x + b`

    decryption:
    - `x -> a^-1 * x - b`

    Where `a^-1` is the modular multiplicative inverse of `a`.

    For more information see https://en.wikipedia.org/wiki/Affine_cipher.
    """

    def __init__(self, key: Tuple[int, int], alphabet: Union[list, str]) -> None:
        self.a, self.b = key
        self.alphabet = alphabet
        self.length = len(self.alphabet)

        assert math.gcd(self.a, self.length) == 1, ValueError(f"First element of key ({self.a}) has to be coprime with the length of the alphabet ({self.length})")

        # Note: modular multiplicative inverse, works only in Python 3.8+
        self.inv_a = pow(self.a, -1, self.length)

    def decrypt(self, ciphertext: str) -> str:
        return "".join([self.alphabet[(self.inv_a * (self.alphabet.index(char) - self.b)) % self.length] for char in ciphertext])

    def encrypt(self, plaintext: str) -> str:
        return "".join([self.alphabet[(self.a * self.alphabet.index(char) + self.b) % self.length] for char in plaintext])
