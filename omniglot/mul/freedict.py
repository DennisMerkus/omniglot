from typing import List, Optional

from bs4 import BeautifulSoup
from pydantic import BaseModel

from omnilingual import LanguageCode, PartOfSpeech
from omniglot.lexeme import Lexeme
from omniglot.sense import Sense


class FreedictEntry(BaseModel):
    orthography: List[str]
    pronunciation: Optional[str]

    pos: Optional[str]
    gender: Optional[str]

    senses: List[List[str]]


def parse_freedict_entry(entry: BeautifulSoup) -> FreedictEntry:
    orthography: List[str] = [orth.string for orth in entry.find_all("orth")]

    pronunciation: Optional[str] = None

    pron = entry.find("pron")
    if pron:
        pronunciation = pron.string

    part_of_speech: Optional[str] = None

    pos = entry.find("pos")
    if pos:
        part_of_speech = pos.string

    gender: Optional[str] = None

    gen = entry.find("gen")
    if gen:
        gender = gen.string

    senses: List[List[str]] = []

    for sense in entry.find_all("sense"):
        quotes: List[str] = []

        for quote in sense.find_all("quote"):
            quotes.append(quote.string)

        senses.append(quotes)

    return FreedictEntry(
        orthography=orthography,
        pronunciation=pronunciation,
        pos=part_of_speech,
        gender=gender,
        senses=senses,
    )


def parse_freedict(
    xml: str, lang_from: LanguageCode, lang_to: LanguageCode
) -> List[Lexeme]:
    soup = BeautifulSoup(xml, "lxml-xml")

    lexemes: List[Lexeme] = []

    for entry in soup.findAll("entry"):
        freedict_entry = parse_freedict_entry(entry)

        tags: List[str] = []
        features: List[str] = []

        pos: PartOfSpeech

        # TODO: Check Freedict POS tags
        if freedict_entry.pos is None:
            pos = PartOfSpeech.Nil
        elif freedict_entry.pos == "adj":
            pos = PartOfSpeech.Adjective
        elif freedict_entry.pos == "adv":
            pos = PartOfSpeech.Adverb
        elif freedict_entry.pos == "art":
            pos = PartOfSpeech.Determiner
            features.append("PronType=Art")
        elif freedict_entry.pos == "conj":
            pos = PartOfSpeech.Conjunction
        elif freedict_entry.pos == "int":
            pos = PartOfSpeech.Interjection
        elif freedict_entry.pos == "n":
            pos = PartOfSpeech.Noun
        elif freedict_entry.pos == "num":
            pos = PartOfSpeech.Number
        elif freedict_entry.pos == "prep":
            pos = PartOfSpeech.Adposition
        elif freedict_entry.pos == "pron":
            pos = PartOfSpeech.Pronoun
        elif freedict_entry.pos == "v":
            pos = PartOfSpeech.Verb
        elif freedict_entry.pos == "vi":
            pos = PartOfSpeech.Verb
            tags.append("vi")
        elif freedict_entry.pos == "vt":
            pos = PartOfSpeech.Verb
            tags.append("vt")
        else:
            raise NotImplementedError("Freedict POS %s" % (freedict_entry.pos))

        pronunciation = (
            {}
            if freedict_entry.pronunciation is None
            else {"ipa": freedict_entry.pronunciation}
        )

        lexemes.append(
            Lexeme(
                language=lang_from.value,
                lemma=freedict_entry.orthography[0],
                orthography={"all": freedict_entry.orthography},
                pronounce=pronunciation,
                pos=pos.value,
                senses=[
                    Sense(definitions={LanguageCode.English.value: definitions})
                    for definitions in freedict_entry.senses
                ],
            )
        )

    return lexemes


def load(
    file_name: str, lang_from: LanguageCode, lang_to: LanguageCode
) -> List[Lexeme]:
    with open(file_name, "r") as file:
        xml = file.read()

    return parse_freedict(xml, lang_from, lang_to)
