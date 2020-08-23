from typing import List

from documental.token import Token


class NaturalLanguageProcessor(object):
    def process(self, text: str) -> List[Token]:
        raise NotImplementedError()
