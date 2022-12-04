# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

import math

from pycipher2.analysis import coincidence, compare


def friedmann(string: str, alphabet: str, languageIOC: float) -> float:
    """
    Returns an estimate for the key length of a polyalphabetic substitution cipher
    """
    nInv = 1 / len(alphabet)
    k = len(string)

    return (languageIOC - nInv) * k / ((k - 1) * coincidence(string, alphabet) - k * nInv + languageIOC)


def shiftTest(string: str, shift: int) -> float:
    """
    Returns the comparison of 'string' by itself, shifted by 'shift'
    """
    string1 = string[shift:]
    string2 = string[:-shift]

    return compare(string1, string2)


def chiSquaredTest(string: str, alphabet: str, letterFrequency: dict[str, float]) -> float:
    """
    Compares the distribution of the letter frequency of 'string' with 'letterFrequency'
    """
    length = len(string)

    return sum((string.count(char) / length - letterFrequency[char]) ** 2 / letterFrequency[char] for char in alphabet) / length


def fitnessScore(text: str, ngrams: dict[str, float]) -> float:
    blocksize = len(next(iter(ngrams.keys())))
    total = sum(ngrams.values())
    zeroProb = math.log10(0.01 / total)
    score = 0

    for idx in range(len(text) + 1 - blocksize):
        block = text[idx:idx + blocksize]

        if block in ngrams:
            score += math.log10(block[ngrams])
            continue

        score += zeroProb

    return score
