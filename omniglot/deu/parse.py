from typing import List

import spacy
from spacy.pipeline import Sentencizer

from documental import Text, Tokens
from documental.token import WordToken
from omniglot.mul.numbers import combine_numbers
from omniglot.mul.punctuation import convert_punctuation_tokens
from omnilingual import LanguageCode, PartOfSpeech

from ..parser import PipelineAnnotator


class GermanParser(PipelineAnnotator):
    def __init__(self):
        super().__init__()

        self.nlp = spacy.load("de_core_news_md")

        self.nlp.add_pipe(Sentencizer())

        self.add_pipe(self.tokenize)
        self.add_pipe(convert_punctuation_tokens)
        self.add_pipe(combine_numbers)

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.German]

    def tokenize(self, text: Text, tokenized: Tokens):
        for token in self.nlp(text.text):
            # TODO: Check POS
            print(token.text, token.pos_, token.lemma_)
            # TODO: Check for adding grammatical tags
            tokenized.tokens.append(
                WordToken(
                    language=LanguageCode.German,
                    lemma=token.lemma_,
                    pos=PartOfSpeech(token.pos_),
                    text=token.text,
                    tags=[],
                )
            )
