from pydantic import BaseModel

from typing import Any, Dict, List, Optional, Set

from omnilingual import LanguageCode

from .sense import Sense


class LexemeIdentifier(BaseModel):
    language: LanguageCode
    lemma: str
    pos: str


class Lexeme(LexemeIdentifier):
    tags: Set[str] = set()

    orthography: Dict[str, str]
    pronounce: Dict[str, str] = {}

    senses: List[Sense]

    features: Optional[Dict[str, str]]

    declensions: Optional[Any]
    conjugations: Optional[Any]
