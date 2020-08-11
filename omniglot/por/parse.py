from typing import List

import spacy
from spacy.pipeline import Sentencizer

from documental import Text, Tokens
from documental.token import WordToken
from omniglot.mul.numbers import combine_numbers
from omniglot.mul.punctuation import convert_punctuation_tokens
from omnilingual import LanguageCode, PartOfSpeech
from omnilingual.features import parse_features

from ..parser import PipelineAnnotator


class PortugueseParser(PipelineAnnotator):
    def __init__(self):
        super().__init__()

        self.nlp = spacy.load("pt_core_news_sm")
        self.nlp.add_pipe(Sentencizer())

        self.add_pipe(self.tokenize)
        self.add_pipe(combine_numbers)
        self.add_pipe(convert_punctuation_tokens)

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.Portuguese]

    def tokenize(self, text: Text, tokenized: Tokens) -> None:
        for token in self.nlp(text.text):
            tokenized.tokens.append(
                WordToken(
                    language=LanguageCode.Portuguese,
                    text=token.text,
                    lemma=token.lemma_,
                    pos=PartOfSpeech(token.pos_),
                    features=parse_features(token.tag_),
                )
            )
