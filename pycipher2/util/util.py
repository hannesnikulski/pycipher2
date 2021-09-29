# -*- coding: utf-8 -*-
# Author: Hannes Nikulski

from typing import List, Tuple, Union


def invDict(dictionary: dict) -> dict:
    newDict = {}

    for key, value in dictionary.items():
        newDict[value] = key

    return newDict


def getKeySquare(key: str, size: int, alphabet: str) -> None:
    keyword = ""

    for char in key + alphabet:
        if char not in keyword:
            keyword += char

    if len(keyword) != size * size:
        raise ValueError(f"cannot create {size}x{size} square with {len(keyword)} characters")

    return [keyword[i * size:(i + 1) * size] for i in range(size)]


def rmNoneAlphChars(text: str, alphabet: Union[list, str]) -> Tuple[str, List[Tuple[int, str]]]:
    result = ""
    rmChars = []

    for index, char in enumerate(text):
        if char not in alphabet:
            rmChars.append((index, char))

        else:
            result += char

    return result, rmChars


def rmIndices(text: str, indices: List[int]) -> str:
    result = text
    rmChars = []

    for index in reversed(sorted(indices)):
        rmChars.append((index, result[index]))
        result = result[:index] + result[index + 1:]

    return result, rmChars[::-1]


def addAlphChars(text: str, chars: List[Tuple[int, str]]) -> str:
    for index, char in chars:
        text = text[:index] + char + text[index:]

    return text


def interleave(string1: str, string2: str) -> str:
    result = [''] * (len(string1) + len(string2))
    result[::2] = string1
    result[1::2] = string2

    return "".join(result)
