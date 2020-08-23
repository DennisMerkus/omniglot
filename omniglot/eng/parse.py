from typing import List

import spacy
from spacy.pipeline import Sentencizer

from documental.token import Token, WordToken
from omnilingual import LanguageCode, PartOfSpeech

from ..mul.numbers import combine_numbers
from ..mul.punctuation import convert_punctuation_tokens
from ..parser import NaturalLanguageProcessor


class EnglishParser(NaturalLanguageProcessor):
    def __init__(self):
        super().__init__()

        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.add_pipe(Sentencizer())

    def process(self, text: str) -> List[Token]:
        tokens: List[Token] = self.tokenize(text)

        tokens = convert_punctuation_tokens(tokens)
        tokens = combine_numbers(tokens)

        return tokens

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.English]

    def tokenize(self, text: str) -> List[Token]:
        tokens: List[Token] = []

        for token in self.nlp(text):
            # TODO: POS checking.
            tokens.append(
                WordToken(
                    text=token.text,
                    language=LanguageCode.English,
                    lemma=token.lemma_,
                    pos=PartOfSpeech(token.pos_),
                    tags=[],
                )
            )

        return tokens
