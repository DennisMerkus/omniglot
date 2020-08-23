from typing import List

from documental.token import Token, WordToken


def remove_extra_whitespace(tokens: List[Token]) -> List[Token]:
    filtered_tokens = []

    for token in tokens:
        if isinstance(token, WordToken) and len(token.text.strip()) == 0:
            continue
        else:
            filtered_tokens.append(token)

    return filtered_tokens
