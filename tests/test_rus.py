import unittest

from documental.token import PunctuationToken, WordToken
from omniglot.rus.parse import RussianParser
from omnilingual import LanguageCode, PartOfSpeech
from omnilingual.features import Animacy, Case, Features, Gender, Number


class TestRussian(unittest.TestCase):
    def setUp(self):
        self.parser = RussianParser()

        self.maxDiff = None

    def test_parses_sentences(self):
        tokens = self.parser.process(
            "Райан Рейнольдс и Хью Джекман годами троллили друг друга."
        )

        expected_tokens = [
            WordToken(
                "Райан",
                LanguageCode.Russian,
                "райан",
                pos=PartOfSpeech.Noun,
                features=Features(
                    Animacy=Animacy.Anim,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    Case=Case.Nom,
                ),
            ),
            WordToken(
                "Рейнольдс",
                LanguageCode.Russian,
                "рейнольдс",
                pos=PartOfSpeech.Noun,
                features=Features(
                    Animacy=Animacy.Anim,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    Case=Case.Nom,
                ),
            ),
            WordToken("и", LanguageCode.Russian, pos=PartOfSpeech.Conjunction),
            WordToken(
                "Хью",
                LanguageCode.Russian,
                "хью",
                pos=PartOfSpeech.Noun,
                features=Features(
                    Animacy=Animacy.Anim,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    Case=Case.Gen,
                ),
            ),
            WordToken(
                "Джекман",
                LanguageCode.Russian,
                "джекман",
                pos=PartOfSpeech.Noun,
                features=Features(
                    Animacy=Animacy.Anim,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    Case=Case.Nom,
                ),
            ),
            WordToken("годами", LanguageCode.Russian, pos=PartOfSpeech.Adverb),
            WordToken(
                "троллили",
                LanguageCode.Russian,
                pos=PartOfSpeech.Noun,
                features=Features(
                    Animacy=Animacy.Anim,
                    Gender=Gender.Fem,
                    Number=Number.Sing,
                    Case=Case.Nom,
                ),
            ),
            WordToken(
                "друг",
                LanguageCode.Russian,
                pos=PartOfSpeech.Noun,
                features=Features(
                    Animacy=Animacy.Anim,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    Case=Case.Nom,
                ),
            ),
            WordToken(
                "друга",
                LanguageCode.Russian,
                "друг",
                pos=PartOfSpeech.Noun,
                features=Features(
                    Animacy=Animacy.Anim,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    Case=Case.Gen,
                ),
            ),
            PunctuationToken(".", sticks_left=True),
        ]

        self.assertListEqual(tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
