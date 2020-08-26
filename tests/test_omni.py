import unittest

from omniglot.omni import OmnilingualProcessor

from omnilingual import LanguageCode


class TestOmni(unittest.TestCase):
    def setUp(self):
        self.omni = OmnilingualProcessor(None)

        self.maxDiff = None


if __name__ == "__main__":
    unittest.main()
