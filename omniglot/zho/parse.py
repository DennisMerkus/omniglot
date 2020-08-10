from typing import List

from spacy.lang.zh import Chinese as SpacyChinese
from spacy.pipeline import Sentencizer

from omnilingual import LanguageCode, PartOfSpeech

from documental import Text, Tokens
from omniglot.mul.numbers import combine_numbers
from omniglot.mul.punctuation import convert_punctuation_tokens

from ..parser import PipelineAnnotator
from ..tokens import WordToken


class MandarinParser(PipelineAnnotator):
    def __init__(self):
        super().__init__()

        # Use PKUSeg with spaCy 2.3
        SpacyChinese.Defaults.use_jieba = False

        self.nlp = SpacyChinese()
        self.nlp.add_pipe(Sentencizer())

        self.add_pipe(self.tokenize)
        self.add_pipe(combine_numbers)
        self.add_pipe(convert_punctuation_tokens)

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.Chinese]

    @staticmethod
    def tokenize(self, text: Text, tokenized: Tokens) -> None:
        for token in self.nlp(text.text):
            tokenized.tokens.append(
                WordToken(
                    text=token.text,
                    language=LanguageCode.Chinese,
                    lemma=token.lemma_,
                    pos=PartOfSpeech.Nil,
                    tags=[],
                )
            )
