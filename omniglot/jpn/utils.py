import re


def is_only_katakana(word: str) -> bool:
    match = re.match(r"^[\u30A0-\u30FF]*$", word)

    return match is True


def is_only_hiragana(word: str) -> bool:
    match = re.match(r"^[\u3040-\u309F]*$", word)

    return match is True
