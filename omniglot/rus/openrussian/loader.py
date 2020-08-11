import os.path
from typing import List

from omniglot.dictionary import DictionaryLoader
from omniglot.lexeme import Lexeme

from .convert import convert_OpenRussian
from .preprocess import sanitize_tsv_file


class OpenRussianLoader(DictionaryLoader):
    def __init__(self, dictionary_path: str = "./cache/openrussian"):
        self.base_path = dictionary_path

        self.files: List[str] = [
            "adjectives.csv",
            "conjugations.csv",
            "declensions.csv",
            "nouns.csv",
            "sentences.csv",
            "translations.csv",
            "verbs.csv",
            "words_rels.csv",
            "words.csv",
        ]

    async def load(self) -> List[Lexeme]:
        await self.verify_files_are_present()

        for file_name in self.files:
            await sanitize_tsv_file(os.path.join(self.base_path, file_name))

        return await convert_OpenRussian(self.base_path)

    async def verify_files_are_present(self) -> None:
        for file_name in self.files:
            if not os.path.isfile(os.path.join(self.base_path, file_name)):
                raise FileNotFoundError("Missing %s file" % (file_name))
