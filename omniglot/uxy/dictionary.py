import os
from typing import Dict, Iterable, List, Optional, Tuple

import aiofiles
from bs4 import BeautifulSoup
from pydantic import BaseModel

from omniglot.lexeme import Lexeme
from omniglot.sense import Sense
from omnilingual import LanguageCode, PartOfSpeech

from omnilingual.features.uxy import (
    XianMood,
    XianFormality,
    XianGender,
    XianSlang,
)


from omniglot.dictionary import IPAPhonetics


class ExpectedElementNotFound(Exception):
    ...


class XianDictionaryEntry(BaseModel):
    word: str

    pos: PartOfSpeech
    form: Optional[XianMood]
    gender: Optional[XianGender]

    slang: Optional[XianSlang]

    service: Optional[bool]

    definition: str
    occupation: Optional[bool]


forms = [
    "FAM",
    "IMP",
    "LAUD",
    "NEU",
    "PEJ",
    "REV",
]


convert_pos: Dict[str, PartOfSpeech] = {
    "chj": PartOfSpeech.Conjunction,  # Misspelling
    "cnj": PartOfSpeech.Conjunction,
    "coj": PartOfSpeech.Conjunction,  # Misspelling
    "col": PartOfSpeech.Noun,
    "con": PartOfSpeech.Phrase,
    "deix": PartOfSpeech.Nil,
    "elm": PartOfSpeech.XianElemental,
    "eim.CMP": PartOfSpeech.XianElementalCompound,  # Misspelling
    "elm.CMP": PartOfSpeech.XianElementalCompound,
    "idm": PartOfSpeech.Nil,
    "line": PartOfSpeech.ProperNoun,
    "n": PartOfSpeech.Noun,
    "name": PartOfSpeech.ProperNoun,
    "nlz": PartOfSpeech.XianNominalizer,
    "nlz.CLT": PartOfSpeech.XianNominalizer,
    "nlz.CLTC": PartOfSpeech.XianNominalizer,
    "noun": PartOfSpeech.Noun,
    "num": PartOfSpeech.Number,
    "pn": PartOfSpeech.Pronoun,
    "PN": PartOfSpeech.ProperNoun,
    "Q": PartOfSpeech.Nil,
    "Q.sffx": PartOfSpeech.Nil,
    "rel": PartOfSpeech.Particle,
    "v": PartOfSpeech.Verb,
    "vcp": PartOfSpeech.XianVerbClarifyingParticle,
}

tags: Dict[str, str] = {
    "col": "Color",
    "con": "Conversational",
    "line": "FamilyLine",
    "rel": "Relational",
    "nlz.CLT": "Enclitic",
    "nlz.CLTC": "Enclitic",
}


def parse_pos(
    word: str, pos_string: str,
) -> Tuple[
    PartOfSpeech,
    Optional[XianMood],
    Optional[XianGender],
    Optional[bool],
    Optional[bool],
    Optional[XianFormality],
    Optional[bool],
]:
    word_form: Optional[XianMood] = None
    gender: Optional[XianGender] = None
    service: Optional[bool] = None
    formality: Optional[XianFormality] = None
    occupation: Optional[bool] = None
    slang: Optional[bool] = None

    for form in forms:
        if form in pos_string:
            word_form = XianMood(form)
            pos_string = pos_string.replace(".%s" % (form), "")

    if ".feml" in pos_string:
        gender = XianGender.Female
        pos_string = pos_string.replace(".feml", "")
    elif ".male" in pos_string:
        gender = XianGender.Male
        pos_string = pos_string.replace(".male", "")

    if ".role" in pos_string:
        occupation = True
        pos_string = pos_string.replace(".role", "")

    if ".GEN" in pos_string:
        pos_string = pos_string.replace(".GEN", "")

    if ".SRV" in pos_string:
        service = True
        pos_string = pos_string.replace(".SRV", "")

    if ".for" in pos_string or ".FOR" in pos_string:
        formality = XianFormality.Formal

        pos_string = pos_string.replace(".for", "")
        pos_string = pos_string.replace(".FOR", "")
    elif ".CAS" in pos_string:
        formality = XianFormality.Casual

        pos_string = pos_string.replace(".CAS", "")
    elif ".SEMFOR" in pos_string:
        formality = XianFormality.SemiFormal

        pos_string = pos_string.replace(".SEMFOR", "")

    if "slng" in pos_string:
        slang = True

        pos_string = pos_string.replace("slng", "")

        if word in ["cho’ro", "chu’ro"]:
            pos = PartOfSpeech.Pronoun
        elif word in ["m..aman”", "ma’ma", "t’ek"]:
            pos = PartOfSpeech.XianElemental
        else:
            raise NotImplementedError("Slang", word)

    pos_string = pos_string.rstrip(".")

    if len(pos_string) > 0 and pos_string not in convert_pos:
        raise NotImplementedError("POS", pos_string)
    elif len(pos_string) > 0:
        pos = convert_pos[pos_string]
    else:
        pos = PartOfSpeech.Nil

    return (pos, word_form, gender, service, occupation, formality, slang)


def parse_entry(entry: BeautifulSoup) -> XianDictionaryEntry:
    head_element = entry.find("td")
    pos_element = head_element.find_next_sibling("td")
    translation_element = pos_element.find_next_sibling("td")

    word = head_element.string.strip()

    pos, word_form, gender, service, occupation, formality, slang = parse_pos(
        word, pos_element.string
    )

    return XianDictionaryEntry(
        word=word,
        pos=pos,
        form=word_form,
        definition=translation_element.get_text(),
        gender=gender,
        occupation=occupation,
        service=service,
    )


def parse_entries(soup: BeautifulSoup) -> Iterable[BeautifulSoup]:
    start = soup.find("span", class_="caps", string="DICTIONARY")

    if start is None:
        raise ExpectedElementNotFound("DICTIONARY <span>")

    start = start.parent.parent.parent

    entries = start.find_all("tr")

    # Skip header
    count = 0
    for entry in entries:
        if count < 2:
            count += 1
            continue

        yield entry


def parse_dictionary(soup: BeautifulSoup) -> List[XianDictionaryEntry]:
    dictionary: List[XianDictionaryEntry] = []

    for entry in entries(soup):
        dictionary.append(parse_entry(entry))

    return dictionary


def convert_dictionary(html: str) -> List[Lexeme]:
    entries = parse_dictionary(BeautifulSoup(html, "lxml"))

    dictionary_entries: List[Lexeme] = []

    for entry in entries:
        features: Dict[str, str] = {}

        if entry.form is not None:
            features["form"] = entry.form.value

        if entry.gender is not None:
            features["gender"] = entry.gender.value

        dictionary_entries.append(
            Lexeme(
                language=LanguageCode.Xian,
                lemma=entry.word,
                pos=entry.pos.value,
                sources={"Xian Dictionary": 1},
                orthography={"all": [entry.word], "srx": entry.word},
                pronounce=IPAPhonetics(
                    ipa=entry.word
                ),  # TODO: Write SRX to IPA converter.
                features=features,
                tags=[],
                senses=[Sense(definitions={LanguageCode.English: [entry.definition]})],
            )
        )

    return dictionary_entries


async def load(cache_directory: str) -> List[Lexeme]:
    async with aiofiles.open(
        os.path.join(cache_directory, "XianDictionary.html"), "r"
    ) as f:
        data = await f.read()

    return convert_dictionary(data)
