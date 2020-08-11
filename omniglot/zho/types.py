from typing import List


from pydantic import BaseModel

from omniglot.dictionary import Orthography


class ChineseOrthography(Orthography):
    Hant: str  # zh-Hant Traditional chinese script
    Hans: str  # zh-Hans Simplified chinese script


class ChinesePronounce(BaseModel):
    pinyin: List[str]
