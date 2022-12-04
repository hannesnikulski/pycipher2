# -*- coding: utf-8 -*-
# Author: Hannes Nikulski


def invertDict(dictionary: dict) -> dict:
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


def separate(string: str, alphabet: list | str) -> tuple[str, list[tuple[str, int]]]:
    """
    Returns `string` argument with every character removed, which is not in the alphabet.
    The removed characters are also returned with their corresponding index in `text`.
    The two returned values can be recombinded with the `include` function.
    """
    cleanText = ""

    separatedChars = []

    for idx, char in enumerate(string):
        if char in alphabet:
            cleanText += char

        else:
            separatedChars.append((char, idx))

    return cleanText, separatedChars


def include(string: str, charIdxPairs: list[tuple[str, int]]) -> str:
    """
    Returns `string` with the characters in `charIdxPair` placed at their given index.
    """
    for char, idx in charIdxPairs:
        string = string[:idx] + char + string[idx:]

    return string


def removeIndices(string: str, indices: list[int]) -> str:
    """
    Returns `text` with the characters at the given indices removed.
    The removed character with their indices are also returned.
    """
    removedChars = []

    for idx in reversed(sorted(indices)):
        string = string[:idx] + string[idx + 1:]
        removedChars.append((idx, string[idx]))

    return string, removedChars[::-1]


def interleave(string1: str, string2: str) -> str:
    """
    Assumes equal lengths of the inputs
    """
    result = [''] * (len(string1) + len(string2))
    result[::2] = string1
    result[1::2] = string2

    return "".join(result)


def stringCount(string: str, substring: str) -> int:
    """
    Return the number of overlapping occurrences of substring. Similar to 'str.count'.
    """
    count = idx = 0

    while True:
        idx = string.find(substring, idx) + 1

        if idx > 0:
            count += 1

        else:
            return count
