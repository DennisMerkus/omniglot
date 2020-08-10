import unittest

from omnilingual.features import (
    Definite,
    Features,
    Gender,
    Number,
    PronType,
    parse_features,
)


class TestFeatures(unittest.TestCase):
    def test_parses_single_feature(self):
        tag = "NOUN__Gender=Fem"

        features = parse_features(tag)

        self.assertEqual(features, Features(Gender=Gender.Fem))

    def test_parses_multiple_features(self):
        tag = "DET__Definite=Def|Gender=Masc|Number=Sing|PronType=Art"

        features = parse_features(tag)

        self.assertEqual(
            features,
            Features(
                Definite=Definite.Def,
                Gender=Gender.Masc,
                Number=Number.Sing,
                PronType=PronType.Art,
            ),
        )

    def test_parses_pos_only(self):
        tag = "ADP"

        features = parse_features(tag)

        self.assertEqual(features, Features())

    def test_parses_empty_features(self):
        tag = ""

        features = parse_features(tag)

        self.assertEqual(features, Features())


if __name__ == "__main__":
    unittest.main()
