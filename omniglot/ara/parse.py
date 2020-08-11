import logging
from typing import List

from spacy.lang.ar import Arabic as SpacyArabic
from spacy.pipeline import Sentencizer

from documental import Text, Tokens
from documental.token import WordToken
from omniglot.mul.numbers import combine_numbers
from omniglot.mul.punctuation import convert_punctuation_tokens
from omnilingual import LanguageCode, PartOfSpeech

from ..parser import PipelineAnnotator


class ArabicParser(PipelineAnnotator):
    def __init__(self):
        super().__init__()

        self.nlp = SpacyArabic()

        self.nlp.add_pipe(Sentencizer())

        self.add_pipe(self.tokenize)
        self.add_pipe(convert_punctuation_tokens)
        self.add_pipe(combine_numbers)

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.Arabic]

    def tokenize(self, text: Text, tokenized: Tokens) -> None:
        for token in self.nlp(text.text):
            logging.debug(
                "%s %s %s %s" % (token.text, token.lemma_, token.pos_, token.tag_)
            )

            # TODO: POS checking.
            word = WordToken(
                language=LanguageCode.Arabic,
                lemma=token.lemma_,
                pos=PartOfSpeech.Nil,
                text=token.text,
                tags=[token.tag_],
            )

            tokenized.tokens.append(word)
