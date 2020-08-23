from typing import List

from documental.token import NumberToken, Token

from ..numbers import NumberConverter


class JapaneseNumberConverter(NumberConverter):
    @staticmethod
    def parse(text: str) -> Token:
        raise NotImplementedError()

    @staticmethod
    def convert_text(text: str) -> NumberToken:
        raise NotImplementedError()

    @staticmethod
    def verbalize_number(number: int) -> List[Token]:
        raise NotImplementedError()
