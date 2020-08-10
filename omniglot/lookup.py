from typing import List, Optional


from omnilingual import LanguageCode, PartOfSpeech
from .lexeme import Lexeme


class LemmaNotFoundError(Exception):
    pass


class LexemeLookup(object):
    async def lexemes_with_lemma(
        self, lemma: str, language: LanguageCode, pos: Optional[PartOfSpeech]
    ) -> List[Lexeme]:
        raise NotImplementedError()


class FrequencyLookup(object):
    async def word_frequency(self, language: LanguageCode, word: str) -> Optional[int]:
        raise NotImplementedError()
