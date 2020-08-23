from typing import List

import spacy
from spacy.pipeline import Sentencizer

from documental.token import WordToken, Token
from omniglot.mul.numbers import combine_numbers
from omniglot.mul.punctuation import convert_punctuation_tokens
from omnilingual import LanguageCode, PartOfSpeech

from ..parser import NaturalLanguageProcessor


class GermanParser(NaturalLanguageProcessor):
    def __init__(self):
        super().__init__()

        self.nlp = spacy.load("de_core_news_md")

        self.nlp.add_pipe(Sentencizer())

    def process(self, text: str) -> List[Token]:
        tokens: List[Token] = self.tokenize(text)

        tokens = convert_punctuation_tokens(tokens)
        tokens = combine_numbers(tokens)

        return tokens

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.German]

    def tokenize(self, text: str) -> List[Token]:
        tokens: List[Token] = []

        for token in self.nlp(text):
            # TODO: Check POS
            print(token.text, token.pos_, token.lemma_)
            # TODO: Check for adding grammatical tags
            tokens.append(
                WordToken(
                    language=LanguageCode.German,
                    lemma=token.lemma_,
                    pos=PartOfSpeech(token.pos_),
                    text=token.text,
                    tags=[],
                )
            )

        return tokens
