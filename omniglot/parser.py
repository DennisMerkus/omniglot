from typing import Callable, List

from omnilingual import LanguageCode

from ..nlp.errors import UnsupportedLanguageError
from .document import Text, TokenizedDocument

Pipe = Callable[[Text, TokenizedDocument], None]


class Annotator(object):
    def process(self, document: Text) -> TokenizedDocument:
        pass


class PipelineAnnotator(Annotator):
    def __init__(self):
        self.pipeline: List[Pipe] = []

    def supported_languages(self) -> List[LanguageCode]:
        raise NotImplementedError()

    def add_pipe(self, pipe: Pipe) -> None:
        self.pipeline.append(pipe)

    def process(self, document: Text) -> TokenizedDocument:
        if document.language not in self.supported_languages():
            raise UnsupportedLanguageError(
                "%s is not supported by this parser" % (document.language)
            )

        tokenized: TokenizedDocument = TokenizedDocument(document.text)

        for pipe in self.pipeline:
            pipe(document, tokenized)

        return tokenized
