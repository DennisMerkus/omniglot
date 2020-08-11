import logging
import os
from typing import List

import aiofiles
from omniglot.dictionary import DictionaryLoader
from omniglot.lexeme import Lexeme

from .convert import convert_CC_CEDICT_to_JSON, create_CC_CEDICT_database_entries

CACHE_DIR = os.getenv("CACHE_DIR", "./cache")


class CcCedictDictionaryLoader(DictionaryLoader):
    async def load(self) -> List[Lexeme]:
        dictionary_path = os.path.join(CACHE_DIR, "CC-CEDICT.u8")

        logging.info("Loading dictionary from %s" % (dictionary_path))

        async with aiofiles.open(dictionary_path, "r") as f:
            data = await f.read()

        dictionary_data = convert_CC_CEDICT_to_JSON(data)

        return create_CC_CEDICT_database_entries(dictionary_data)


CcCedictLoader = CcCedictDictionaryLoader()
