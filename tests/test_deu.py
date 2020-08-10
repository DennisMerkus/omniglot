import unittest

from documental import Text
from documental.token import PunctuationToken, WordToken
from omnilingual import LanguageCode, PartOfSpeech

from omniglot.deu.parse import GermanParser


class TestGerman(unittest.TestCase):
    def setUp(self):
        self.parser = GermanParser()

    def test_parses_sentences(self):
        tokenized = self.parser.process(
            Text(
                "Die wei­ßen Evan­ge­li­ka­len in den USA gel­ten als ein­ge­schwo­re­ne Ge­mein­schaft.",
                LanguageCode.German,
            )
        )

        expected_tokens = [
            WordToken("Die", LanguageCode.German, "die", pos=PartOfSpeech.Determiner),
            WordToken("wei­ßen", LanguageCode.German, pos=PartOfSpeech.Adjective),
            WordToken("Evan­ge­li­ka­len", LanguageCode.German, pos=PartOfSpeech.Noun),
            WordToken("in", LanguageCode.German, pos=PartOfSpeech.Adposition),
            WordToken("den", LanguageCode.German, pos=PartOfSpeech.Determiner),
            WordToken("USA", LanguageCode.German, pos=PartOfSpeech.ProperNoun),
            WordToken("gel­ten", LanguageCode.German, pos=PartOfSpeech.Auxiliary),
            WordToken(
                "als", LanguageCode.German, pos=PartOfSpeech.CoordinatingConjunction,
            ),
            # Something weird with detecting the POS for this
            WordToken("ein­ge­schwo­re­ne", LanguageCode.German),
            WordToken("Ge­mein­schaft", LanguageCode.German, pos=PartOfSpeech.Noun),
            PunctuationToken("."),
        ]

        self.assertListEqual(tokenized.tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
