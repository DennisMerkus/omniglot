from typing import List

from .tokens import NumberToken, Token


def is_number(text: str) -> bool:
    try:
        int(text)

        return True
    except ValueError:
        return False


def is_float(text: str) -> bool:
    try:
        float(text)

        return True
    except ValueError:
        return False


class NumberConverter(object):
    @staticmethod
    def parse(text: str) -> Token:
        raise NotImplementedError()

    @staticmethod
    def convert_text(text: str) -> NumberToken:
        raise NotImplementedError()

    @staticmethod
    def convert_number(number: int) -> List[Token]:
        raise NotImplementedError()
