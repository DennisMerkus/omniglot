import unittest

from documental.token import NumberToken, PunctuationToken, WordToken
from documental.token.word import RubyCharacter, RubyToken
from omniglot.jpn.parse import JapaneseParser
from omnilingual import LanguageCode, PartOfSpeech


class TestJapanese(unittest.TestCase):
    def setUp(self):
        self.parser = JapaneseParser()

    def test_parses_sentences(self):
        tokens = self.parser.process("2020年4月11日")

        expected_tokens = [
            NumberToken(
                "2020",
                2020,
                words=[
                    RubyToken(
                        characters=[RubyCharacter(base="二", text="に")],
                        language=LanguageCode.Japanese,
                        lemma="二",
                        pos=PartOfSpeech.Number,
                    ),
                    RubyToken(
                        characters=[RubyCharacter(base="千", text="せん")],
                        language=LanguageCode.Japanese,
                        lemma="千",
                        pos=PartOfSpeech.Number,
                    ),
                    RubyToken(
                        characters=[RubyCharacter(base="二", text="に")],
                        language=LanguageCode.Japanese,
                        lemma="二",
                        pos=PartOfSpeech.Number,
                    ),
                    RubyToken(
                        characters=[RubyCharacter(base="十", text="じゅう")],
                        language=LanguageCode.Japanese,
                        lemma="十",
                        pos=PartOfSpeech.Number,
                    ),
                ],
            ),
            WordToken("年", LanguageCode.Japanese, pos=PartOfSpeech.Noun),
            NumberToken(
                "4",
                4,
                words=[
                    RubyToken(
                        characters=[RubyCharacter(base="四", text="し")],
                        language=LanguageCode.Japanese,
                        lemma="四",
                        pos=PartOfSpeech.Number,
                    )
                ],
            ),
            WordToken("月", LanguageCode.Japanese, pos=PartOfSpeech.Noun),
            NumberToken(
                "11",
                11,
                words=[
                    RubyToken(
                        characters=[RubyCharacter(base="十", text="じゅう")],
                        language=LanguageCode.Japanese,
                        lemma="十",
                        pos=PartOfSpeech.Number,
                    ),
                    RubyToken(
                        characters=[RubyCharacter(base="一", text="いち")],
                        language=LanguageCode.Japanese,
                        lemma="一",
                        pos=PartOfSpeech.Number,
                    ),
                ],
            ),
            WordToken("日", LanguageCode.Japanese, pos=PartOfSpeech.Noun),
        ]

        self.assertListEqual(tokens, expected_tokens)

    def test_combine_capitalized_words(self):
        tokens = self.parser.process("そして新たにThe New York Timesが報じた、")

        expected_tokens = [
            WordToken(
                "そして", LanguageCode.Japanese, pos=PartOfSpeech.CoordinatingConjunction,
            ),
            WordToken("新た", LanguageCode.Japanese, pos=PartOfSpeech.Adjective),
            WordToken("に", LanguageCode.Japanese, pos=PartOfSpeech.Particle),
            WordToken("The", LanguageCode.Japanese, "THE", pos=PartOfSpeech.Noun),
            WordToken(
                "New York Times", LanguageCode.Japanese, pos=PartOfSpeech.ProperNoun,
            ),
            WordToken("が", LanguageCode.Japanese, pos=PartOfSpeech.Particle),
            WordToken("報じた", LanguageCode.Japanese, "報ずる", pos=PartOfSpeech.Verb),
            PunctuationToken("、"),
        ]

        self.assertListEqual(tokens, expected_tokens)

    def test_combines_morphology_into_single_phrase(self):
        sentences = {
            "キットはウイルスに汚染されていた": [
                WordToken("キット", LanguageCode.Japanese, pos=PartOfSpeech.Noun),
                WordToken("は", LanguageCode.Japanese, pos=PartOfSpeech.Particle),
                WordToken("ウイルス", LanguageCode.Japanese, pos=PartOfSpeech.Noun),
                WordToken("に", LanguageCode.Japanese, pos=PartOfSpeech.Particle),
                WordToken("汚染", LanguageCode.Japanese, pos=PartOfSpeech.Verb),
                WordToken("されていた", LanguageCode.Japanese, "する", pos=PartOfSpeech.Verb),
            ],
            "ことが明らかになりました。": [
                WordToken("こと", LanguageCode.Japanese, pos=PartOfSpeech.Noun),
                WordToken("が", LanguageCode.Japanese, pos=PartOfSpeech.Particle),
                WordToken("明らか", LanguageCode.Japanese, pos=PartOfSpeech.Adjective),
                WordToken("に", LanguageCode.Japanese, pos=PartOfSpeech.Particle),
                WordToken("なりました", LanguageCode.Japanese, "なる", pos=PartOfSpeech.Verb),
                PunctuationToken("。"),
            ],
        }

        for sentence, expected_tokens in sentences.items():
            tokens = self.parser.process(sentence)

            self.assertListEqual(tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
