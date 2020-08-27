from pydantic import BaseModel

from typing import Any, Dict, List, Optional, Set, Union

from omnilingual import LanguageCode, PartOfSpeech

from .sense import Sense


class LexemeIdentifier(BaseModel):
    language: LanguageCode
    lemma: str
    pos: PartOfSpeech

    def to_bson(self):
        return {
            "language": self.language.value,
            "lemma": self.lemma,
            "pos": self.pos.value,
        }


class Lexeme(LexemeIdentifier):
    tags: Set[str] = set()

    orthography: Dict[str, Union[str, List[str]]]
    pronounce: Dict[str, str] = {}

    senses: List[Sense]

    features: Optional[Dict[str, str]]

    declensions: Optional[Any]
    conjugations: Optional[Any]

    def to_bson(self):
        return {
            "language": self.language.value,
            "lemma": self.lemma,
            "pos": self.pos.value,
            "tags": list(self.tags),
            "orthography": self.orthography,
            "pronounce": self.pronounce,
            "senses": [sense.to_bson() for sense in self.senses],
            "features": self.features,
            "declensions": self.declensions,
            "conjugations": self.conjugations,
        }
