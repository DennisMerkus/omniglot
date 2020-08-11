import re
from typing import Iterator, List, Optional

from omnilingual import LanguageCode, PartOfSpeech
from omnilingual.features.zbn import BanuNounClass, BanuVerbType
from pydantic import BaseModel

from omniglot.lexeme import Lexeme
from omniglot.sense import Sense


class BanuDictionaryEntry(BaseModel):
    word: str
    emphatic: Optional[str]

    pos: PartOfSpeech

    noun_classes: Optional[List[BanuNounClass]]
    verb_type: Optional[BanuVerbType]

    definition: str
    number: Optional[int]


def read_file(file_name: str) -> Iterator[str]:
    with open(file_name) as file:
        for line in file:
            yield line.strip()


def parse_entry(line: str) -> BanuDictionaryEntry:
    ENTRY_REGEX = r"^(?P<head>[\-a-z]*[\sa-z]*\w+)\s*(\((?P<notes>[^\)]+)\))?\s*(?P<number>\d+)?\s*(?P<banu_head>[\-a-z]*[\sa-z]*\w+)\s*(\((?P<banu_notes>[^\)]+)\))?\s+(?P<pos>[\w\-\.]+)\s+(?P<rest>.*)$"

    VERB_POS_REGEX = r"^[vV]\.T(?P<number>\d)$"

    match = re.match(ENTRY_REGEX, line)

    if match is not None:
        head = match.group("head")

        pos_string = match.group("pos")

        pos_match = re.match(VERB_POS_REGEX, pos_string)

        emphatic: Optional[str] = None
        verb_type: Optional[BanuVerbType] = None
        noun_classes: Optional[List[BanuNounClass]] = None

        number: Optional[int] = None

        tags: List[str] = []
        features: List[str] = []

        if match.group("number") is not None:
            number = int(match.group("number"))

        if pos_match is not None:
            pos = PartOfSpeech.Verb
            verb_type = BanuVerbType(int(pos_match.group("number")))

            notes = match.group("notes")

            if notes is not None:
                emphatic = notes.strip()
        elif pos_string == "n.":
            pos = PartOfSpeech.Noun

            notes = match.group("notes")

            if notes is not None:
                classes = [
                    noun_class.strip()
                    for noun_class in re.split("[,;]", match.group("notes"))
                ]

                noun_classes = []

                for class_item in classes:
                    if class_item in [
                        "zwo",
                        "kto",
                        "kso",
                        "go",
                        "afa",
                        "isi",
                        "utu",
                        "enge",
                        "ndzo",
                    ]:
                        noun_classes.append(BanuNounClass(class_item))
                    else:
                        raise ValueError("Unexpected noun class %s" % (class_item))
        elif pos_string == "adv.":
            pos = PartOfSpeech.Adverb
        elif pos_string == "clss.":
            pos = PartOfSpeech.BanuClass
        elif pos_string == "clss.sp.":
            pos = PartOfSpeech.BanuClassSpecifier
        elif pos_string == "collql.":
            pos = PartOfSpeech.Nil
            tags.append("Colloquial")
        elif pos_string == "idiom." or pos_string == "n.idiom.":
            pos = PartOfSpeech.Nil
            tags.append("Idiom")
        elif pos_string == "q.":
            pos = PartOfSpeech.BanuQuestion
        elif pos_string == "q.v.":
            pos = PartOfSpeech.BanuQuestionVerb
        elif pos_string == "qty.indf.":
            pos = PartOfSpeech.BanuIndefiniteQuantity
        elif pos_string == "rel.pn.":
            pos = PartOfSpeech.Pronoun
            tags.append("PronType=Rel")
        elif pos_string == "cnj.":
            pos = PartOfSpeech.Conjunction
        elif pos_string == "contr.":
            pos = PartOfSpeech.Nil
            tags.append("Contraction")
        elif pos_string == "particle":
            pos = PartOfSpeech.Particle
        elif pos_string == "pn.":
            pos = PartOfSpeech.Pronoun
        elif pos_string == "pn.io.r.":
            pos = PartOfSpeech.Pronoun
        elif pos_string == "pn.rflx.":
            pos = PartOfSpeech.Pronoun
            features.append("Reflex=Yes")
        elif pos_string == "quasi-pn.":
            pos = PartOfSpeech.Pronoun
        elif pos_string == "sffx.":
            pos = PartOfSpeech.Suffix
        else:
            raise NotImplementedError("pos %s\n%s" % (pos_string, line))

        return BanuDictionaryEntry(
            word=head,
            pos=pos,
            verb_type=verb_type,
            noun_classes=noun_classes,
            emphatic=emphatic,
            definition=match.group("rest"),
            number=number,
        )
    else:
        raise ValueError("Could not match line %s" % (line))


def load(file_name: str) -> List[Lexeme]:
    lexemes: List[Lexeme] = []

    for line in read_file(file_name):
        entry = parse_entry(line)

        lexemes.append(
            Lexeme(
                language=LanguageCode.Banu,
                lemma=entry.word,
                orthography={"all": [entry.word]},
                pronounce={},
                pos=[entry.pos.value],
                senses=[Sense(definitions={LanguageCode.English: [entry.definition]})],
            )
        )

    return lexemes
