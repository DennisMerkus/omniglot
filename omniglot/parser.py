from typing import Callable, List

from documental import Text, Tokens
from omnilingual import LanguageCode

from .errors import UnsupportedLanguageError

Pipe = Callable[[Text, Tokens], None]


class Annotator(object):
    def process(self, document: Text) -> Tokens:
        pass


class PipelineAnnotator(Annotator):
    def __init__(self):
        self.pipeline: List[Pipe] = []

    def supported_languages(self) -> List[LanguageCode]:
        raise NotImplementedError()

    def add_pipe(self, pipe: Pipe) -> None:
        self.pipeline.append(pipe)

    def process(self, document: Text) -> Tokens:
        if document.language not in self.supported_languages():
            raise UnsupportedLanguageError(
                "%s is not supported by this parser" % (document.language)
            )

        tokenized = Tokens(document.text)

        for pipe in self.pipeline:
            pipe(document, tokenized)

        return tokenized
