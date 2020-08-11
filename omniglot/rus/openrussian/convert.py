import os.path
from collections import defaultdict
from typing import Dict, List, Optional, Union

from omniglot.sense import Sense
from omniglot.lexeme import Lexeme
from omnilingual import LanguageCode, PartOfSpeech
from omnilingual.features import Animacy, Gender

from ..types import RussianDeclensions, RussianOrthography, RussianVerbConjugations
from .parse import (
    parseAdjectivesFile,
    parseConjugationsFile,
    parseDeclensionsFile,
    parseNounsFile,
    parseTranslationsFile,
    parseVerbsFile,
    parseWordsFile,
)
from .types import (
    OpenRussianAdjective,
    OpenRussianConjugation,
    OpenRussianDeclension,
    OpenRussianNoun,
    OpenRussianTranslation,
    OpenRussianVerb,
    OpenRussianWord,
)

convert_pos: Dict[str, PartOfSpeech] = {
    "noun": PartOfSpeech.Noun,
    "verb": PartOfSpeech.Verb,
    "adjective": PartOfSpeech.Adjective,
    "adverb": PartOfSpeech.Adverb,
}


convert_gender: Dict[str, Gender] = {
    "m": Gender.Masc,
    "f": Gender.Fem,
    "n": Gender.Neut,
    "both": Gender.Both,
}

convert_aspect = {
    "imperfective": "Imp",
    "perfective": "Perf",
    "both": "Both",  # Convert to list?
}


def extract_declensions(declension: OpenRussianDeclension):
    return {
        "Nom": declension.nom,
        "Gen": declension.gen,
        "Dat": declension.dat,
        "Acc": declension.acc,
        "Ins": declension.inst,
        "Loc": declension.prep,
    }


def extract_adjective_declensions(
    adjective: OpenRussianAdjective, declensions: Dict[int, OpenRussianDeclension],
):
    if hasattr(adjective, "decl_m_id"):
        masc = extract_declensions(declensions[adjective.decl_m_id])
    else:
        masc = None

    if hasattr(adjective, "decl_f_id"):
        fem = extract_declensions(declensions[adjective.decl_f_id])
    else:
        fem = None

    if hasattr(adjective, "decl_n_id"):
        neut = extract_declensions(declensions[adjective.decl_n_id])
    else:
        neut = None

    if hasattr(adjective, "decl_pl_id"):
        plur = extract_declensions(declensions[adjective.decl_pl_id])
    else:
        plur = None

    return {"Masc": masc, "Fem": fem, "Neut": neut, "Plur": plur}


