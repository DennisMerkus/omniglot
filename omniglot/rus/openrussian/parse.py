import csv
from typing import List, Optional, Dict

import aiofiles

from collections import defaultdict

from omnilingual import LanguageCode

from .extract import (
    extract_boolean,
    extract_number,
    extract_optional_boolean,
    extract_optional_number,
    extract_optional_string,
)
from .types import (
    OpenRussianAdjective,
    OpenRussianConjugation,
    OpenRussianDeclension,
    OpenRussianNoun,
    OpenRussianTranslation,
    OpenRussianVerb,
    OpenRussianWord,
)


async def parseWordsFile(file_path: str) -> Dict[int, OpenRussianWord]:
    async with aiofiles.open(file_path, "r") as tsv:
        reader = csv.DictReader(tsv, dialect="excel-tab")

        words: Dict[int, OpenRussianWord] = {}

        for row in reader:
            if not row["id"].isdecimal():
                raise ValueError("Expected id to be a number\n%s" % (row))

            id = int(row["id"])

            position = extract_optional_number(row["position"])

            if position is not None and position != 1 and position != 2:
                raise ValueError("Expected position to be 1 or 2\n%s" % (row))

            bare = row["bare"]

            if bare is None:
                raise ValueError("Expected bare to be a string\n%s" % (row))

            accented = row["accented"]

            if accented is None:
                raise ValueError("Expected accented to be a string\n%s" % (row))

            derived_id: Optional[int] = extract_optional_number(
                row["derived_from_word_id"]
            )

            rank: Optional[int] = extract_optional_number(row["rank"])

            disabled: bool = extract_boolean(row["disabled"])

            audio: Optional[str] = extract_optional_string(row["audio"])

            usage_en: Optional[str] = extract_optional_string(row["usage_en"])
            usage_de: Optional[str] = extract_optional_string(row["usage_de"])

            number_value: Optional[str] = extract_optional_string(row["number_value"])

            level: Optional[str] = None

            if row["level"] is None or len(row["level"]) == 0:
                level = None
            elif row["level"] not in ["A1", "A2", "B1", "B2", "C1", "C2"]:
                raise ValueError("Expected level to be a CEFR level\n%s" % (row))
            else:
                level = row["level"]

            row_type: Optional[str] = None

            if row["type"] is None or len(row["type"]) == 0:
                row_type = None
            elif row["type"] not in [
                "noun",
                "verb",
                "adjective",
                "adverb",
                "expression",
                "other",
            ]:
                raise ValueError("Unexpected type %s\n%s" % (row_type, row))
            else:
                row_type = row["type"]

            words[id] = OpenRussianWord(
                id=id,
                position=position,
                bare=bare,
                accented=accented,
                derived_from_word_id=derived_id,
                rank=rank,
                disabled=disabled,
                audio=audio,
                usage_en=usage_en,
                usage_de=usage_de,
                number_value=number_value,
                type=row_type,
                level=level,
            )

    return words


async def parseTranslationsFile(
    file_path: str,
) -> Dict[int, List[OpenRussianTranslation]]:
    async with aiofiles.open(file_path, "r") as tsv:
        reader = csv.DictReader(tsv, dialect="excel-tab")

        translations: Dict[int, List[OpenRussianTranslation]] = defaultdict(list)

        for row in reader:
            lang = row["lang"]

            if lang == "en":
                language: LanguageCode = LanguageCode.English
            elif lang == "de":
                language = LanguageCode.German
            else:
                raise ValueError("Unexpected translation language\n%s" % (row))

            word_id = extract_number(row["word_id"])

            row_info = extract_optional_string(row["info"])

            translations[word_id].append(
                OpenRussianTranslation(
                    id=int(row["id"]),
                    language=language,
                    word_id=word_id,
                    position=extract_number(row["position"]),
                    tl=row["tl"],
                    example_ru=extract_optional_string(row["example_ru"]),
                    example_tl=extract_optional_string(row["example_tl"]),
                    info=row_info,
                )
            )

    return translations


