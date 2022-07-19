# https://de.wikipedia.org/wiki/Koinzidenzindex

from typing import Union


def frequency(text: str, alphabet: Union[list, str]) -> dict[str, float]:
    """
    Returns the frequency of every character in the alphabet in the text.
    """
    length = len(text)
    return dict(zip(alphabet, [text.count(char) / length for char in alphabet]))


def compare(text1: str, text2: str) -> float:
    """
    Compares two texts character by character.
    Returns the ratio of equal characters (in the same position) to the length of the text.
    Similar to the 'Hamming Distance'.
    """
    # TODO: Warning for strings of different lengths?
    delta = [char1 == char2 for char1, char2 in zip(text1, text2)]
    return sum(delta) / len(delta)


def kullbackDistance(text1: str, text2: str, alphabet: Union[list, str]) -> float:
    """
    Returns a number, which represents the similarity between the two texts.
    """
    counts = [(text1.count(char), text2.count(char)) for char in alphabet]
    count1, count2 = list(zip(*counts))

    return sum(map(lambda pair: pair[0] * pair[1], counts)) / (sum(count1) * sum(count2))


def kullbackInformation(text: str, alphabet: Union[list, str]) -> float:
    """
    Returns the 'kullbackDistance' of the text with itself.
    """
    return kullbackDistance(text, text, alphabet)


def coincidence(text: str, alphabet: Union[list, str]) -> float:
    """
    Returns the index of coincidence of a text.
    """
    counts = [text.count(char) for char in alphabet]
    N = sum(counts)

    return sum(charCount * (charCount - 1) for charCount in counts) / (N * (N - 1))


def ngramDist(text: str, ngramSize: int) -> dict:
    """
    Returns the ngram Distribution of the given text.
    Assumes all non-alphabetic chars have been removed.
    """
    ngrams = {}

    for idx in range(len(text) - ngramSize + 1):
        block = text[idx:idx + ngramSize]

        if block in ngrams:
            ngrams[block] += 1

        else:
            ngrams[block] = 1

    return ngrams
