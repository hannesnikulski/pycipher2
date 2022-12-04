# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

from pycipher2.util import stringCount


def frequency(string: str, alphabet: list | str) -> dict[str, float]:
    """
    Returns the frequency of every character in the alphabet in the string.
    """
    return {char: string.count(char) for char in alphabet}


def compare(string1: str, string2: str) -> float:
    """
    Compares two texts character by character.
    Returns the ratio of equal characters (in the same position) to the length of the text.
    Similar to the 'Hamming Distance'.
    """
    assert len(string1) == len(string2), "Strings have to be of equal lengths"

    return sum(char1 == char2 for char1, char2 in zip(string1, string2)) / len(string1)


def kullbackDistance(string1: str, string2: str, alphabet: list | str) -> float:
    """
    Returns a number, which represents the similarity between two strings.
    """
    count1 = [string1.count(char) for char in alphabet]
    count2 = [string2.count(char) for char in alphabet]

    return sum(c1 * c2 for c1, c2 in zip(count1, count2)) / (sum(count1) * sum(count2))


def kullbackInformation(string: str, alphabet: list | str) -> float:
    """
    Returns the 'kullbackDistance' of the string with itself.
    """
    return kullbackDistance(string, string, alphabet)


def coincidence(string: str, alphabet: list | str) -> float:
    """
    Returns the index of coincidence of a string.
    """
    counts = [string.count(char) for char in alphabet]
    totalSum = sum(counts)

    return sum(charCount * (charCount - 1) for charCount in counts) / (totalSum * (totalSum - 1))


def ngramDist(string: str, ngramSize: int) -> dict:
    """
    Returns the ngram Distribution of the given text.
    Assumes all non-alphabetic chars have been removed.
    """
    ngrams = {}

    for idx in range(len(string) - ngramSize + 1):
        block = string[idx:idx + ngramSize]

        if block not in ngrams:
            ngrams[block] = stringCount(string, block)

    return ngrams
