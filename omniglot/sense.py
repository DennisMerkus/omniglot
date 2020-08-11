from typing import Dict, List, Optional, Set

from omnilingual import LanguageCode
from pydantic import BaseModel


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
