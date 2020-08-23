import unittest

from omniglot.omni import OmnilingualProcessor

from omnilingual import LanguageCode


class TestOmni(unittest.TestCase):
    def setUp(self):
        self.omni = OmnilingualProcessor()

        self.maxDiff = None

    def test_parses_sentences(self):
        tokens = self.parser.process(
            "المركز الوطني للسكري يوضح آلية توصيل الدواء للمنازل ويؤكد استمراريته - صحيفة الرأي"
        )

        expected_tokens = [
            WordToken("المركز", LanguageCode.Arabic),
            WordToken("الوطني", LanguageCode.Arabic),
            WordToken("للسكري", LanguageCode.Arabic),
            WordToken("يوضح", LanguageCode.Arabic),
            WordToken("آلية", LanguageCode.Arabic),
            WordToken("توصيل", LanguageCode.Arabic),
            WordToken("الدواء", LanguageCode.Arabic),
            WordToken("للمنازل", LanguageCode.Arabic),
            WordToken("ويؤكد", LanguageCode.Arabic),
            WordToken("استمراريته", LanguageCode.Arabic),
            PunctuationToken("-"),
            WordToken("صحيفة", LanguageCode.Arabic),
            WordToken("الرأي", LanguageCode.Arabic),
        ]

        self.assertListEqual(tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
