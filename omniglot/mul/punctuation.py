from typing import List

from documental.token import PunctuationToken, Token, WordToken

punctuation = [
    "-",
    "—",
    "！",  # Chinese
    "「",
    "」",
    "：",
]

punctuation_sticks_left = [".", ",", "?", "!", ")", ">", "}", "]"]

punctuation_sticks_right = ["(", ">", "{", "[", "«", "»"]

all_punctuation = punctuation + punctuation_sticks_left + punctuation_sticks_right


def convert_punctuation_tokens(tokens: List[Token]) -> List[Token]:
    converted_tokens: List[Token] = []

    for token in tokens:
        if isinstance(token, WordToken) and token.text in all_punctuation:
            converted_tokens.append(
                PunctuationToken(
                    token.text,
                    sticks_left=token.text in punctuation_sticks_left,
                    sticks_right=token.text in punctuation_sticks_right,
                )
            )
        else:
            converted_tokens.append(token)

    return converted_tokens
