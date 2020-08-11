import os
from typing import List

from omniglot.sense import Sense
from omnilingual import LanguageCode

from .extract import extract_data
from .wndb import WordnetData


def convert_Princeton_wordnet(files_location: str) -> List[Sense]:
    data_files = ["adj", "adv", "noun", "verb"]

    wordnet_data: List[WordnetData] = []

    for file_name in data_files:
        with open(os.path.join(files_location, "data.%s" % (file_name))) as file:
            for line in file:
                if line.startswith(" "):
                    continue

                wordnet_data.append(extract_data(line))

    senses: List[Sense] = []

    for synset in wordnet_data:
        senses.append(
            Sense(
                wordnet=synset.synset_offset,
                pos=synset.ss_type,
                lemmas={LanguageCode.English: [word.word for word in synset.words]},
                definitions={LanguageCode.English: [synset.gloss]},
                examples={},
            )
        )

    return senses
