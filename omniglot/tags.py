# TODO: Change this to a more sensible type, such as Enums.

field_tags = set(
    [
        "#Anatomy",
        "#Architecture",
        "#Astronomy",
        "#Baseball",
        "#Biology",
        "#Botany",
        "#Buddhism",
        "#Business",
        "#Chemistry",
        "#Christianity",
        "#Computer",
        "#Economics",
        "#Engineering",
        "#Finance",
        "#Food",
        "#General",
        "#Geology",
        "#Geometry",
        "#Law",
        "#Linguistics",
        "#Mahjong",
        "#MartialArts",
        "#Mathematics",
        "#Medicine",
        "#Military",
        "#Music",
        "#Physics",
        "#Shinto",
        "#Shogi",
        "#Sports",
        "#Sumo",
        "#Zoology",
    ]
)

usage_tags = set(
    [
        "!X-rated",
        "!Abbreviation",
        "!Archaism",
        "!Ateji",
        "!Children",
        "!Colloquialism",
        "!Outdated",
        "!Derogatory",
        "!Expression",
        "!Familiar",
        "!Female",
        "!Historical",
        "!Honorific",
        "!Sonkeigo",
        "!Humble",
        "!Kenjougo",
        "!Idiomatic",
        "!Jocular",
        "!Literary",
        "!Formal",
        "!Slang",
        "!MangaSlang",
        "!Male",
        "!MaleSlang",
        "!Internet",
        "!Obsolete",
        "!Obscure",
        "!Mimetic",
        "!Onomatopoeia",
        "!Poetical",
        "!Polite",
        "!Teineigo",
        "!Proverb",
        "!Quotation",
        "!Rare",
        "!Sensitive",
        "!Yojijukugo",
        "!Vulgar",
    ]
)

named_entity_tags = set(
    [
        "!Name",
        "!CompanyName",
        "!OrganizationName",
        "!PersonName",
        "!FirstName",
        "!LastName",
        "!FullName",
        "!PlaceName",
        "!ProductName",
        "!StationName",
        "!UnclassifiedName",
        "!WorkName",
    ]
)

japanese_specific_tags = set(
    [
        "?ExclusivelyKanji",
        "?ExclusivelyKana",
        "?Gikun",
        "?IrregularKana",
        "?IrregularKanji",
        "?IrregularOkurigana",
        "?IrregularVerb",
        "?OutdatedKanji",
        "?OutdatedKana",
        "?OldKana",
        "?UsuallyKanji",
        "?UsuallyKana",
    ]
)

japanese_dialect_tags = set(
    [
        "#Kyoto-ben",
        "#Osaka-ben",
        "#Kansai-ben",
        "#Kantou-ben",
        "#Tosa-ben",
        "#Touhoku-ben",
        "#Tsugaru-ben",
        "#Kyushu-ben",
        "#Ryukyu-ben",
        "#Nagano-ben",
        "#Hokkaido-ben",
    ]
)