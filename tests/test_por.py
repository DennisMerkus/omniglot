import unittest

from documental.token import PunctuationToken, WordToken
from omnilingual import LanguageCode, PartOfSpeech
from omnilingual.features import (
    Definite,
    Features,
    Gender,
    Mood,
    Number,
    Person,
    PronType,
    Tense,
    VerbForm,
)

from omniglot.por.parse import PortugueseParser


class TestPortuguese(unittest.TestCase):
    def setUp(self):
        self.parser = PortugueseParser()

        self.maxDiff = None

    def test_parses_sentences(self):
        tokens = self.parser.process(
            "O coronavírus ataca as pessoas de maneiras diferentes."
        )

        expected_tokens = [
            WordToken(
                "O",
                LanguageCode.Portuguese,
                "o",
                pos=PartOfSpeech.Determiner,
                features=Features(
                    Definite=Definite.Def,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    PronType=PronType.Art,
                ),
            ),
            WordToken(
                "coronavírus",
                LanguageCode.Portuguese,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            WordToken(
                "ataca",
                LanguageCode.Portuguese,
                "atacar",
                pos=PartOfSpeech.Verb,
                features=Features(
                    Mood=Mood.Ind,
                    Number=Number.Sing,
                    Person=Person.Third,
                    Tense=Tense.Pres,
                    VerbForm=VerbForm.Fin,
                ),
            ),
            WordToken(
                "as",
                LanguageCode.Portuguese,
                "o",
                pos=PartOfSpeech.Determiner,
                features=Features(
                    Definite=Definite.Def,
                    Gender=Gender.Fem,
                    Number=Number.Plur,
                    PronType=PronType.Art,
                ),
            ),
            WordToken(
                "pessoas",
                LanguageCode.Portuguese,
                "pessoa",
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Fem, Number=Number.Plur),
            ),
            WordToken("de", LanguageCode.Portuguese, "de", PartOfSpeech.Adposition),
            WordToken(
                "maneiras",
                LanguageCode.Portuguese,
                "maneiro",
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Fem, Number=Number.Plur),
            ),
            WordToken(
                "diferentes",
                LanguageCode.Portuguese,
                "diferente",
                pos=PartOfSpeech.Adjective,
                features=Features(Gender=Gender.Fem, Number=Number.Plur),
            ),
            PunctuationToken(".", sticks_left=True),
        ]

        self.assertListEqual(tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
