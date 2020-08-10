from typing import List

from omniglot.document import Text, TokenizedDocument
from omniglot.tokens import PunctuationToken, Token, WordToken

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


def convert_punctuation_tokens(text: Text, tokenized: TokenizedDocument) -> None:
    converted_tokens: List[Token] = []

    for token in tokenized.tokens:
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

    tokenized.tokens = converted_tokens
