import unittest

from documental.token import NumberToken, PunctuationToken, WordToken

from omniglot.zho.parse import MandarinParser


class TestMandarin(unittest.TestCase):
    def setUp(self):
        self.parser = MandarinParser()

    def test_parses_sentences(self):
        tokens = self.parser.process("zho", "「4 大超狂曬包守則」：原來名牌包老司機都在投資這幾款！")

        expected_tokens = [
            PunctuationToken("「"),
            NumberToken("4"),
            WordToken("大超狂"),
            WordToken("曬"),
            WordToken("包守則"),
            PunctuationToken("」"),
            PunctuationToken("："),
            WordToken("原來"),
            WordToken("名牌"),
            WordToken("包老司"),
            WordToken("機都"),
            WordToken("在"),
            WordToken("投資"),
            WordToken("這幾款"),
            PunctuationToken("！"),
        ]

        self.assertListEqual(tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
