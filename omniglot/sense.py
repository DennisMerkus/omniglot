from typing import Dict, List, Optional, Set

from omnilingual import LanguageCode
from pydantic import BaseModel


class SourceWord(BaseModel):
    language: LanguageCode

    word: Optional[str]

    full: bool

    tags: Set[str] = set()


class Sense(BaseModel):
    definitions: Dict[LanguageCode, List[str]]

    tags: Set[str] = set()

    information: List[str] = []

    references: List[str] = []

    antonyms: List[str] = []
    synonyms: List[str] = []

    source_language_words: List[SourceWord] = []

    def to_bson(self):
        return {
            "definitions": {
                language.value: definitions
                for language, definitions in self.definitions.items()
            },
            "tags": list(self.tags),
            "information": self.information,
            "references": self.references,
            "antonyms": self.antonyms,
            "synonyms": self.synonyms,
            "source_language_words": self.source_language_words,
        }
