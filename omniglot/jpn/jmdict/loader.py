import logging
import os
from typing import List

import aiofiles
from omniglot.dictionary import DictionaryLoader
from omniglot.lexeme import Lexeme

from .convert import create_JMDict_database_entries
from .extract import convert_to_JSON

CACHE_DIR = os.getenv("CACHE_DIR", "./cache")


class JMDictDictionaryLoader(DictionaryLoader):
    async def load(self) -> List[Lexeme]:
        dictionary_path = os.path.join(CACHE_DIR, "JMDict")

        logging.info("Loading dictionary from %s" % (dictionary_path))

        async with aiofiles.open(dictionary_path, "r") as f:
            data = await f.read()

        dictionary_data = await convert_to_JSON(data)

        return await create_JMDict_database_entries(dictionary_data)


JMDictLoader = JMDictDictionaryLoader()
