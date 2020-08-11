import unittest

from documental import Text
from documental.token import NumberToken, PunctuationToken, WordToken
from omnilingual import LanguageCode, PartOfSpeech

from omniglot.jpn.parse import JapaneseParser


class TestJapanese(unittest.TestCase):
    def setUp(self):
        self.parser = JapaneseParser()

    def test_parses_sentences(self):
        tokenized = self.parser.process(Text("2020年4月11日", LanguageCode.Japanese))

        expected_tokens = [
            NumberToken("2020", 2020, "に　せん　に　じゅう"),
            WordToken("年", LanguageCode.Japanese, pos=PartOfSpeech.Noun),
            NumberToken("4"),
            WordToken("月", LanguageCode.Japanese, pos=PartOfSpeech.Noun),
            NumberToken("11"),
            WordToken("日", LanguageCode.Japanese, pos=PartOfSpeech.Noun),
        ]

        self.assertListEqual(tokenized.tokens, expected_tokens)

    def test_combine_capitalized_words(self):
        tokenized = self.parser.process(
            Text("そして新たにThe New York Timesが報じた、", LanguageCode.Japanese)
        )

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

        self.assertListEqual(tokenized.tokens, expected_tokens)

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
            tokenized = self.parser.process(Text(sentence, LanguageCode.Japanese))

            self.assertListEqual(tokenized.tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
