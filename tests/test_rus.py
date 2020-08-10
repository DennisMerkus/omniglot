import unittest

from documental import Text
from documental.token import PunctuationToken, WordToken
from omnilingual import LanguageCode, PartOfSpeech
from omnilingual.features import Animacy, Case, Features, Gender, Number

from omniglot.rus.parse import RussianParser


class TestRussian(unittest.TestCase):
    def setUp(self):
        self.parser = RussianParser()

    def test_parses_sentences(self):
        tokenized = self.parser.process(
            Text(
                "Райан Рейнольдс и Хью Джекман годами троллили друг друга.",
                LanguageCode.Russian,
            )
        )

        expected_tokens = [
            WordToken(
                "Райан",
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
                "Рейнольдс",
                LanguageCode.Russian,
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
                pos=PartOfSpeech.Noun,
                features=Features(
                    Animacy=Animacy.Anim,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    Case=Case.Gen,
                ),
            ),
            PunctuationToken("."),
        ]

        self.assertListEqual(tokenized.tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
