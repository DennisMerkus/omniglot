from typing import Dict, List

from pydantic import BaseModel


class JapaneseOrthography(BaseModel):
    kanji: List[str]
    kana: List[str]


class Kanji(BaseModel):
    character: str
    stroke_count: int

    on_readings: List[str]
    kun_readings: List[str]

    meanings: Dict[str, List[str]]
