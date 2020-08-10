from pydantic import BaseModel

from typing import Any, Dict, List, Optional, Set

from omnilingual import LanguageCode


class LexemeIdentifier(BaseModel):
    language: str
    lemma: str
    pos: str


class SourceWord(BaseModel):
    language: LanguageCode

    word: Optional[str]

    full: bool

    tags: Set[str] = set()


class Sense(BaseModel):
    definitions: Dict[str, List[str]]

    tags: Set[str] = set()

    information: List[str] = []

    references: List[str] = []

    antonyms: List[str] = []
    synonyms: List[str] = []

    source_language_words: List[SourceWord] = []


class Lexeme(LexemeIdentifier):
    tags: Set[str] = set()

    orthography: Dict[str, str]
    pronounce: Dict[str, str] = {}

    senses: List[Sense]

    features: Optional[Dict[str, str]]

    declensions: Optional[Any]
    conjugations: Optional[Any]
