import functools
import itertools
from typing import List, Set

from omnilingual import LanguageCode, PartOfSpeech

from omniglot.jpn.types import JapaneseOrthography
from omniglot.lexeme import Lexeme
from omniglot.sense import Sense, SourceWord

from .tags import normalize_tag
from .types import (
    JMDictDictionary,
    JMDictEntry,
    JMDictIntermediateEntry,
    JMDictJsonKeb,
    JMDictJsonReb,
    JMDictJsonSense,
    JMDictSense,
    SenseNumberToWordMap,
)


def map_sense_to_kebs_and_rebs(
    senses: List[JMDictSense], kebs: List[JMDictJsonKeb], rebs: List[JMDictJsonReb],
) -> SenseNumberToWordMap:
    sense_map: SenseNumberToWordMap = {}

    for index in range(1, len(senses) + 1):
        sense_map[index] = []

    for sense in senses:
        if len(sense.stagk) == 0 and len(sense.stagr) == 0:
            for keb in kebs:
                sense_map[sense.number].append(keb.keb)

            for reb in rebs:
                sense_map[sense.number].append(reb.reb)
        else:
            if len(sense.stagk) > 0:
                for stagk in sense.stagk:
                    sense_map[sense.number].append(stagk)

            if len(sense.stagr) > 0:
                for stagr in sense.stagr:
                    sense_map[sense.number].append(stagr)

    return sense_map


def kanji_sets_with_common_readings(kebs: List[str], keb_readings) -> List[Set[str]]:
    sets = []
    for length in range(1, len(kebs) + 1):
        sets.append(itertools.combinations(kebs, length))

    kanji_sets = list(itertools.chain(sets))

    # Generate all kanji sets that have the same readings
    # 1. Generate all kanji sets
    # 2. Eliminate those that don't share all readings

    common_sets = []

    for kanjis in kanji_sets:
        first = list(kanjis)[0]

        readings = list(map(lambda x: keb_readings[x], kanjis))
        common = functools.reduce(lambda x, y: x & y, readings)

        if len(common) == len(first):
            common_sets.append(common)

    return common_sets


def extract_kebs(entry: JMDictEntry) -> List[JMDictJsonKeb]:
    kebs: List[JMDictJsonKeb] = []

    for k_ele in entry.k_ele:
        poses: List[PartOfSpeech] = []
        tags: List[str] = []

        for ke_inf in k_ele.ke_inf:
            normalized_tags = normalize_tag(ke_inf)
            poses.extend(normalized_tags.pos)
            tags.extend(normalized_tags.tags)

        for ke_pri in k_ele.ke_pri:
            normalized_tags = normalize_tag(ke_pri)
            poses.extend(normalized_tags.pos)
            tags.extend(normalized_tags.tags)

        kebs.append(JMDictJsonKeb(keb=k_ele.keb, pos=poses, tags=tags))

    return kebs


def extract_rebs(entry: JMDictEntry) -> List[JMDictJsonReb]:
    rebs: List[JMDictJsonReb] = []

    for r_ele in entry.r_ele:
        nokanji = False

        if r_ele.re_nokanji is True:
            nokanji = True

        only_for: List[str] = []
        if len(r_ele.re_restr) > 0:
            only_for = r_ele.re_restr

        poses: List[PartOfSpeech] = []
        tags: List[str] = []

        for re_inf in r_ele.re_inf:
            normalized_tags = normalize_tag(re_inf)
            poses.extend(normalized_tags.pos)
            tags.extend(normalized_tags.tags)

        for re_pri in r_ele.re_pri:
            normalized_tags = normalize_tag(re_pri)
            poses.extend(normalized_tags.pos)
            tags.extend(normalized_tags.tags)

        rebs.append(
            JMDictJsonReb(
                reb=r_ele.reb, pos=poses, tags=tags, nokanji=nokanji, only_for=only_for,
            )
        )

    return rebs


