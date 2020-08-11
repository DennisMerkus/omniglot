from enum import Enum


class WordnetPointerSymbol(Enum):
    Antonym = "!"
    Hypernym = "@"

    InstanceHypernym = "@i"
    Hyponym = "~"
    InstanceHyponym = "~i"

    MemberHolonym = "#m"
    SubstanceHolonym = "#s"
    PartHolonym = "#p"

    MemberMeronym = "%m"
    SubstanceMeronym = "%%s"
    PartMeronym = "%p"

    Attribute = "="

    DerivationallyRelated = "+"

    TopicDomain = ";c"
    TopicMember = "-c"

    RegionDomain = ";r"
    RegionMember = "-r"

    UsageDomain = ";u"
    UsageMember = "-u"

    # Verb
    Entailment = "*"
    Cause = ">"
    SeeAlso = "^"

    VerbGroup = "$"

    # Adjective
    SimilarTo = "&"
    ParticipleOfVerb = "<"

    Pertainym = "\\"

    # Adverb
    DerivedFromAdjective = "\\"
