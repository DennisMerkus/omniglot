import unittest

from documental import Text
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

    def test_parses_sentences(self):
        tokenized = self.parser.process(
            Text(
                "O coronavírus ataca as pessoas de maneiras diferentes.",
                LanguageCode.Portuguese,
            )
        )

        expected_tokens = [
            WordToken(
                "O",
                LanguageCode.Portuguese,
                "o",
                pos=PartOfSpeech.Determiner,
                features=Features(
                    definite=Definite.Def,
                    gender=Gender.Masc,
                    number=Number.Sing,
                    pron_type=PronType.Art,
                ),
            ),
            WordToken(
                "coronavírus",
                LanguageCode.Portuguese,
                pos=PartOfSpeech.Noun,
                features=Features(gender=Gender.Masc, number=Number.Sing),
            ),
            WordToken(
                "ataca",
                LanguageCode.Portuguese,
                pos=PartOfSpeech.Verb,
                features=Features(
                    mood=Mood.Ind,
                    number=Number.Sing,
                    person=Person.Third,
                    tense=Tense.Pres,
                    verb_form=VerbForm.Fin,
                ),
            ),
            WordToken(
                "as",
                LanguageCode.Portuguese,
                pos=PartOfSpeech.Determiner,
                features=Features(
                    definite=Definite.Def,
                    gender=Gender.Fem,
                    number=Number.Plur,
                    pron_type=PronType.Art,
                ),
            ),
            WordToken(
                "pessoas",
                LanguageCode.Portuguese,
                features=Features(gender=Gender.Fem, number=Number.Plur),
            ),
            WordToken("de", LanguageCode.Portuguese),
            WordToken(
                "maneiras",
                LanguageCode.Portuguese,
                features=Features(gender=Gender.Fem, number=Number.Plur),
            ),
            WordToken(
                "diferentes",
                LanguageCode.Portuguese,
                features=Features(gender=Gender.Fem, number=Number.Plur),
            ),
            PunctuationToken("."),
        ]

        self.assertListEqual(tokenized.tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
