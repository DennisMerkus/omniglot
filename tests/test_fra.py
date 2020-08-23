import unittest

from documental.token import Ellision, PunctuationToken, WordToken
from omniglot.fra.numbers import FrenchNumberConverter
from omniglot.fra.parse import FrenchParser
from omnilingual import LanguageCode, PartOfSpeech
from omnilingual.features import (
    Definite,
    Features,
    Gender,
    Mood,
    Number,
    Person,
    Polarity,
    Poss,
    PronType,
    Tense,
    VerbForm,
)


class TestFrenchParser(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

        self.parser = FrenchParser()

    def test_parses_sentence_1(self):
        tokens = self.parser.process(
            "Elle avait chevillé au corps le refus d’un destin préétabli."
        )

        expected_tokens = [
            WordToken(
                "Elle",
                LanguageCode.French,
                lemma="elle",
                pos=PartOfSpeech.Pronoun,
                features=Features(
                    Gender=Gender.Fem, Number=Number.Sing, Person=Person.Third,
                ),
            ),
            WordToken(
                "avait",
                LanguageCode.French,
                lemma="avoir",
                pos=PartOfSpeech.Auxiliary,
                features=Features(
                    Mood=Mood.Ind,
                    Number=Number.Sing,
                    Person=Person.Third,
                    Tense=Tense.Imp,
                    VerbForm=VerbForm.Fin,
                ),
            ),
            WordToken(
                "chevillé",
                LanguageCode.French,
                lemma="cheviller",
                pos=PartOfSpeech.Verb,
                features=Features(
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    Tense=Tense.Past,
                    VerbForm=VerbForm.Part,
                ),
            ),
            WordToken(
                "au",
                LanguageCode.French,
                pos=PartOfSpeech.Determiner,
                features=Features(
                    Definite=Definite.Def,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    PronType=PronType.Art,
                ),
            ),
            WordToken(
                "corps",
                LanguageCode.French,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            WordToken(
                "le",
                LanguageCode.French,
                pos=PartOfSpeech.Determiner,
                features=Features(
                    Definite=Definite.Def,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    PronType=PronType.Art,
                ),
            ),
            WordToken(
                "refus",
                LanguageCode.French,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            Ellision(
                "d’un",
                [
                    WordToken("de", LanguageCode.French, pos=PartOfSpeech.Adposition),
                    WordToken(
                        "un",
                        LanguageCode.French,
                        pos=PartOfSpeech.Determiner,
                        features=Features(
                            Definite=Definite.Ind,
                            Gender=Gender.Masc,
                            Number=Number.Sing,
                            PronType=PronType.Art,
                        ),
                    ),
                ],
                LanguageCode.French,
            ),
            WordToken(
                "destin",
                LanguageCode.French,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            WordToken(
                "préétabli",
                LanguageCode.French,
                lemma="préétablir",
                pos=PartOfSpeech.Verb,
                features=Features(
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    Tense=Tense.Past,
                    VerbForm=VerbForm.Part,
                ),
            ),
            PunctuationToken(".", sticks_left=True),
        ]

        self.assertListEqual(tokens, expected_tokens)

    def test_parses_sentence_2(self):
        tokens = self.parser.process(
            "Malgré la présence de Simandou, plus grand gisement de fer non exploité au monde, sur son territoire, le pays d’Afrique de l’Ouest n’en a pas extrait un seul gramme en vingt ans."
        )

        expected_tokens = [
            WordToken(
                "Malgré",
                LanguageCode.French,
                lemma="malgré",
                pos=PartOfSpeech.Adposition,
            ),
            WordToken(
                "la",
                LanguageCode.French,
                pos=PartOfSpeech.Determiner,
                features=Features(
                    Definite=Definite.Def,
                    Gender=Gender.Fem,
                    Number=Number.Sing,
                    PronType=PronType.Art,
                ),
            ),
            WordToken(
                "présence",
                LanguageCode.French,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Fem, Number=Number.Sing),
            ),
            WordToken("de", LanguageCode.French, pos=PartOfSpeech.Adposition),
            WordToken("Simandou", LanguageCode.French, pos=PartOfSpeech.ProperNoun),
            PunctuationToken(",", sticks_left=True),
            WordToken("plus", LanguageCode.French, pos=PartOfSpeech.Adverb),
            WordToken(
                "grand",
                LanguageCode.French,
                pos=PartOfSpeech.Adjective,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            WordToken(
                "gisement",
                LanguageCode.French,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            WordToken("de", LanguageCode.French, pos=PartOfSpeech.Adposition),
            WordToken(
                "fer",
                LanguageCode.French,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            WordToken("non", LanguageCode.French, pos=PartOfSpeech.Adverb),
            WordToken(
                "exploité",
                LanguageCode.French,
                lemma="exploiter",
                pos=PartOfSpeech.Verb,
                features=Features(
                    Gender=Gender.Fem,
                    Number=Number.Sing,
                    Tense=Tense.Past,
                    VerbForm=VerbForm.Part,
                ),
            ),
            WordToken(
                "au",
                LanguageCode.French,
                pos=PartOfSpeech.Determiner,
                features=Features(
                    Definite=Definite.Def,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    PronType=PronType.Art,
                ),
            ),
            WordToken(
                "monde",
                LanguageCode.French,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            PunctuationToken(",", sticks_left=True),
            WordToken("sur", LanguageCode.French, pos=PartOfSpeech.Adposition),
            WordToken(
                "son",
                LanguageCode.French,
                pos=PartOfSpeech.Determiner,
                features=Features(Number=Number.Sing, Poss=Poss.Yes),
            ),
            WordToken(
                "territoire",
                LanguageCode.French,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            PunctuationToken(",", sticks_left=True),
            WordToken(
                "le",
                LanguageCode.French,
                pos=PartOfSpeech.Determiner,
                features=Features(
                    Definite=Definite.Def,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    PronType=PronType.Art,
                ),
            ),
            WordToken(
                "pays",
                LanguageCode.French,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            Ellision(
                "d’Afrique",
                [
                    WordToken("de", LanguageCode.French, pos=PartOfSpeech.Adposition),
                    WordToken(
                        "Afrique",
                        LanguageCode.French,
                        pos=PartOfSpeech.ProperNoun,
                        features=Features(Gender=Gender.Fem, Number=Number.Sing),
                    ),
                ],
                LanguageCode.French,
            ),
            WordToken("de", LanguageCode.French, pos=PartOfSpeech.Adposition),
            Ellision(
                "l’Ouest",
                [
                    WordToken(
                        "l’",
                        LanguageCode.French,
                        pos=PartOfSpeech.Determiner,
                        features=Features(
                            Definite=Definite.Def,
                            Number=Number.Sing,
                            PronType=PronType.Art,
                        ),
                    ),
                    WordToken(
                        "Ouest",
                        LanguageCode.French,
                        lemma="Ouest",
                        pos=PartOfSpeech.ProperNoun,
                        features=Features(Number=Number.Sing),
                    ),
                ],
                LanguageCode.French,
            ),
            Ellision(
                "n’en",
                [
                    WordToken(
                        "n’",
                        LanguageCode.French,
                        pos=PartOfSpeech.Adverb,
                        features=Features(Polarity=Polarity.Neg),
                    ),
                    WordToken(
                        "en",
                        LanguageCode.French,
                        pos=PartOfSpeech.Pronoun,
                        features=Features(Person=Person.Third),
                    ),
                ],
                LanguageCode.French,
            ),
            WordToken(
                "a",
                LanguageCode.French,
                lemma="avoir",
                pos=PartOfSpeech.Auxiliary,
                features=Features(
                    Mood=Mood.Ind,
                    Number=Number.Sing,
                    Person=Person.Third,
                    Tense=Tense.Pres,
                    VerbForm=VerbForm.Fin,
                ),
            ),
            WordToken(
                "pas",
                LanguageCode.French,
                pos=PartOfSpeech.Adverb,
                features=Features(Polarity=Polarity.Neg),
            ),
            WordToken(
                "extrait",
                LanguageCode.French,
                lemma="extraire",
                pos=PartOfSpeech.Verb,
                features=Features(
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    Tense=Tense.Past,
                    VerbForm=VerbForm.Part,
                ),
            ),
            WordToken(
                "un",
                LanguageCode.French,
                pos=PartOfSpeech.Determiner,
                features=Features(
                    Definite=Definite.Ind,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    PronType=PronType.Art,
                ),
            ),
            WordToken(
                "seul",
                LanguageCode.French,
                pos=PartOfSpeech.Adjective,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            WordToken(
                "gramme",
                LanguageCode.French,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            WordToken("en", LanguageCode.French, pos=PartOfSpeech.Adposition),
            WordToken("vingt", language=LanguageCode.French, pos=PartOfSpeech.Number),
            WordToken(
                "ans",
                LanguageCode.French,
                lemma="an",
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Plur),
            ),
            PunctuationToken(".", sticks_left=True),
        ]

        self.assertListEqual(tokens, expected_tokens)

    def test_parses_sentence_3(self):
        tokens = self.parser.process(
            "En Guinée, le fer est pavé de mauvaises intentions"
        )

        expected_tokens = [
            WordToken(
                "En", LanguageCode.French, lemma="en", pos=PartOfSpeech.Adposition,
            ),
            WordToken(
                "Guinée",
                LanguageCode.French,
                pos=PartOfSpeech.ProperNoun,
                features=Features(Gender=Gender.Fem, Number=Number.Sing),
            ),
            PunctuationToken(",", sticks_left=True),
            WordToken(
                "le",
                LanguageCode.French,
                pos=PartOfSpeech.Determiner,
                features=Features(
                    Definite=Definite.Def,
                    Gender=Gender.Masc,
                    Number=Number.Sing,
                    PronType=PronType.Art,
                ),
            ),
            WordToken(
                "fer",
                LanguageCode.French,
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Masc, Number=Number.Sing),
            ),
            WordToken(
                "est",
                LanguageCode.French,
                lemma="être",
                pos=PartOfSpeech.Auxiliary,
                features=Features(
                    Mood=Mood.Ind,
                    Number=Number.Sing,
                    Person=Person.Third,
                    Tense=Tense.Pres,
                    VerbForm=VerbForm.Fin,
                ),
            ),
            WordToken(
                "pavé",
                LanguageCode.French,
                lemma="paver",
                pos=PartOfSpeech.Verb,
                features=Features(
                    Number=Number.Sing, Tense=Tense.Past, VerbForm=VerbForm.Part,
                ),
            ),
            WordToken("de", LanguageCode.French, pos=PartOfSpeech.Adposition),
            WordToken(
                "mauvaises",
                LanguageCode.French,
                lemma="mauvais",
                pos=PartOfSpeech.Adjective,
                features=Features(Gender=Gender.Fem, Number=Number.Plur),
            ),
            WordToken(
                "intentions",
                LanguageCode.French,
                lemma="intention",
                pos=PartOfSpeech.Noun,
                features=Features(Gender=Gender.Fem, Number=Number.Plur),
            ),
        ]

        self.assertListEqual(tokens, expected_tokens)


class TestFrenchNumbers(unittest.TestCase):
    def test_converts_numbers(self):
        self.assertListEqual(
            FrenchNumberConverter.verbalize_number(1),
            [WordToken("un", LanguageCode.French, pos=PartOfSpeech.Number)],
        ),
        self.assertEqual(
            FrenchNumberConverter.verbalize_number(12),
            [WordToken("douze", LanguageCode.French, pos=PartOfSpeech.Number)],
        )
        self.assertEqual(
            FrenchNumberConverter.verbalize_number(202),
            [
                WordToken("deux", LanguageCode.French, pos=PartOfSpeech.Number),
                PunctuationToken("-", sticks_left=True, sticks_right=True),
                WordToken("cent", LanguageCode.French, pos=PartOfSpeech.Number),
                PunctuationToken("-", sticks_left=True, sticks_right=True),
                WordToken("deux", LanguageCode.French, pos=PartOfSpeech.Number),
            ],
        )
        self.assertEqual(
            FrenchNumberConverter.verbalize_number(95),
            [
                WordToken("quatre", LanguageCode.French, pos=PartOfSpeech.Number),
                PunctuationToken("-", sticks_left=True, sticks_right=True),
                WordToken("vingt", LanguageCode.French, pos=PartOfSpeech.Number),
                PunctuationToken("-", sticks_left=True, sticks_right=True),
                WordToken("quinze", LanguageCode.French, pos=PartOfSpeech.Number),
            ],
        )


if __name__ == "__main__":
    unittest.main()
