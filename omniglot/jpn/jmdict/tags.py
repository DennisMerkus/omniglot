import re
from typing import Dict, List

from pydantic import BaseModel

from omniglot.tags import (
    field_tags,
    japanese_dialect_tags,
    japanese_specific_tags,
    named_entity_tags,
    usage_tags,
)
from omnilingual import PartOfSpeech


class PosAndTags(BaseModel):
    pos: List[PartOfSpeech]
    tags: List[str]


jmdict_tags: Dict[str, List[str]] = {
    "#General": ["#General"],  # field default
    "MA": ["#MartialArts"],  # field
    "X": ["!X-rated"],  # ??
    "abbr": ["!Abbreviation"],  # misc
    "anat": ["#Anatomy"],  # field
    "arch": ["!Archaism"],  # misc
    "archit": ["#Architecture"],  # field
    "astron": ["#Astronomy"],  # field
    "ateji": ["!Ateji"],  # ke_inf
    "baseb": ["#Baseball"],  # field
    "biol": ["#Biology"],  # field
    "bot": ["#Botany"],  # field
    "Buddh": ["#Buddhism"],  # field
    "bus": ["#Business"],  # field
    "chem": ["#Chemistry"],  # field
    "chn": ["!Children"],  # misc
    "Christn": ["#Christianity"],  # field
    "col": ["!Colloquialism"],  # misc
    "comp": ["#Computer"],  # field
    "company": ["!CompanyName", "!Name"],  #
    "dated": ["!Outdated"],  # misc
    "derog": ["!Derogatory"],  # misc
    "econ": ["#Economics"],  # field
    "eK": ["?ExclusivelyKanji"],  # ??
    "ek": ["?ExclusivelyKana"],  # ??
    "engr": ["#Engineering"],  # field
    "fam": ["!Familiar"],  # misc
    "fem": ["!Female"],  # misc
    "finc": ["#Finance"],  # field
    "food": ["#Food"],  # misc
    "geol": ["#Geology"],  # field
    "geom": ["#Geometry"],  # field
    "gikun": ["?Gikun"],  # re_inf
    "given": ["!FirstName", "!PersonName", "!Name"],  #
    "hist": ["!Historical"],  # misc
    "hon": ["!Honorific", "!Sonkeigo"],  # misc
    "hum": ["!Humble", "!Kenjougo"],  # misc
    "ik": ["?IrregularKana"],  # re_inf
    "iK": ["?IrregularKanji"],  # ke_inf
    "id": ["!Idiomatic"],  # misc
    "io": ["?IrregularOkurigana"],  # ke_inf
    "iv": ["?IrregularVerb"],  # ??
    "joc": ["!Jocular"],  # misc
    "law": ["#Law"],  # field
    "ling": ["#Linguistics"],  # field
    "lit": ["!Literary"],  # misc
    "litf": ["!Literary", "!Formal"],  # misc
    "m-sl": ["!MangaSlang"],  # misc
    "mahj": ["#Mahjong"],  # field
    "male": ["!Male"],  # misc
    "male-sl": ["!MaleSlang"],  # ??
    "math": ["#Mathematics"],  # field
    "med": ["#Medicine"],  # field
    "mil": ["#Military"],  # field
    "music": ["#Music"],  # field
    "net-sl": ["!Slang", "!Internet"],  # misc
    "oK": ["?OutdatedKanji"],  # ke_inf
    "ok": ["?OutdatedKana"],  # re_inf
    "obs": ["!Obsolete"],  # misc
    "obsc": ["!Obscure"],  # misc
    "oik": ["?OldKana"],  # re_inf
    "on-mim": ["!Mimetic", "!Onomatopoeia"],  # misc
    "organization": ["!OrganizationName", "!Name"],  #
    "person": ["!FullName", "!Name"],  #
    "place": ["!PlaceName"],  #
    "poet": ["!Poetical"],  # misc
    "pol": ["!Polite", "!Teineigo"],  # misc
    "product": ["!ProductName", "!Name"],  #
    "proverb": ["!Proverb"],  # misc
    "physics": ["#Physics"],  # field
    "quote": ["!Quotation"],  #
    "rare": ["!Rare"],  # misc
    "sens": ["!Sensitive"],  # misc
    "Shinto": ["#Shinto"],  # field
    "shogi": ["#Shogi"],  # field
    "sl": ["!Slang"],  # misc
    "sports": ["#Sports"],  # field
    "station": ["!StationName", "!Name"],  #
    "sumo": ["#Sumo"],  # field
    "surname": ["!LastName", "!Name"],  # Could not find
    "uK": ["?UsuallyKanji"],  # misc
    "uk": ["?UsuallyKana"],  # misc
    "unclass": ["!UnclassifiedName", "!Name"],  #
    "work": ["!WorkName", "!Name"],  #
    "yoji": ["!Yojijukugo"],  # misc
    "kyb": ["#Kyoto-ben"],  # dial
    "osb": ["#Osaka-ben"],  # dial
    "ksb": ["#Kansai-ben"],  # dial
    "ktb": ["#Kantou-ben"],  # dial
    "tsb": ["#Tosa-ben"],  # dial
    "thb": ["#Touhoku-ben"],  # dial
    "tsug": ["#Tsugaru-ben"],  # dial
    "kyu": ["#Kyushu-ben"],  # dial
    "rkb": ["#Ryukyu-ben"],  # dial
    "nab": ["#Nagano-ben"],  # dial
    "hob": ["#Hokkaido-ben"],  # dial
    "vulg": ["!Vulgar"],  # misc
    "zool": ["#Zoology"],  # field
}


