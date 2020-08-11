from typing import List

import spacy
from spacy.pipeline import Sentencizer

from documental import Text, Tokens
from omnilingual import LanguageCode, PartOfSpeech

from ..mul.numbers import combine_numbers
from ..mul.punctuation import convert_punctuation_tokens
from ..parser import PipelineAnnotator
from documental.token import WordToken


class EnglishParser(PipelineAnnotator):
    def __init__(self):
        super().__init__()

        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.add_pipe(Sentencizer())

        self.add_pipe(self.tokenize)
        self.add_pipe(convert_punctuation_tokens)
        self.add_pipe(combine_numbers)

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.English]

    def tokenize(self, text: Text, tokenized: Tokens) -> None:
        for token in self.nlp(text.text):
            # TODO: POS checking.
            tokenized.tokens.append(
                WordToken(
                    text=token.text,
                    language=LanguageCode.English,
                    lemma=token.lemma_,
                    pos=PartOfSpeech(token.pos_),
                    tags=[],
                )
            )
