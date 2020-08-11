from enum import Enum, unique


@unique
class Usage(Enum):
    ExclusivelyKana = "?ExclusivelyKana"
    ExclusivelyKanji = "?ExclusivelyKanji"
    Giku = "?Gikun"
    IrregularKana = "?IrregularKana"
    IrregularKanji = "?IrregularKanji"
    IrregularOkurigana = "?IrregularOkurigana"
    IrregularVerb = "?IrregularVerb"
    OutdatedKana = "?OutdatedKana"
    OutdatedKanji = "?OutdatedKanji"
    OldKana = "?OldKana"
    UsuallyKanji = "?UsuallyKanji"
    UsuallyKana = "?UsuallyKana"
