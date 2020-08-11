from typing import Dict, List, Optional, Union

from pydantic import BaseModel

from omnilingual import LanguageCode, PartOfSpeech


class JMDictLanguageSource(BaseModel):
    language: LanguageCode

    type: str
    word: Optional[str]

    wasei: bool


class JMDictSense(BaseModel):
    number: int

    stagk: List[str]
    stagr: List[str]

    pos: List[str]

    xref: List[str]
    ant: List[str]

    field: List[str]
    misc: List[str]

    lsource: Dict[LanguageCode, List[JMDictLanguageSource]]

    dial: List[str]
    gloss: Dict[LanguageCode, List[str]]
    s_inf: List[str]


class JMDictKElement(BaseModel):
    keb: str

    ke_inf: List[str]
    ke_pri: List[str]


class JMDictRElement(BaseModel):
    reb: str

    re_nokanji: bool
    re_restr: List[str]

    re_inf: List[str]
    re_pri: List[str]


class JMDictEntry(BaseModel):
    ent_seq: int

    k_ele: List[JMDictKElement]
    r_ele: List[JMDictRElement]

    senses: List[JMDictSense]


class JMDictDictionary(BaseModel):
    date_created: str

    entries: List[JMDictEntry]


class JMDictJsonKeb(BaseModel):
    keb: str

    pos: List[PartOfSpeech]
    tags: List[str]


class JMDictJsonReb(BaseModel):
    reb: str

    pos: List[PartOfSpeech]
    tags: List[str]

    nokanji: bool
    only_for: List[str]


class JMDictJsonSense(BaseModel):
    number: int

    pos: List[PartOfSpeech]
    tags: List[str]

    information: List[str]
    definitions: Dict[str, List[str]]

    references: List[str]
    antonyms: List[str]

    source_words: Dict[str, List[JMDictLanguageSource]]


SenseNumberToWordMap = Dict[int, List[str]]


class JMDictIntermediateEntry(BaseModel):
    sources: Dict[str, Union[str, int]]

    kebs: List[JMDictJsonKeb]
    rebs: List[JMDictJsonReb]
    senses: List[JMDictJsonSense]

    sense_map: SenseNumberToWordMap
