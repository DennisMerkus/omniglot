from enum import Enum, unique

from typing import List

from pydantic import BaseModel

from .symbols import WordnetPointerSymbol


@unique
class WordnetPOS(Enum):
    Noun = "n"
    Verb = "v"
    Adjective = "a"
    Adverb = "r"
    AdjectiveSatellite = "s"


# see wndb(5WN)
class WordnetIndex(BaseModel):
    lemma: str
    pos: WordnetPOS

    synset_cnt: int  # number of synsets
    p_cnt: int  # number of total pointers

    ptr_symbol: List[str]  # see wninput(5WN), can be empty

    sense_cnt: int  # redundant
    tagsense_cnt: int

    synset_offset: List[str]  # at least one, 8 digits


class WordnetIdentifier(BaseModel):
    word: str
    lex_id: int  # 1 digit hexademical integer, identifies sense with lemma


class WordnetPointer(BaseModel):
    pointer_symbol: WordnetPointerSymbol
    synset_offset: str
    pos: WordnetPOS
    source: int  # relating to the `word` fields in a sysnset, beginning with 1
    target: int  # source/target is one 4 decimal digit field with 2 2 decimal ints


# see wndb(5WN)
class WordnetData(BaseModel):
    synset_offset: str

    lex_filenum: str  # see lexnames(5WN)
    ss_type: WordnetPOS  # n, v, a, s, r

    w_cnt: int  # 2 digit hexademical integer in file

    words: List[WordnetIdentifier]  # at least one

    p_cnt: int  # 3 digit decimal integer in file
    pointers: List[WordnetPointer]

    gloss: str


class WordnetFrame(BaseModel):
    f_num: int
    w_num: int  # two digit hexadecimal integer


class WordnetVerbData(WordnetData):
    frames: List[WordnetFrame]


class MultilingualWordnetEntry(BaseModel):
    offset: str
    pos: WordnetPOS

    language: str


class MultilingualWordnetLemma(MultilingualWordnetEntry):
    lemma: str


class MultilingualWordnetDefinition(MultilingualWordnetEntry):
    definition: str


class MultilingualWordnetExample(MultilingualWordnetEntry):
    example: str


class MultiLingualWordnetData(BaseModel):
    definitions: List[MultilingualWordnetDefinition]
    examples: List[MultilingualWordnetExample]
    lemmas: List[MultilingualWordnetLemma]
