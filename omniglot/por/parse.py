from typing import List

import spacy
from spacy.pipeline import Sentencizer

from documental.token import WordToken, Token
from omniglot.mul.numbers import combine_numbers
from omniglot.mul.punctuation import convert_punctuation_tokens
from omnilingual import LanguageCode, PartOfSpeech
from omnilingual.features import parse_features

from ..parser import NaturalLanguageProcessor


class PortugueseParser(NaturalLanguageProcessor):
    def __init__(self):
        super().__init__()

        self.nlp = spacy.load("pt_core_news_sm")
        self.nlp.add_pipe(Sentencizer())

    def process(self, text: str) -> List[Token]:
        tokens: List[Token] = self.tokenize(text)

        tokens = combine_numbers(tokens)
        tokens = convert_punctuation_tokens(tokens)

        return tokens

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.Portuguese]

    def tokenize(self, text: str) -> List[Token]:
        tokens: List[Token] = []

        for token in self.nlp(text):
            print(token, token.tag_)

            tokens.append(
                WordToken(
                    language=LanguageCode.Portuguese,
                    text=token.text,
                    lemma=token.lemma_.lower(),
                    pos=PartOfSpeech(token.pos_),
                    features=parse_features(token.tag_),
                )
            )

        return tokens
