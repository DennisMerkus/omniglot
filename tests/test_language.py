import unittest

from omnilingual import Language, LanguageCode

from pycld2 import LANGUAGES as pycld2_languages


class TestLanguage(unittest.TestCase):
    def test_requires_valid_code(self):
        with self.assertRaises(ValueError):
            Language.where(tag="a")

    def test_russian_equivalents(self):
        iso_1 = "ru"
        iso_3 = "rus"

        self.assertEqual(Language.where(iso_1=iso_1), iso_1)
        self.assertEqual(Language.where(iso_3=iso_3), iso_3)
        self.assertEqual(Language.where(iso_1=iso_1), iso_3)
        self.assertEqual(Language.where(iso_3=iso_3), iso_1)

        self.assertEqual(Language.where(iso_1=iso_1), Language.where(iso_3=iso_3))

    def test_supports_all_pycld2_languages(self):
        for name, code in pycld2_languages:
            if code.startswith("xx-") or code in [
                "xxx",
                "zzb",
                "zze",
                "zzh",
                "zzp",
            ]:
                continue

            self.assertNotEqual(
                Language.where(tag=code).code, LanguageCode.Undetermined
            )

    def test_should_convert_non_iso_639_3_codes(self):
        self.assertEqual(Language.where(iso_2="fre").code, LanguageCode.French)
        self.assertEqual(Language.where(iso_2="ger").code, LanguageCode.German)

        self.assertEqual(Language.where(tag="fre").code, LanguageCode.French)
        self.assertEqual(Language.where(tag="ger").code, LanguageCode.German)


if __name__ == "__main__":
    unittest.main()
