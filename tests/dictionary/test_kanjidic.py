import unittest

import pytest
from bs4 import BeautifulSoup

from entwine.database.kanji import Kanji
from entwine.dictionary.kanjidic.extract import convert_entry

from .test_kanjidic_entries import entry_意, entry_衣


class TestKanjidic(unittest.TestCase):
    @pytest.mark.asyncio
    async def test_should_convert_意(self):
        kanji: Kanji = convert_entry(BeautifulSoup(entry_意, "lxml-xml"))

        self.assertEqual(kanji.character, "意")
        self.assertEqual(kanji.stroke_count, 13)
        self.assertListEqual(kanji.on_readings, ["イ"])
        self.assertListEqual(kanji.kun_readings, [])

        self.assertDictEqual(
            kanji.meanings,
            {
                "eng": [
                    "idea",
                    "mind",
                    "heart",
                    "taste",
                    "thought",
                    "desire",
                    "care",
                    "liking",
                ],
                "fra": [
                    "idée",
                    "esprit",
                    "coeur",
                    "pensée",
                    "attention",
                    "goût",
                    "désir",
                ],
                "spa": ["idea", "sentimiento", "razón", "intención"],
                "por": [
                    "idéia",
                    "mente",
                    "coração",
                    "gosto",
                    "pensamento",
                    "desejo",
                    "atenção",
                ],
            },
        )

    @pytest.mark.asyncio
    async def test_should_convert_衣(self):
        kanji: Kanji = convert_entry(BeautifulSoup(entry_衣, "lxml-xml"))

        self.assertEqual(kanji.character, "衣")
        self.assertEqual(kanji.stroke_count, 6)
        self.assertListEqual(kanji.on_readings, ["イ", "エ"])
        self.assertListEqual(kanji.kun_readings, ["ころも", "きぬ", "-ぎ"])

        self.assertDictEqual(
            kanji.meanings,
            {
                "eng": ["garment", "clothes", "dressing"],
                "fra": ["vêtement", "habillement"],
                "spa": ["prenda", "ropas", "vestidos"],
                "por": ["vestuário", "roupas", "vestindo"],
            },
        )
