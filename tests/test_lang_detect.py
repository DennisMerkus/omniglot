import unittest

from omniglot.omni import OmnilingualProcessor


class TestLanguageDetection(unittest.TestCase):
    def setUp(self):
        self.Omni = OmnilingualProcessor(None)

    def test_detect_russian(self):
        sentences = [
            "Райан Рейнольдс и Хью Джекман годами троллили друг друга.",
            "Карантин ввели и в медучреждениях республики, не связанных с РКБ. На 21 апреля в Башкирии выявлен 371 случай заболевания: 20 человек выздоровели, 14 умерли.",
            "«Мы все боимся — и руководство, и врачи» Больницы в России закрываются на карантин из-за коронавируса. «Медуза» выяснила, как принимаются такие решения и что происходит потом",
        ]

        for sentence in sentences:
            language = self.Omni.guess_language(sentence)
            self.assertEqual(language, "rus")


if __name__ == "__main__":
    unittest.main()