async def parseNounsFile(file_path: str) -> Dict[int, OpenRussianNoun]:
    async with aiofiles.open(file_path, "r") as tsv:
        reader = csv.DictReader(tsv, dialect="excel-tab")

        nouns: Dict[int, OpenRussianNoun] = {}

        for row in reader:
            word_id = extract_number(row["word_id"])
            gender: Optional[str] = extract_optional_string(row["gender"])

            if gender is not None and gender not in ["m", "f", "n", "both"]:
                raise ValueError("Unexpected gender\n%s" % (row))

            nouns[word_id] = OpenRussianNoun(
                word_id=word_id,
                gender=gender,
                partner=extract_optional_string(row["partner"]),
                animate=extract_optional_boolean(row["animate"]),
                indeclinable=extract_optional_boolean(row["indeclinable"]),
                sg_only=extract_optional_boolean(row["sg_only"]),
                pl_only=extract_optional_boolean(row["pl_only"]),
                decl_sg_id=extract_optional_number(row["decl_sg_id"]),
                decl_pl_id=extract_optional_number(row["decl_pl_id"]),
            )

    return nouns


async def parseVerbsFile(file_path: str) -> Dict[int, OpenRussianVerb]:
    async with aiofiles.open(file_path, "r") as tsv:
        reader = csv.DictReader(tsv, dialect="excel-tab")

        nouns: Dict[int, OpenRussianVerb] = {}

        for row in reader:
            word_id = extract_number(row["word_id"])
            aspect: Optional[str] = row["aspect"]

            if aspect is None or len(aspect) == 0:
                aspect = None
            elif aspect not in ["perfective", "imperfective", "both"]:
                raise ValueError("Unexpected aspect\n%s" % (row))

            nouns[word_id] = OpenRussianVerb(
                word_id=word_id,
                aspect=aspect,
                partner=extract_optional_string(row["partner"]),
                imperative_sg=extract_optional_string(row["imperative_sg"]),
                imperative_pl=extract_optional_string(row["imperative_pl"]),
                past_m=extract_optional_string(row["past_m"]),
                past_f=extract_optional_string(row["past_f"]),
                past_n=extract_optional_string(row["past_n"]),
                past_pl=extract_optional_string(row["past_pl"]),
                presfut_conj_id=extract_number(row["presfut_conj_id"]),
            )

    return nouns


async def parseAdjectivesFile(file_path: str,) -> Dict[int, OpenRussianAdjective]:
    async with aiofiles.open(file_path, "r") as tsv:
        reader = csv.DictReader(tsv, dialect="excel-tab")

        adjectives: Dict[int, OpenRussianAdjective] = {}

        for row in reader:
            word_id = extract_number(row["word_id"])
            adjectives[word_id] = OpenRussianAdjective(
                word_id=word_id,
                incomparable=extract_optional_boolean(row["incomparable"]),
                comparative=extract_optional_string(row["comparative"]),
                superlative=extract_optional_string(row["superlative"]),
                short_m=extract_optional_string(row["short_m"]),
                short_f=extract_optional_string(row["short_f"]),
                short_n=extract_optional_string(row["short_n"]),
                short_pl=extract_optional_string(row["short_pl"]),
                decl_m_id=extract_number(row["decl_m_id"]),
                decl_f_id=extract_number(row["decl_f_id"]),
                decl_n_id=extract_number(row["decl_n_id"]),
                decl_pl_id=extract_number(row["decl_pl_id"]),
            )

    return adjectives


async def parseConjugationsFile(file_path: str,) -> Dict[int, OpenRussianConjugation]:
    async with aiofiles.open(file_path, "r") as tsv:
        reader = csv.DictReader(tsv, dialect="excel-tab")

        conjugations: Dict[int, OpenRussianConjugation] = {}

        for row in reader:
            id = extract_number(row["id"])
            conjugations[id] = OpenRussianConjugation(
                id=id,
                word_id=extract_number(row["word_id"]),
                sg1=extract_optional_string(row["sg1"]),
                sg2=extract_optional_string(row["sg2"]),
                sg3=extract_optional_string(row["sg3"]),
                pl1=extract_optional_string(row["pl1"]),
                pl2=extract_optional_string(row["pl2"]),
                pl3=extract_optional_string(row["pl3"]),
            )

    return conjugations


async def parseDeclensionsFile(file_path: str,) -> Dict[int, OpenRussianDeclension]:
    async with aiofiles.open(file_path, "r") as tsv:
        reader = csv.DictReader(tsv, dialect="excel-tab")

        declensions: Dict[int, OpenRussianDeclension] = {}

        for row in reader:
            id = extract_number(row["id"])
            declensions[id] = OpenRussianDeclension(
                id=id,
                word_id=extract_number(row["word_id"]),
                nom=extract_optional_string(row["nom"]),
                gen=extract_optional_string(row["gen"]),
                dat=extract_optional_string(row["dat"]),
                acc=extract_optional_string(row["acc"]),
                inst=extract_optional_string(row["inst"]),
                prep=extract_optional_string(row["prep"]),
            )

    return declensions
