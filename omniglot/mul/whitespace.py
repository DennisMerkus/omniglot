from documental import Text, Tokens
from documental.token import WordToken


def remove_extra_whitespace(text: Text, tokenized: Tokens) -> None:
    filtered_tokens = []

    for token in tokenized.tokens:
        if isinstance(token, WordToken) and len(token.text.strip()) == 0:
            continue
        else:
            filtered_tokens.append(token)

    tokenized.tokens = filtered_tokens