async def convert_OpenRussian(base_path: str) -> List[Lexeme]:
    words: Dict[int, OpenRussianWord] = await parseWordsFile(
        os.path.join(base_path, "words.csv.clean")
    )
    translations: Dict[int, List[OpenRussianTranslation]] = await parseTranslationsFile(
        "./cache/openrussian-csv/translations.csv.clean"
    )
    nouns: Dict[int, OpenRussianNoun] = await parseNounsFile(
        os.path.join(base_path, "nouns.csv.clean")
    )
    verbs: Dict[int, OpenRussianVerb] = await parseVerbsFile(
        os.path.join(base_path, "verbs.csv.clean")
    )
    adjectives: Dict[int, OpenRussianAdjective] = await parseAdjectivesFile(
        os.path.join(base_path, "adjectives.csv.clean")
    )
    conjugations: Dict[int, OpenRussianConjugation] = await parseConjugationsFile(
        os.path.join(base_path, "conjugations.csv.clean")
    )
    declensions: Dict[int, OpenRussianDeclension] = await parseDeclensionsFile(
        os.path.join(base_path, "declensions.csv.clean")
    )

    entries: List[Lexeme] = []

    for word_id, word in words.items():
        tags = []

        word_declensions: Optional[RussianDeclensions] = None
        verb_conjugations: Optional[RussianVerbConjugations] = None
        features: Optional[Dict[str, Union[str, bool, None]]] = None

        if word.type is not None:
            if word.type in convert_pos:
                pos = convert_pos[word.type]
            else:
                pos = PartOfSpeech.Nil

            if word.type == "expression":
                tags.append("!Expression")

            if pos is PartOfSpeech.Noun:
                word_noun = nouns[word_id]

                if word_noun.gender is None:
                    gender: Optional[Gender] = None
                else:
                    gender = convert_gender[word_noun.gender]

                if word_noun.animate is None:
                    animacy: Optional[Animacy] = None
                elif word_noun.animate is True:
                    animacy = Animacy.Anim
                else:
                    animacy = Animacy.Inan

                features = {
                    "Animacy": None if animacy is None else animacy.value,
                    "Gender": None if gender is None else gender.value,
                }

                if word_id in declensions:
                    this_word_declensions = declensions[word_id]
                    if this_word_declensions is not None:
                        word_declensions = extract_declensions(this_word_declensions)
            elif pos is PartOfSpeech.Verb:
                word_verb = verbs[word_id]

                word_aspect: Optional[str] = None
                if word_verb.aspect is not None:
                    word_aspect = convert_aspect[word_verb.aspect]

                features = {"Aspect": word_aspect}

                # TODO: Skipping `partner` for now

                verb_presfut = conjugations[word_verb.presfut_conj_id]

                verb_conjugations = RussianVerbConjugations(
                    ImpSing=word_verb.imperative_sg,
                    ImpPlur=word_verb.imperative_pl,
                    PastMasc=word_verb.past_m,
                    PastFem=word_verb.past_f,
                    PastNeut=word_verb.past_n,
                    PastPlur=word_verb.past_pl,
                    PresSing1=verb_presfut.sg1,
                    PresSing2=verb_presfut.sg2,
                    PresSing3=verb_presfut.sg3,
                    PresPlur1=verb_presfut.pl1,
                    PresPlur2=verb_presfut.pl2,
                    PresPlur3=verb_presfut.pl3,
                )
            elif pos is PartOfSpeech.Adjective:
                word_adjective = adjectives[word_id]

                features = {
                    "incomparable": word_adjective.incomparable,
                    "Pos": word.accented,
                    "Cmp": word_adjective.comparative,
                    "Sup": word_adjective.superlative,
                    "shortMasc": word_adjective.short_m,
                    "shortFem": word_adjective.short_f,
                    "shortNeut": word_adjective.short_n,
                    "shortPlur": word_adjective.short_pl,
                }

                word_declensions = extract_adjective_declensions(
                    word_adjective, declensions
                )

        if word.level is not None:
            tags.append("CEFR:%s" % (word.level))

        word_translations: List[OpenRussianTranslation] = translations[word_id]

        senses: List[Sense] = []

        # Gather by position/number
        gathered_translations: Dict[int, List[OpenRussianTranslation]] = defaultdict(
            list
        )

        information = []

        for word_translation in word_translations:
            if word_translation.info is not None:
                information.append(word_translation.info)

            gathered_translations[word_translation.position].append(word_translation)

        for (position, gathered_translation_list,) in gathered_translations.items():
            english_definitions = []
            german_definitions = []

            for gathered_translation in gathered_translation_list:
                if gathered_translation.language == LanguageCode.English:
                    english_definitions.append(gathered_translation.tl)
                elif gathered_translation.language == LanguageCode.German:
                    german_definitions.append(gathered_translation.tl)

            all_definitions: Dict[LanguageCode, List[str]] = {}

            if len(english_definitions) > 0:
                all_definitions[LanguageCode.English] = english_definitions

            if len(german_definitions) > 0:
                all_definitions[LanguageCode.German] = german_definitions

            senses.append(
                Sense(
                    definitions=all_definitions,
                    tags=[],
                    information=information,
                    references=[],
                    antonyms=[],
                    synonyms=[],  # TODO: OpenRussian has synonym data
                    source_language_words=[],
                )
            )

        entries.append(
            Lexeme(
                language=LanguageCode.Russian,
                lemma=word.bare,
                pos=pos,
                sources={"OpenRussian": word.id},
                orthography=RussianOrthography(
                    all=[word.bare, word.accented],
                    bare=word.bare,
                    accented=word.accented,
                ),
                tags=tags,
                senses=senses,
                features=features,
                declensions=word_declensions,
                conjugations=verb_conjugations,
            )
        )

    return entries
