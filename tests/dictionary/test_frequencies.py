import unittest

from entwine.dictionary.frequencies import load_row
from omnilingual import Language


class TestFrequencies(unittest.TestCase):
    def test_loads_rows(self):
        rows = [
            ["     1", "34943515", "の"],
            ["   234", "236173", "度"],
            ["2610776", "1", "⺌"],
        ]

        for row in rows:
            load_row(row, Language("jpn"))


if __name__ == "__main__":
    unittest.main()
