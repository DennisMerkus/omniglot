import re
from typing import List

from .wndb import (
    WordnetData,
    WordnetFrame,
    WordnetIdentifier,
    WordnetPointer,
    WordnetPOS,
)

WORDNET_DATA_WORD_REGEX = r"((?P<word>[\S]+)\s(?P<lex_id>[0-9A-Fa-f]))+"


def extract_words(string: str) -> List[WordnetIdentifier]:
    words: List[WordnetIdentifier] = []

    for word in re.findall(WORDNET_DATA_WORD_REGEX, string):
        words.append(WordnetIdentifier(word=word[1], lex_id=int(word[2], 16)))

    return words


WORDNET_POINTERS_REGEX = r"((?P<pointer_symbol>\S+)\s(?P<synset_offset>\d{8})\s(?P<pos>[nasrv])\s(?P<source_target>[0-9A-Fa-f]{4}))+"


def extract_pointers(string: str) -> List[WordnetPointer]:
    pointers: List[WordnetPointer] = []

    for match in re.findall(WORDNET_POINTERS_REGEX, string):
        source, target = (
            match[4][:2],
            match[4][2:],
        )
        pointers.append(
            WordnetPointer(
                pointer_symbol=match[1],
                synset_offset=match[2],
                pos=WordnetPOS(match[3]),
                source=int(source, 16),
                target=int(target, 16),
            )
        )

    return pointers


WORDNET_FRAME_REGEX = r"\+\s(?P<f_num>\d{2})\s(?P<w_num>[0-9A-Fa-f]{2})"


def extract_frames(string: str) -> List[WordnetFrame]:
    frames: List[WordnetFrame] = []

    for match in re.findall(WORDNET_FRAME_REGEX, string):
        frames.append(WordnetFrame(f_num=int(match[0]), w_num=int(match[1])))

    return frames


WORDNET_DATA_REGEX = r"^(?P<synset_offset>\d{8})\s(?P<lex_filenum>\d{2})\s(?P<ss_type>[nasrv])\s(?P<w_cnt>[0-9A-Fa-f]{2})\s(?P<words>([\S]+\s[0-9A-Fa-f]\s)+)(000|(?P<p_cnt>\d{3})\s(?P<pointers>([\S]+\s\d{8}\s[nasrv]\s[0-9A-Fa-f]{4}\s?)+))(\s(?P<f_cnt>\d{2})(?P<frames>(\s\+\s(?P<f_num>\d{2})\s(?P<w_num>[0-9A-Fa-f]{2}))+))?\s\|\s(?P<gloss>.*?)\s*$"


def extract_data(data_string: str) -> WordnetData:
    match = re.match(WORDNET_DATA_REGEX, data_string)

    if match is None:
        raise ValueError("Unexpected WordNet string\n%s" % (data_string))

    words_string = match.group("words")

    if words_string is None:
        raise ValueError(
            "Unexpected WordNet words\n%s\n%s" % (words_string, data_string)
        )

    words = extract_words(words_string)

    if match.group("p_cnt") is not None:
        p_cnt = int(match.group("p_cnt"))
    else:
        p_cnt = 0

    if p_cnt == 0:
        pointers = []
    else:
        pointers = extract_pointers(match.group("pointers"))

    return WordnetData(
        synset_offset=match.group("synset_offset"),
        lex_filenum=match.group("lex_filenum"),
        ss_type=WordnetPOS(match.group("ss_type")),
        w_cnt=int(match.group("w_cnt"), 16),
        words=words,
        p_cnt=p_cnt,
        pointers=pointers,
        gloss=match.group("gloss"),
    )
