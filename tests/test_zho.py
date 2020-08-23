import unittest

from documental.token import PunctuationToken, WordToken

from omniglot.zho.parse import MandarinChineseParser
from omnilingual import LanguageCode, PartOfSpeech


class TestMandarinChinese(unittest.TestCase):
    def setUp(self):
        self.parser = MandarinChineseParser()

        self.maxDiff = None

    def test_parses_sentences(self):
        tokens = self.parser.process("「4 大超狂曬包守則」：原來名牌包老司機都在投資這幾款！")

        expected_tokens = [
            PunctuationToken("「"),
            WordToken("4", language=LanguageCode.Chinese, pos=PartOfSpeech.Number),
            WordToken("大", language=LanguageCode.Chinese, pos=PartOfSpeech.Adjective),
            WordToken("超", language=LanguageCode.Chinese),
            WordToken("狂", language=LanguageCode.Chinese),
            WordToken("曬", language=LanguageCode.Chinese),
            WordToken("包", language=LanguageCode.Chinese),
            WordToken("守則", language=LanguageCode.Chinese, pos=PartOfSpeech.Noun),
            PunctuationToken("」"),
            PunctuationToken("："),
            WordToken("原來", language=LanguageCode.Chinese, pos=PartOfSpeech.Adjective),
            WordToken("名牌", language=LanguageCode.Chinese, pos=PartOfSpeech.Noun),
            WordToken("包老", language=LanguageCode.Chinese),
            WordToken("司機", language=LanguageCode.Chinese, pos=PartOfSpeech.Noun),
            WordToken("都", language=LanguageCode.Chinese),
            WordToken("在", language=LanguageCode.Chinese),
            WordToken("投資", language=LanguageCode.Chinese, pos=PartOfSpeech.Verb),
            WordToken("這", language=LanguageCode.Chinese, pos=PartOfSpeech.Noun),
            WordToken("幾", language=LanguageCode.Chinese),
            WordToken("款", language=LanguageCode.Chinese),
            PunctuationToken("！"),
        ]

        self.assertListEqual(tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
