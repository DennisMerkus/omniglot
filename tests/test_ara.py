import unittest

from documental import Text
from documental.token import PunctuationToken, WordToken
from omniglot.ara.parse import ArabicParser
from omnilingual import LanguageCode


class TestArabic(unittest.TestCase):
    def setUp(self):
        self.parser = ArabicParser()

    def test_parses_sentences(self):
        tokenized = self.parser.process(
            Text(
                "المركز الوطني للسكري يوضح آلية توصيل الدواء للمنازل ويؤكد استمراريته - صحيفة الرأي",
                language=LanguageCode.Arabic,
            )
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

        self.assertListEqual(tokenized.tokens, expected_tokens)


if __name__ == "__main__":
    unittest.main()
