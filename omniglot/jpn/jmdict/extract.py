import logging
import re
from collections import defaultdict
from datetime import date
from typing import Dict, List, Optional

from bs4 import BeautifulSoup

from omnilingual import Language, LanguageCode, PartOfSpeech

from .types import (
    JMDictDictionary,
    JMDictEntry,
    JMDictKElement,
    JMDictLanguageSource,
    JMDictRElement,
    JMDictSense,
)


def convert_jmdict_pos(pos: str) -> PartOfSpeech:
    pass


async def extract_created_date(xml: str) -> Optional[str]:
    JMDict_created_regexp = r"JMdict\s*created:\s*(\d{4}\-\d{2}\-\d{2})"
    match = re.search(JMDict_created_regexp, xml)

    if match:
        return date.fromisoformat(match.group(1)).isoformat()
    else:
        return None


def extract_sequence_number(entry: BeautifulSoup) -> int:
    result = entry.find("ent_seq")

    if not result:
        raise ValueError("Expected <entry> to have <ent_seq>.")
    else:
        return int(result.string)


def extract_senses(entry: BeautifulSoup) -> List[JMDictSense]:
    senses = []

    sense_number = 1
    for sense in entry.findAll("sense"):
        # If present, signals that this sense only applies to the <keb>
        # with the <stagk> string
        stagks: List[str] = []
        for stagk in sense.findAll("stagk"):
            stagks.append(stagk.string)

        stagrs: List[str] = []
        for stagr in sense.findAll("stagr"):
            stagrs.append(stagr.string)

        # TODO: Figure out how to cross-reference the entries
        xrefs: List[str] = []
        for xref in sense.findAll("xref"):
            xrefs.append(xref.string)

        poses: List[str] = []
        for pos in sense.findAll("pos"):
            poses.append(pos.string)

        # TODO: Match keb or reb in other entry
        ants: List[str] = []
        for ant in sense.findAll("ant"):
            ants.append(ant.string)

        fields: List[str] = []
        for field in sense.findAll("field"):
            fields.append(field.string)

        # If no field is found, it's for general use
        if len(fields) == 0:
            fields.append("#General")

        miscs: List[str] = []
        for misc in sense.findAll("misc"):
            miscs.append(misc.string)

        lsources: Dict[LanguageCode, List[JMDictLanguageSource]] = defaultdict(list)
        for lsource in sense.findAll("lsource"):
            lsource_code: LanguageCode

            if "xml:lang" in lsource.attrs:
                lsource_code = Language.where(tag=lsource["xml:lang"]).code
            else:
                lsource_code = LanguageCode.English

            if "ls_type" in lsource.attrs:
                ls_type = lsource["ls_type"]
            else:
                ls_type = "full"  # Default value when absent

            wasei = "ls_wasei" in lsource.attrs

            # Can be <lsource ... /> without content word
            word = lsource.string

            lsources[lsource_code].append(
                JMDictLanguageSource(
                    type=ls_type, word=word, wasei=wasei, language=lsource_code,
                )
            )

        dials: List[str] = []
        for dial in sense.findAll("dial"):
            dials.append(dial.string)

        # TODO: There's supposed to be a <pri> element for <gloss>
        # Could not find it

        glosses: Dict[LanguageCode, List[str]] = defaultdict(list)
        for gloss in sense.findAll("gloss"):
            gloss_code: LanguageCode

            if "xml:lang" in gloss.attrs:
                gloss_lang: str = gloss["xml:lang"]

                gloss_code = Language.where(tag=gloss_lang).code
            else:
                gloss_code = LanguageCode.English

            # There can be entries with an empty gloss (error in JMDict?)
            if gloss.string is not None:
                glosses[gloss_code].append(gloss.string)

        # A freeform sentence
        # Has some subsets of forms that I could exploit such as honorific use
        s_infs: List[str] = []
        for s_inf in sense.findAll("s_inf"):
            s_infs.append(s_inf.string)

        senses.append(
            JMDictSense(
                number=sense_number,
                stagk=stagks,
                stagr=stagrs,
                xref=xrefs,
                pos=poses,
                ant=ants,
                field=fields,
                misc=miscs,
                lsource=lsources,
                dial=dials,
                gloss=glosses,
                s_inf=s_infs,
            )
        )

    return senses


def extract_kanji_elements(entry: BeautifulSoup) -> List[JMDictKElement]:
    elements: List[JMDictKElement] = []

    for k_ele in entry.findAll("k_ele"):
        keb = k_ele.find("keb")

        if keb is None:
            raise ValueError("Expected <k_ele> to have <keb>.")

        ke_infs = []

        # TODO: In parser, transform possible tags
        for ke_inf in k_ele.findAll("ke_inf"):
            ke_infs.append(ke_inf.string)

        # TODO: In parser, transform possible tags
        ke_pris = []
        for ke_pri in k_ele.findAll("ke_pri"):
            ke_pris.append(ke_pri.string)

        elements.append(JMDictKElement(keb=keb.string, ke_inf=ke_infs, ke_pri=ke_pris))

    return elements


def extract_reading_elements(entry: BeautifulSoup) -> List[JMDictRElement]:
    elements: List[JMDictRElement] = []

    for r_ele in entry.findAll("r_ele"):
        reb = r_ele.find("reb")

        if reb is None:
            raise ValueError("Expected <r_ele> to have <reb>.")

        # If present, reading is not a strict reading of the k_ele kanji
        re_nokanji = r_ele.find("re_nokanji")

        nokanji = re_nokanji is not None

        restricted = []
        for re_restr in r_ele.findAll("re_restr"):
            # Normally, the current reb reading applies to all kanji
            # But there are re_restr, then the reading only applies to
            # a subset of the kanji in the re_restr elements
            restricted.append(re_restr.string)

        information = []
        for re_inf in r_ele.findAll("re_inf"):
            information.append(re_inf.string)

        priority = []
        for re_pri in r_ele.findAll("re_pri"):
            priority.append(re_pri.string)

        elements.append(
            JMDictRElement(
                reb=reb.string,
                re_nokanji=nokanji,
                re_restr=restricted,
                re_inf=information,
                re_pri=priority,
            )
        )

    return elements


def extract_entry(entry: BeautifulSoup) -> JMDictEntry:
    return JMDictEntry(
        ent_seq=extract_sequence_number(entry),
        k_ele=extract_kanji_elements(entry),
        r_ele=extract_reading_elements(entry),
        senses=extract_senses(entry),
    )


async def convert_to_JSON(xml: str) -> JMDictDictionary:
    created_date = await extract_created_date(xml)

    if created_date is None:
        raise ValueError("[JMDict] Could not find the created date.")

    logging.info("[JMDict] Dictionary version: %s" % (created_date))

    logging.info("[JMDict] Loading XML")

    soup = BeautifulSoup(xml, "lxml-xml")

    entry_count: int = 0
    entries: List[JMDictEntry] = []
    for entry in soup.findAll("entry"):
        entries.append(extract_entry(entry))

        entry_count += 1
        if entry_count % 1000 == 0:
            logging.info("Parsed %d entries." % (entry_count))

    return JMDictDictionary(date_created=created_date, entries=entries)
