import unittest

import pytest

from omniglot.zbn.dictionary import BanuDictionaryEntry, parse_entry
from omnilingual import PartOfSpeech
from omnilingual.features.zbn import BanuNounClass, BanuVerbType


class TestBanuDictionary(unittest.TestCase):
    @pytest.mark.asyncio
    async def test_ktako(self):
        entry = "ktako (ktakowæ) ktako(ktakowæ) v.T2 hurt; be painful - .eto sese sara renge ktako. “I’ve already eaten ’til it hurts.”"

        parsed_entry = parse_entry(entry)

        self.assertEqual(
            parsed_entry,
            BanuDictionaryEntry(
                word="ktako",
                emphatic="ktakowæ",
                pos=PartOfSpeech.Verb,
                verb_type=BanuVerbType.Type2,
                definition="hurt; be painful - .eto sese sara renge ktako. “I’ve already eaten ’til it hurts.”",
            ),
        )

    @pytest.mark.asyncio
    async def test_esse(self):
        entry = "esse (enge) esse(enge) n. cause, reason"

        parsed_entry = parse_entry(entry)

        self.assertEqual(
            parsed_entry,
            BanuDictionaryEntry(
                word="esse",
                pos=PartOfSpeech.Noun,
                noun_classes=[BanuNounClass.enge],
                definition="cause, reason",
            ),
        )

    @pytest.mark.asyncio
    async def test_lae(self):
        entry = "-læ 1 læ pn.io.r. to them (third person plural) indirect object/recipient (suffix/clitic)."

        parsed_entry = parse_entry(entry)

        self.assertEqual(
            parsed_entry,
            BanuDictionaryEntry(
                word="-læ",
                pos=PartOfSpeech.Pronoun,
                definition="to them (third person plural) indirect object/recipient (suffix/clitic).",
                number=1,
            ),
        )

    @pytest.mark.asyncio
    async def test_dale_aya(self):
        entry = "dale aya (go) dale aya(go) n. “serial number” (“the unique number”)."

        parsed_entry = parse_entry(entry)

        self.assertEqual(
            parsed_entry,
            BanuDictionaryEntry(
                word="dale aya",
                pos=PartOfSpeech.Noun,
                noun_classes=[BanuNounClass.go],
                definition="“serial number” (“the unique number”).",
            ),
        )
