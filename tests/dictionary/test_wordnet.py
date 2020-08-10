import io
import unittest
from typing import List

from entwine.dictionary.wordnet.extract import (
    extract_data,
    extract_pointers,
    extract_frames,
)
from entwine.dictionary.wordnet.multi import parse_multilingual_wordnet
from entwine.dictionary.wordnet.wndb import (
    WordnetPOS,
    WordnetData,
    WordnetIdentifier,
    WordnetPointer,
    WordnetFrame,
    MultilingualWordnetLemma,
)
from entwine.dictionary.wordnet.symbols import WordnetPointerSymbol


class TestWordNet(unittest.TestCase):
    def test_extract_data_pointers(self):
        pointer_string = "@ 11574626 n 0000 #m 11684541 n 0000"

        expected_pointers: List[WordnetPointer] = [
            WordnetPointer(
                pointer_symbol=WordnetPointerSymbol.Hypernym,
                synset_offset="11574626",
                pos=WordnetPOS.Noun,
                source=0,
                target=0,
            ),
            WordnetPointer(
                pointer_symbol=WordnetPointerSymbol.MemberHolonym,
                synset_offset="11684541",
                pos=WordnetPOS.Noun,
                source=0,
                target=0,
            ),
        ]

        self.assertListEqual(
            extract_pointers(pointer_string), expected_pointers
        )

    def test_extract_data(self):
        data_string = "11563715 20 n 02 Jungermanniaceae 0 family_Jungermanniaceae 0 002 @ 11558116 n 0000 #m 11563371 n 0000 | comprising the leafy members of the order Jungermanniales  "

        expected_data = WordnetData(
            synset_offset="11563715",
            lex_filenum="20",
            ss_type=WordnetPOS.Noun,
            w_cnt=2,
            words=[
                WordnetIdentifier(word="Jungermanniaceae", lex_id=0),
                WordnetIdentifier(word="family_Jungermanniaceae", lex_id=0),
            ],
            p_cnt=2,
            pointers=[
                WordnetPointer(
                    pointer_symbol=WordnetPointerSymbol.Hypernym,
                    synset_offset="11558116",
                    pos=WordnetPOS.Noun,
                    source=0,
                    target=0,
                ),
                WordnetPointer(
                    pointer_symbol=WordnetPointerSymbol.MemberHolonym,
                    synset_offset="11563371",
                    pos=WordnetPOS.Noun,
                    source=0,
                    target=0,
                ),
            ],
            gloss="comprising the leafy members of the order Jungermanniales",
        )

        self.assertEqual(extract_data(data_string), expected_data)

    def test_extract_frames(self):
        frames_string = "+ 02 00 + 08 00"

        expected_frames = [
            WordnetFrame(f_num=2, w_num=0),
            WordnetFrame(f_num=8, w_num=0,),
        ]

        self.assertListEqual(extract_frames(frames_string), expected_frames)


class TestMultilingualWordnet(unittest.TestCase):
    def test_multilingual_wordnet(self):
        file = "00018158-v	ind:lemma	membubung\n00018189-r	ind:lemma	bahkan\n"

        data = parse_multilingual_wordnet(io.StringIO(file))

        self.assertListEqual(
            data.lemmas,
            [
                MultilingualWordnetLemma(
                    language="ind",
                    offset="00018158",
                    pos=WordnetPOS.Verb,
                    lemma="membubung",
                ),
                MultilingualWordnetLemma(
                    language="ind",
                    offset="00018189",
                    pos=WordnetPOS.Adverb,
                    lemma="bahkan",
                ),
            ],
        )


if __name__ == "__main__":
    unittest.main()
