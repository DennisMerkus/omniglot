import unittest
import pytest

from entwine.dictionary.jmdict.convert import create_JMDict_database_entries
from entwine.dictionary.jmdict.extract import convert_to_JSON

from omnilingual import PartOfSpeech

from .test_jmdict_entries import entry_America, entry_batsuichi


class TestJMDict(unittest.TestCase):
    @pytest.mark.asyncio
    async def test_converts_America_entry_correctly(self):
        lexemes = await create_JMDict_database_entries(
            await convert_to_JSON(entry_America)
        )

        self.assertEqual(len(lexemes), 1)

        lexeme = lexemes[0]

        self.assertSetEqual(set(lexeme.orthography.all), set(["亜米利加", "亜墨利加", "アメリカ"]))

        self.assertIn("アメリカ", lexeme.orthography.kana)

        self.assertEqual(lexeme.pos, PartOfSpeech.Noun)

        self.assertIn("?UsuallyKana", lexeme.tags)

    @pytest.mark.asyncio
    async def test_converts_restricted_kana_correctly(self):
        lexemes = await create_JMDict_database_entries(
            await convert_to_JSON(entry_batsuichi)
        )

        self.assertEqual(len(lexemes), 1)

        lexeme = lexemes[0]

        self.assertSetEqual(
            set(lexeme.orthography.all),
            set(["罰一", "ばつ一", "バツ１", "ばついち", "バツいち", "バツイチ"]),
        )
        self.assertSetEqual(set(lexeme.orthography.kana), set(["ばついち", "バツいち", "バツイチ"]))
        self.assertSetEqual(set(lexeme.orthography.kanji), set(["罰一", "ばつ一", "バツ１"]))

        self.assertEqual(lexeme.pos, PartOfSpeech.Noun)


if __name__ == "__main__":
    unittest.main()
