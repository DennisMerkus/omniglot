import re
from typing import List

from num2words import num2words

from omnilingual import LanguageCode, PartOfSpeech
from omnilingual.features import NumType
from ..numbers import NumberConverter, is_number
from documental.token import (
    Token,
    NumberToken,
    WordToken,
    PunctuationToken,
)


class FrenchNumberConverter(NumberConverter):
    @staticmethod
    def parse(text: str) -> Token:
        text = text.strip()

        if is_number(text):
            number = int(text)

            return NumberToken(
                text,
                number,
                FrenchNumberConverter.convert_number(number),
                NumType.Card,
                language=LanguageCode.French,
            )
        else:
            # Parse word as a number
            return WordToken(text, LanguageCode.French, pos=PartOfSpeech.Number)

    @staticmethod
    def verbalize_number(number: int) -> List[Token]:
        text: str = num2words(number, lang="fr")

        pronunciation: List[Token] = []

        tokens: List[str] = re.split(r"(\W+)", text)

        for token in tokens:
            if token == "-" or token == " ":
                pronunciation.append(
                    PunctuationToken("-", sticks_left=True, sticks_right=True)
                )
            else:
                pronunciation.append(
                    WordToken(token, LanguageCode.French, pos=PartOfSpeech.Number)
                )

        return pronunciation