def normalize_tag(tag: str) -> PosAndTags:
    tags: PosAndTags = PosAndTags(pos=[], tags=[])

    if (
        tag in field_tags
        or tag in usage_tags
        or tag in named_entity_tags
        or tag in japanese_specific_tags
        or tag in japanese_dialect_tags
    ):
        tags.tags.append(tag)
    elif tag in jmdict_tags.keys():
        tags.tags.extend(jmdict_tags[tag])
    elif tag in [
        "adj-i",
        "adj-ix",
        "adj-na",
        "adj-no",
        "adj-pn",
        "adj-t",
        "adj-f",
        "adj-kari",  # Archaic forms from here
        "adj-ku",
        "adj-shiku",
        "adj-nari",
    ]:
        tags.pos.append(PartOfSpeech.Adjective)
        tags.tags.append(tag)
    elif tag in ["adv", "adv-to"]:
        tags.pos.append(PartOfSpeech.Adverb)
        tags.tags.append(tag)
    elif tag in ["aux", "aux-v", "aux-adj"]:
        tags.pos.append(PartOfSpeech.Auxiliary)
        tags.tags.append(tag)
    elif tag == "conj":
        tags.pos.append(PartOfSpeech.Conjunction)
    elif tag == "cop-da":
        tags.tags.append("cop-da")
    elif tag == "cop":  # Not in the DTD, but appears in file
        tags.tags.append("cop")
    elif tag == "ctr":
        tags.tags.append("*Counter")
    elif tag == "exp":
        tags.tags.append("*Expression")
    elif tag == "int":
        tags.pos.append(PartOfSpeech.Interjection)
        tags.tags.append("#Kandoushi")
    elif tag == "n":
        tags.pos.append(PartOfSpeech.Noun)
    elif tag in ["n-adv", "n-suf", "n-pref", "n-t"]:
        tags.pos.append(PartOfSpeech.Noun)
        tags.tags.append(tag)
    elif tag == "num":
        tags.pos.append(PartOfSpeech.Number)
    elif tag == "pn":
        tags.pos.append(PartOfSpeech.Pronoun)
    elif tag == "pref":
        tags.tags.append("pref")
    elif tag == "prt":
        tags.pos.append(PartOfSpeech.Particle)
    elif tag == "suf":
        tags.tags.append("suf")
    elif tag == "unc":
        # Make this 'X'?
        tags.tags.append("unc")
    elif tag in [
        "v1",
        "v1-s",
        "v2a-s",
        "v4h",
        "v4r",
        "v5aru",
        "v5b",
        "v5g",
        "v5k",
        "v5k-s",
        "v5m",
        "v5n",
        "v5r",
        "v5r-i",
        "v5s",
        "v5t",
        "v5u",
        "v5u-s",
        "v5uru",
        "vz",
        "vi",
        "vk",
        "vn",
        "vr",
        "vs",
        "vs-c",
        "vs-s",
        "vs-i",
        "vt",
        "v-unspec",  # Did not find in the JMDict file. Deprecated?
        "v4k",  # Archaic verbs from here
        "v4g",
        "v4s",
        "v4t",
        "v4n",
        "v4b",
        "v4m",
        "v2k-k",
        "v2g-k",
        "v2t-k",
        "v2d-k",
        "v2h-k",
        "v2b-k",
        "v2m-k",
        "v2y-k",
        "v2r-k",
        "v2k-s",
        "v2g-s",
        "v2s-s",
        "v2z-s",
        "v2t-s",
        "v2d-s",
        "v2n-s",
        "v2h-s",
        "v2b-s",
        "v2m-s",
        "v2y-s",
        "v2r-s",
        "v2w-s",
    ]:
        tags.pos.append(PartOfSpeech.Verb)
        tags.tags.append(tag)
    elif tag == "n-pr":
        tags.pos.append(PartOfSpeech.ProperNoun)
    elif tag in [
        "news1",
        "news2",
        "ichi1",
        "ichi2",
        "gai1",
        "gai2",
        "spec1",
        "spec2",
    ]:
        tags.tags.append(tag)
    elif re.match(r"^nf\d\d$", tag):
        tags.tags.append(tag)
    else:
        raise ValueError('Unsupported tag "%s"' % (tag))

    return tags
