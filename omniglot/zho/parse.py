from typing import List

import spacy
from spacy.pipeline import Sentencizer

from documental.token import Token, WordToken
from omniglot.mul.numbers import combine_numbers
from omniglot.mul.punctuation import convert_punctuation_tokens
from omnilingual import LanguageCode, PartOfSpeech

from ..parser import NaturalLanguageProcessor


class MandarinChineseParser(NaturalLanguageProcessor):
    def __init__(self):
        super().__init__()

        self.nlp = spacy.load("zh_core_web_md")
        self.nlp.add_pipe(Sentencizer())

    def process(self, text: str) -> List[Token]:
        tokens: List[Token] = self.tokenize(text)

        tokens = combine_numbers(tokens)
        tokens = convert_punctuation_tokens(tokens)

        return tokens

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.Chinese]

    def tokenize(self, text: str) -> List[Token]:
        tokens: List[Token] = []

        for token in self.nlp(text):
            print(token, token.pos_, token.lemma_, token.tag_)

            tokens.append(
                WordToken(
                    text=token.text,
                    language=LanguageCode.Chinese,
                    lemma=token.lemma_,
                    pos=PartOfSpeech.Nil,
                    tags=[],
                )
            )

        return tokens
