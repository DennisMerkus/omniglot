import unittest

import pytest
from omnilingual import PartOfSpeech
from omnilingual.features.uxy import XianMood

from bs4 import BeautifulSoup
from omniglot.uxy.dictionary import XianDictionaryEntry, parse_entries, parse_entry

from .test_xian_dictionary import dictionary


class TestXianDictionary(unittest.TestCase):
    @pytest.mark.asyncio
    async def test_it_finds_the_dictionary_start(self):
        entries = parse_entries(BeautifulSoup(dictionary, "lxml"))

        start = next(entries)

        self.assertIn("in the Familiar verb paradigm", start.get_text())

    @pytest.mark.asyncio
    async def test_hao(self):
        entry = """
        <tr>
        <td><strong> hao </strong></td>
        <td>v.LAUD</td>
        <td>be of a class</td>
        </tr>
        """

        parsed_entry = parse_entry(BeautifulSoup(entry, "lxml").find("tr"))

        self.assertEqual(
            parsed_entry,
            XianDictionaryEntry(
                word="hao",
                pos=PartOfSpeech.Verb,
                form=XianMood.Laudative,
                definition="be of a class",
            ),
        )

    @pytest.mark.asyncio
    async def teste_nyaoa(self):
        entry = """
        <tr>
        <td><strong> nya•oa </strong></td>
        <td>PN.role</td>
        <td>programmer/computation engineer</td>
        </tr>
        """

        parsed_entry = parse_entry(BeautifulSoup(entry, "lxml").find("tr"))

        self.assertEqual(
            parsed_entry,
            XianDictionaryEntry(
                word="nya•oa",
                pos=PartOfSpeech.ProperNoun,
                definition="programmer/computation engineer",
                occupation=True,
            ),
        )
