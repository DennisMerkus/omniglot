import unittest

from documental.token import PunctuationToken, WordToken
from omnilingual import LanguageCode, PartOfSpeech

from omniglot.deu.parse import GermanParser


class TestGerman(unittest.TestCase):
    def setUp(self):
        self.parser = GermanParser()

        self.maxDiff = None

    def test_parses_sentences(self):
        tokens = self.parser.process(
            "Die wei­ßen Evan­ge­li­ka­len in den USA gel­ten als ein­ge­schwo­re­ne Ge­mein­schaft."
        )

        expected_tokens = [
            WordToken("Die", LanguageCode.German, "der", pos=PartOfSpeech.Determiner),
            WordToken("wei­ßen", LanguageCode.German, pos=PartOfSpeech.Adjective),
            WordToken("Evan­ge­li­ka­len", LanguageCode.German, pos=PartOfSpeech.Noun),
            WordToken("in", LanguageCode.German, pos=PartOfSpeech.Adposition),
            WordToken("den", LanguageCode.German, "der", pos=PartOfSpeech.Determiner),
            WordToken("USA", LanguageCode.German, pos=PartOfSpeech.ProperNoun),
            WordToken("gel­ten", LanguageCode.German, pos=PartOfSpeech.Auxiliary),
            WordToken(
                "als", LanguageCode.German, pos=PartOfSpeech.CoordinatingConjunction,
            ),
            # TODO: Something weird with detecting the POS for this. General fix?
            WordToken(
                "ein­ge­schwo­re­ne", LanguageCode.German, pos=PartOfSpeech.ProperNoun
            ),
            WordToken("Ge­mein­schaft", LanguageCode.German, pos=PartOfSpeech.Noun),
            PunctuationToken(".", sticks_left=True),
        ]

        self.assertListEqual(tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
