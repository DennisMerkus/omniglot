from collections import defaultdict
from typing import Dict, List

import aiofiles
import os

from bs4 import BeautifulSoup

from omniglot.jpn.types import Kanji
from omnilingual import Language


def convert_entry(character: BeautifulSoup) -> Kanji:
    literal: str = character.find("literal").string

    stroke_count = int(character.find("stroke_count").string)

    on_readings: List[str] = []
    kun_readings: List[str] = []

    for reading in character.findAll("reading"):
        if reading["r_type"] == "ja_on":
            on_readings.append(reading.string)
        elif reading["r_type"] == "ja_kun":
            kun_readings.append(reading.string)

    meanings: Dict[str, List[str]] = defaultdict(list)

    for meaning in character.findAll("meaning"):
        if "m_lang" not in meaning.attrs:
            meaning_language = Language("eng")
        else:
            meaning_language = Language(meaning["m_lang"])

        meanings[meaning_language.alpha_3].append(meaning.string)

    return Kanji(
        character=literal,
        stroke_count=stroke_count,
        on_readings=on_readings,
        kun_readings=kun_readings,
        meanings=meanings,
    )


def convert(xml: str) -> List[Kanji]:
    soup = BeautifulSoup(xml, "lxml-xml")

    kanji: List[Kanji] = []

    for character in soup.findAll("character"):
        kanji.append(convert_entry(character))

    return kanji


async def load_kanjidic(cache_directory: str) -> List[Kanji]:
    async with aiofiles.open(os.path.join(cache_directory, "kanjidic2.xml"), "r") as f:
        data = await f.read()

    return convert(data)
