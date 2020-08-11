from typing import Optional

from pydantic import BaseModel

from omniglot.dictionary import Orthography


class RussianOrthography(Orthography):
    bare: str
    accented: str


class RussianNounFeatures(BaseModel):
    Gender: Optional[str]  # Masc, Fem, Neut, Both?
    Animacy: Optional[str]  # Anim, Inan


class RussianVerbFeatures(BaseModel):
    Aspect: Optional[str]  # Imp, Perf, Both


class RussianAdjectiveFeatures(BaseModel):
    incomparable: Optional[bool]

    Pos: str  # Positive, first order
    Cmp: Optional[str]  # Comparative, second order
    Sup: Optional[str]  # Superlative, third order

    # Short forms
    shortMasc: Optional[str]
    shortFem: Optional[str]
    shortNeut: Optional[str]
    shortPlur: Optional[str]


class RussianDeclensions(BaseModel):
    # Cases
    Nom: Optional[str]
    Gen: Optional[str]
    Dat: Optional[str]
    Acc: Optional[str]
    Ins: Optional[str]
    Loc: Optional[str]


class RussianAdjectiveDeclensions(BaseModel):
    Masc: RussianDeclensions
    Fem: RussianDeclensions
    Neut: RussianDeclensions
    Plur: RussianDeclensions


class RussianVerbConjugations(BaseModel):
    ImpSing: Optional[str]
    ImpPlur: Optional[str]

    PastMasc: Optional[str]
    PastFem: Optional[str]
    PastNeut: Optional[str]
    PastPlur: Optional[str]

    PresSing1: Optional[str]
    PresSing2: Optional[str]
    PresSing3: Optional[str]

    PresPlur1: Optional[str]
    PresPlur2: Optional[str]
    PresPlur3: Optional[str]
