from typing import List

from omnilingual import LanguageCode, PartOfSpeech

import spacy
from spacy.pipeline import Sentencizer

from ..parser import PipelineAnnotator
from ..tokens import WordToken
from .document import Text, TokenizedDocument
from .mul.numbers import combine_numbers
from .mul.punctuation import convert_punctuation_tokens


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

    def tokenize(self, text: Text, tokenized: TokenizedDocument):
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
