from typing import Dict

from pydantic import BaseModel


class Morpheme(BaseModel):
    text: str
    lemma: str

    features: Dict[str, str]
