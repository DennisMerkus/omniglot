from typing import List

from pydantic import BaseModel

from omniglot.lexeme import Lexeme


class DictionaryLoader(object):
    async def load(self) -> List[Lexeme]:
        raise NotImplementedError()


class Orthography(BaseModel):
    all: List[str]


class IPAPhonetics(BaseModel):
    ipa: str
