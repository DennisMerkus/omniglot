import unittest

from documental.token import PunctuationToken, WordToken
from omnilingual import LanguageCode, PartOfSpeech

from omniglot.eng.parse import EnglishParser


class TestEnglish(unittest.TestCase):
    def setUp(self):
        self.parser = EnglishParser()

    def test_parses_sentences(self):
        tokens = self.parser.process("A fast-changing world can be a lonely place.")

        expected_tokens = [
            WordToken("A", LanguageCode.English, "a", pos=PartOfSpeech.Determiner),
            WordToken("fast", LanguageCode.English, pos=PartOfSpeech.Adverb),
            PunctuationToken("-"),
            WordToken(
                "changing", LanguageCode.English, "change", pos=PartOfSpeech.Verb,
            ),
            WordToken("world", LanguageCode.English, pos=PartOfSpeech.Noun),
            WordToken("can", LanguageCode.English, pos=PartOfSpeech.Verb),
            WordToken("be", LanguageCode.English, pos=PartOfSpeech.Auxiliary),
            WordToken("a", LanguageCode.English, pos=PartOfSpeech.Determiner),
            WordToken("lonely", LanguageCode.English, pos=PartOfSpeech.Adjective),
            WordToken("place", LanguageCode.English, pos=PartOfSpeech.Noun),
            PunctuationToken("."),
        ]

        self.assertListEqual(tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
