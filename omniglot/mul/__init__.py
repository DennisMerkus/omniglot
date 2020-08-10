from omniglot.document import Text, TokenizedDocument
from omniglot.tokens import WordToken


def remove_extra_whitespace(text: Text, tokenized: TokenizedDocument) -> None:
    filtered_tokens = []

    for token in tokenized.tokens:
        if isinstance(token, WordToken) and len(token.text.strip()) == 0:
            continue
        else:
            filtered_tokens.append(token)

    tokenized.tokens = filtered_tokens
