import io
import logging
import re
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from ..types import ChineseOrthography
from omniglot.lexeme import Lexeme
from omniglot.sense import Sense
from omnilingual import LanguageCode, PartOfSpeech


class CcCedictCounter(BaseModel):
    traditional: str
    simplified: Optional[str]

    pinyin: str


class CcCedictEntry(BaseModel):
    traditional: str
    simplified: str

    pinyin: str
    equivalents: List[str]

    counters: List[str]


class CcCedictJSON(BaseModel):
    created_date: str
    entries: List[CcCedictEntry]


def extract_created_date(data: str) -> Optional[str]:
    CC_CEDICT_created_regexp = r"^#! date=(.+)$"

    for line in io.StringIO(data).readlines():
        # Passed the header without finding the date. Abort.
        if not line.startswith("#"):
            return None

        match = re.search(CC_CEDICT_created_regexp, line)

        if match:
            extracted_date = match.group(1)
            if extracted_date[-1] == "Z":
                extracted_date = extracted_date[:-1]

            return datetime.fromisoformat(extracted_date).date().isoformat()

    return None


def convert_CC_CEDICT_to_JSON(data: str) -> CcCedictJSON:
    entry_regex = r"^(.+?)\s(.+?)\s\[([\w\s:,·]*?)\]\s\/(.*)\/$"

    created_date = extract_created_date(data)

    if created_date is None:
        raise ValueError("[CC-CEDICT] Could not find the created date")

    entries: List[CcCedictEntry] = []

    buffer = io.StringIO(data)
    for line in buffer.readlines():
        entry = line.strip()

        # Skip the header
        if entry.startswith("#"):
            continue

        match = re.match(entry_regex, entry)

        if match is None:
            raise ValueError("Failed to parse entry\n%s" % (entry))

        logging.debug(match.group(1), match.group(2), match.group(3), match.group(4))

        traditional = match.group(1)
        simplified = match.group(2)

        pinyin = match.group(3).replace("u:", "ü")

        equivalents = match.group(4).split("/")

        entries.append(
            CcCedictEntry(
                traditional=traditional,
                simplified=simplified,
                pinyin=pinyin,
                equivalents=equivalents,
                counters=[],
            )
        )

    return CcCedictJSON(created_date=created_date, entries=entries,)


def create_CC_CEDICT_database_entries(
    cc_cedict_dictionary: CcCedictJSON,
) -> List[Lexeme]:
    database_entries: List[Lexeme] = []

    for entry in cc_cedict_dictionary.entries:
        # TODO: /abbr. for 四清運動|四清运动[Si4 qing1 Yun4 dong4]/
        # TODO: Taiwanese pronunciation /Taiwan pr. []/ or /*sense* (Taiwan pr. [])/
        # TODO: Cross-reference classifiers: /CL:封[feng1]/
        # TODO: Extract tags (coll., idiom, math., finance, etc)

        # TODO: Parse traditional/simplified phrases with ， and pinyin with ,
        # TODO: Parse triditional/simplified names with · and pinyin with ·

        senses: List[Sense] = [
            Sense(
                definitions={LanguageCode.English: [equivalent]},
                tags=[],
                information=[],
                references=[],
                antonyms=[],
                synonyms=[],
                source_language_words=[],
            )
            for equivalent in entry.equivalents
        ]

        database_entries.append(
            Lexeme(
                language=LanguageCode.Chinese,
                lemma=entry.traditional,
                pos=PartOfSpeech.Nil,
                sources={"CC-CEDICT": cc_cedict_dictionary.created_date},
                orthography=ChineseOrthography(
                    all=[entry.traditional, entry.simplified],
                    Hant=entry.traditional,
                    Hans=entry.simplified,
                ),
                pronounce={"pinyin": entry.pinyin},
                tags=[],
                senses=senses,
                features={},
                declensions=None,
                conjugations=None,
            )
        )

    return database_entries