async def convert_JMDict_entry_intermediate(
    entries: List[JMDictEntry],
) -> List[JMDictIntermediateEntry]:
    intermediate_entries: List[JMDictIntermediateEntry] = []

    for jmdict_entry in entries:
        kebs: List[JMDictJsonKeb] = extract_kebs(jmdict_entry)
        rebs: List[JMDictJsonReb] = extract_rebs(jmdict_entry)

        sense_number_to_word_map = map_sense_to_kebs_and_rebs(
            jmdict_entry.senses, kebs, rebs
        )

        all_entry_poses: Set[PartOfSpeech] = set()
        all_entry_tags: Set[str] = set()

        for keb in kebs:
            all_entry_poses.update(keb.pos)
            all_entry_tags.update(keb.tags)

        for reb in rebs:
            all_entry_poses.update(reb.pos)
            all_entry_tags.update(reb.tags)

        # Delete these every time there's a new pos/misc
        cumulative_poses: Set[str] = set()
        cumulative_miscs: Set[str] = set()

        # Collect senses
        senses: List[JMDictJsonSense] = []
        for sense in jmdict_entry.senses:
            all_sense_tags: Set[str] = set()

            # TODO: xref
            references = []
            for xref in sense.xref:
                # TODO: Get the cross-reference
                references.append(xref)

            if len(sense.pos) > 0:
                cumulative_poses = set(sense.pos)

            all_sense_tags.update(cumulative_poses)

            antonyms = []
            for ant in sense.ant:
                # TODO: Get the cross-reference
                antonyms.append(ant)

            all_sense_tags.update(sense.field)

            if len(sense.misc) > 0:
                cumulative_miscs = set(sense.misc)

            all_sense_tags.update(cumulative_miscs)

            all_sense_tags.update(sense.dial)

            source_words = sense.lsource

            definitions = sense.gloss

            information = sense.s_inf

            normalized_poses: Set[PartOfSpeech] = set()
            normalized_tags: Set[str] = set()
            for tag in all_entry_tags.union(all_sense_tags):
                normalized = normalize_tag(tag)
                normalized_poses.update(normalized.pos)
                normalized_tags.update(normalized.tags)

            senses.append(
                JMDictJsonSense(
                    number=sense.number,
                    pos=list(normalized_poses.union(all_entry_poses)),
                    tags=list(normalized_tags),
                    information=information,
                    definitions=definitions,
                    references=references,
                    antonyms=antonyms,
                    source_words=source_words,
                )
            )

        intermediate_entries.append(
            JMDictIntermediateEntry(
                sources={"JMDict": jmdict_entry.ent_seq},
                kebs=kebs,
                rebs=rebs,
                senses=senses,
                sense_map=sense_number_to_word_map,
            )
        )

    return intermediate_entries


async def convert_intermediate_entries(
    intermediate_entries: List[JMDictIntermediateEntry],
) -> List[Lexeme]:
    # TODO: Return a single POS, turn everything else into tags
    database_entries: List[Lexeme] = []

    for entry in intermediate_entries:
        kanji: List[str] = [keb.keb for keb in entry.kebs]
        kana: List[str] = [reb.reb for reb in entry.rebs]

        lemmas: List[str] = kanji + kana

        lemma: str = lemmas[0]

        entry_poses: Set[PartOfSpeech] = set()
        entry_tags: Set[str] = set()

        database_senses: List[Sense] = []

        for word_sense in entry.senses:
            if len(set(lemmas) & set(entry.sense_map[word_sense.number])) > 0:
                source_language_words: List[SourceWord] = []

                entry_poses.update(word_sense.pos)
                entry_tags.update(word_sense.tags)

                for language in word_sense.source_words:
                    for word in word_sense.source_words[language]:
                        if word.type == "full":
                            full = True
                        elif word.type == "part":
                            full = False
                        else:
                            raise ValueError(
                                "[JMDict] Unexpected source word type %s" % (word.type)
                            )

                        if word.wasei is True:
                            source_tags = ["!Wasei"]
                        else:
                            source_tags = []

                        source_language_words.append(
                            SourceWord(
                                language=language,
                                word=word.word,
                                full=full,
                                tags=source_tags,
                            )
                        )

                database_senses.append(
                    Sense(
                        tags=word_sense.tags,
                        information=word_sense.information,
                        definitions=word_sense.definitions,
                        references=[],  # TODO: Where to get these xrefs?
                        antonyms=[],  # TODO: Fill in antonyms
                        synonyms=[],
                        source_language_words=source_language_words,
                    )
                )

        for keb in entry.kebs:
            entry_poses.update(keb.pos)
            entry_tags.update(keb.tags)

        for reb in entry.rebs:
            entry_poses.update(reb.pos)
            entry_tags.update(reb.tags)

        if len(entry_poses) == 1:
            pos: PartOfSpeech = next(iter(entry_poses))
        elif len(entry_poses) == 0:
            pos = PartOfSpeech.Nil
        elif (
            len(entry_poses) == 2
            and PartOfSpeech.Noun in entry_poses
            and PartOfSpeech.Verb in entry_poses
            and "vs" in entry_tags
        ):
            pos = PartOfSpeech.Noun
        else:
            raise NotImplementedError("Unhandled JMDict POS/tag combination")

        database_entries.append(
            Lexeme(
                language=LanguageCode.Japanese,
                lemma=lemma,
                pos=pos,
                orthography=JapaneseOrthography(
                    all=kanji + kana, kanji=kanji, kana=kana
                ),
                tags=list(entry_tags),
                senses=database_senses,
                sources=entry.sources,
                pronounce={"kana": kana},
            )
        )

    return database_entries


async def create_JMDict_database_entries(
    jmdict_dictionary: JMDictDictionary,
) -> List[Lexeme]:
    # 1. Convert kebs and rebs to lemmas
    # 2. Create sets of keb/reb+sense sets based on stagk/stagr data
    # 2a. Create subsets of keb/reb combinations based on reb's `restricted`
    # 3. Create dictionary entries from extracted sense subsets
    # 4. Cross-reference _ids for xref and ants
    # 5. Insert all entries into database
    intermediate_entries: List[
        JMDictIntermediateEntry
    ] = await convert_JMDict_entry_intermediate(jmdict_dictionary.entries)

    return await convert_intermediate_entries(intermediate_entries)
