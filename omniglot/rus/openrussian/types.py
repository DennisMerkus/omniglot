from typing import Optional

from pydantic import BaseModel

from omnilingual import LanguageCode


class OpenRussianWord(BaseModel):
    id: int

    position: Optional[int]

    bare: str
    accented: str

    derived_from_word_id: Optional[int]
    rank: Optional[int]
    disabled: bool

    audio: Optional[str]  # URL on openrussian.org domain

    usage_en: Optional[str]
    usage_de: Optional[str]

    number_value: Optional[str]

    type: Optional[str]

    level: Optional[str]  # CEFR level


class OpenRussianTranslation(BaseModel):
    id: int

    language: LanguageCode  # iso-2 code, en or de

    word_id: int
    position: int

    tl: str

    example_ru: Optional[str]
    example_tl: Optional[str]

    info: Optional[str]


class OpenRussianNoun(BaseModel):
    word_id: int

    gender: Optional[str]

    partner: Optional[str]

    animate: Optional[bool]
    indeclinable: Optional[bool]

    sg_only: Optional[bool]
    pl_only: Optional[bool]

    decl_sg_id: Optional[int]
    decl_pl_id: Optional[int]


class OpenRussianVerb(BaseModel):
    word_id: int

    aspect: Optional[str]

    partner: Optional[str]

    imperative_sg: Optional[str]
    imperative_pl: Optional[str]

    past_m: Optional[str]
    past_f: Optional[str]
    past_n: Optional[str]
    past_pl: Optional[str]

    presfut_conj_id: int


class OpenRussianAdjective(BaseModel):
    word_id: int
    incomparable: Optional[bool]

    comparative: Optional[str]
    superlative: Optional[str]

    short_m: Optional[str]
    short_f: Optional[str]
    short_n: Optional[str]
    short_pl: Optional[str]

    decl_m_id: int
    decl_f_id: int
    decl_n_id: int
    decl_pl_id: int


class OpenRussianConjugation(BaseModel):
    id: int
    word_id: int  # Verb id

    sg1: Optional[str]
    sg2: Optional[str]
    sg3: Optional[str]

    pl1: Optional[str]
    pl2: Optional[str]
    pl3: Optional[str]


class OpenRussianDeclension(BaseModel):
    id: int
    word_id: int  # Noun id

    nom: Optional[str]
    gen: Optional[str]
    dat: Optional[str]
    acc: Optional[str]
    inst: Optional[str]
    prep: Optional[str]
