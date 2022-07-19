# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

from typing import Union


def invDict(dictionary: dict) -> dict:
    """
    Inverts a dicitonary. Values have to be unique.
    """
    newDict = {}

    for key, value in dictionary.items():
        newDict[value] = key

    return newDict


def getKeySquare(key: str, size: int, alphabet: str) -> None:
    """
    Returns a key square
    """
    keyword = ""

    for char in key + alphabet:
        if char not in keyword:
            keyword += char

    if len(keyword) != size * size:
        raise ValueError(f"cannot create {size}x{size} square with {len(keyword)} characters")

    return [keyword[i * size:(i + 1) * size] for i in range(size)]


def separate(text: str, alphabet: Union[list, str]) -> tuple[str, list[tuple[str, int]]]:
    """
    Returns `text` argument with every character removed, which is not in the alphabet.
    The removed characters are also returned with their corresponding index in `text`.
    The two returned values can be recombinded with the `include` function.
    """
    cleanText = ""

    removedChars = []

    for idx, char in enumerate(text):
        if char in alphabet:
            cleanText += char

        else:
            removedChars.append((char, idx))

    return cleanText, removedChars


def include(text: str, charIdxPairs: list[tuple[str, int]]) -> str:
    """
    Returns `text` with the characters in `charIdxPair` placed at their given index.
    """
    for char, idx in charIdxPairs:
        text = text[:idx] + char + text[idx:]

    return text


def remove(text: str, indices: list[int]) -> str:
    """
    Returns `text` with the characters at the given indices removed.
    The removed character with their indices are also returned.
    """
    removedChars = []

    for idx in reversed(sorted(indices)):
        text = text[:idx] + text[idx + 1:]
        removedChars.append((idx, text[idx]))

    return text, removedChars[::-1]


def interleave(string1: str, string2: str) -> str:
    """
    Assumes equal lengths of the inputs
    """
    result = [''] * (len(string1) + len(string2))
    result[::2] = string1
    result[1::2] = string2

    return "".join(result)
