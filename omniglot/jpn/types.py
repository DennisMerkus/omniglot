from typing import List

from pydantic import BaseModel


class JapaneseOrthography(BaseModel):
    kanji: List[str]
    kana: List[str]
