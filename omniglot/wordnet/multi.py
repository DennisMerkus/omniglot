import io
import re
from typing import List

from .wndb import (
    MultiLingualWordnetData,
    MultilingualWordnetDefinition,
    MultilingualWordnetExample,
    MultilingualWordnetLemma,
    WordnetPOS,
)

LEMMA_REGEX = r"^(?P<offset>\d{8})-(?P<pos>[nvars])\s(?P<language>\w{3}):(?P<type>lemma|def|exe)\s((?P<sid>\d{1})\s)?(?P<content>.+)\s*$"


def parse_multilingual_wordnet(file: io.StringIO) -> MultiLingualWordnetData:
    definitions: List[MultilingualWordnetDefinition] = []
    examples: List[MultilingualWordnetExample] = []
    lemmas: List[MultilingualWordnetLemma] = []

    for line in file:
        if line.startswith("#"):
            continue

        match = re.match(LEMMA_REGEX, line)

        if match is None:
            raise ValueError("Unexpected line format\n%s" % (line))
        else:
            offset = match.group("offset")
            pos: WordnetPOS = WordnetPOS(match.group("pos"))

            language = match.group("language")

            entry_type = match.group("type")

            content = match.group("content")

            if entry_type == "lemma":
                lemmas.append(
                    MultilingualWordnetLemma(
                        offset=offset,
                        pos=pos,
                        language=language,
                        lemma=content,
                    )
                )
            elif entry_type == "def":
                definitions.append(
                    MultilingualWordnetDefinition(
                        offset=offset,
                        pos=pos,
                        language=language,
                        definition=content,
                    )
                )
            elif entry_type == "exe":
                examples.append(
                    MultilingualWordnetExample(
                        offset=offset,
                        pos=pos,
                        language=language,
                        example=content,
                    )
                )

    return MultiLingualWordnetData(
        definitions=definitions, examples=examples, lemmas=lemmas,
    )
