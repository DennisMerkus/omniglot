import logging
from typing import List, Set

from spacy.lang.ar import Arabic as SpacyArabic
from spacy.pipeline import Sentencizer

from documental.token import Token, WordToken
from omniglot.mul.numbers import combine_numbers
from omniglot.mul.punctuation import convert_punctuation_tokens
from omnilingual import LanguageCode, PartOfSpeech

from ..parser import NaturalLanguageProcessor


class ArabicParser(NaturalLanguageProcessor):
    def __init__(self):
        super().__init__()

        self.nlp = SpacyArabic()

        self.nlp.add_pipe(Sentencizer())

    def process(self, text: str) -> List[Token]:
        tokens: List[Token] = self.tokenize(text)

        tokens = convert_punctuation_tokens(tokens)
        tokens = combine_numbers(tokens)

        return tokens

    def supported_languages(self) -> Set[LanguageCode]:
        return set([LanguageCode.Arabic])

    def tokenize(self, text: str) -> List[Token]:
        tokens: List[Token] = []

        for token in self.nlp(text):
            logging.debug(
                "%s %s %s %s" % (token.text, token.lemma_, token.pos_, token.tag_)
            )

            # TODO: POS checking.
            word = WordToken(
                language=LanguageCode.Arabic,
                lemma=token.lemma_,
                pos=PartOfSpeech.Nil,
                text=token.text,
            )

            tokens.append(word)

        return tokens
