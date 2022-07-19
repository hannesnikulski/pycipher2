import math
from pycipher2.analysis.analysis import coincidence, compare


def friedmann(text: str, alphabet: str, languageIOC: float) -> float:
    """
    Returns an estimate for the key length of a polyalphabetic substitution cipher
    """
    nInv = 1 / len(alphabet)
    k = len(text)

    return (languageIOC - nInv) * k / ((k - 1) * coincidence(text, alphabet) - k * nInv + languageIOC)


def shiftTest(text: str, shift: int) -> float:
    text1 = text[shift:]
    text2 = text[:-shift]

    return compare(text1, text2)


def kasiski(text: str):
    pass


def chiSquaredTest(text: str, alphabet: str, letterFrequency: dict[str, float]) -> float:
    """
    compares two distributions
    """
    length = len(text)

    return sum((text.count(char) / length - letterFrequency[char]) ** 2 / letterFrequency[char] for char in alphabet) / length


def fitnessScore(text: str, ngrams: dict[str, float]) -> float:
    blocksize = len(ngrams.keys()[0])
    total = sum(ngrams.values())
    zeroProp = math.log10(0.01 / total)
    score = 0

    for idx in range(len(text) - blocksize + 1):
        block = text[idx:idx + blocksize]

        if block in ngrams:
            score += math.log10(block[ngrams])

            continue

        score += zeroProp

    return score
