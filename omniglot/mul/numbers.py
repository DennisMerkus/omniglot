from typing import List, Optional

from omniglot.document import Text, TokenizedDocument
from omniglot.tokens import NumberToken, Token


def combine_numbers(text: Text, tokenized: TokenizedDocument) -> None:
    combined_tokens: List[Token] = []

    combined_number: Optional[str] = None

    for token in tokenized.tokens:
        if isinstance(token, NumberToken):
            if combined_number is None:
                combined_number = token.text
            else:
                combined_number += token.text
        else:
            if combined_number is not None:
                combined_tokens.append(NumberToken(combined_number))
                combined_number = None

            combined_tokens.append(token)

    if combined_number is not None:
        combined_tokens.append(NumberToken(combined_number))

    tokenized.tokens = combined_tokens
