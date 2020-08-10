import logging
import string
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

import pycld2
from omnilingual import Language, LanguageCode

from .ara.parse import ArabicParser
from .deu.parse import GermanParser
from .document import Document, ParentDocument, Text, TokenizedDocument
from .eng.parse import EnglishParser
from .fra.parse import FrenchParser
from .jpn.parse import JapaneseParser
from .lexeme import Lexeme
from .lookup import LemmaNotFoundError, LexemeLookup
from .parser import Annotator
from .por.parse import PortugueseParser
from .rus.parse import RussianParser
from .tokens import PunctuationToken, SpaceToken, WordToken
from .zho.parse import MandarinParser


class NaturalLanguageProcessor(object):
    async def process(self, document: Document) -> Document:
        raise NotImplementedError()


class OmnilingualProcessor(NaturalLanguageProcessor):
    def __init__(self, lexeme_lookup: LexemeLookup):
        self.parsers: Dict[LanguageCode, Annotator] = {
            LanguageCode.Arabic: ArabicParser(),
            LanguageCode.English: EnglishParser(),
            LanguageCode.French: FrenchParser(),
            LanguageCode.German: GermanParser(),
            LanguageCode.Japanese: JapaneseParser(),
            LanguageCode.Portuguese: PortugueseParser(),
            LanguageCode.Russian: RussianParser(),
            LanguageCode.Chinese: MandarinParser(),
        }

        self.lexeme_lookup = lexeme_lookup

    async def process(self, document: Document) -> Document:
        document_languages, uncertain_guesses = self.detect_languages(document)

        for node in document:
            if node.id in document_languages:
                node.language = document_languages[node.id]

        tokenized = self.tokenize(document)

        await self.lookup_senses(self.lexeme_lookup, tokenized)

        self.add_spaces(tokenized)

        return tokenized

    def tokenize(self, document: Document) -> Document:
        if isinstance(document, ParentDocument):
            document.children = [self.tokenize(child) for child in document.children]

            return document
        elif isinstance(document, Text):
            logging.debug("Tokenizing Document %s" % (document.text))

            tokenized = TokenizedDocument(document.text)

            if document.language is LanguageCode.Undetermined:
                logging.warning("[Omni] Undetermined languages. Skipping tokenization.")

                return document
            elif document.language in self.parsers.keys():
                return self.parsers[document.language].process(document)
            else:
                logging.warning(
                    "[Omni] Unrecognized language %s\n%s"
                    % (document.language, document.text)
                )

                return document

            return tokenized
        else:
            return document

    async def lookup_senses(self, lookup: LexemeLookup, document: Document) -> None:
        for element in document:
            if not isinstance(element, TokenizedDocument):
                continue

            for token in element.tokens:
                if not isinstance(token, WordToken):
                    continue

                try:
                    dictionary_entries: List[Lexeme] = await lookup.lexemes_with_lemma(
                        token.lemma, LanguageCode(element.language), token.pos
                    )

                    for entry in dictionary_entries:
                        entry_id = str(entry.id)

                        token.lexemeIds.append(entry_id)
                        element.lexemes[entry_id] = entry
                except LemmaNotFoundError:
                    logging.warning(
                        "Could not find a definition for %s:%s\t%s"
                        % (token.pos, token.lemma, token.text)
                    )

    def guess_language(
        self, text: str, hintLanguage: Optional[Language] = None
    ) -> Language:
        if hintLanguage is not None and hintLanguage.code != LanguageCode.Undetermined:
            is_reliable, _, details = pycld2.detect(
                text, hintLanguage=hintLanguage.original_or_alpha_2()
            )
        else:
            is_reliable, _, details = pycld2.detect(text, bestEffort=True)

        detected_languages: Dict[str, int] = defaultdict(int)

        highest_language = "un"
        highest_score = 0

        for name, code, percent, score in details:
            detected_languages[code] += percent

            if detected_languages[code] > highest_score:
                highest_score = detected_languages[code]
                highest_language = code

        return Language.where(tag=highest_language)

    def detect_languages(
        self, document: Document
    ) -> Tuple[Dict[str, str], Dict[str, str]]:
        # 1. Make a pass to detect languages for each TextDocument
        #    Mark unreliable and unknown texts
        # 2. Calculate the most likely languages
        document_languages: Dict[str, Language] = {}
        language_counts: Dict[str, int] = defaultdict(int)

        uncertain_guesses: Dict[str, str] = {}

        for node in document:
            if isinstance(node, Text):
                language = self.guess_language(node.text)
                document_languages[node.id] = language

                language_counts[language.specific] += 1

                if language.code is LanguageCode.Undetermined:
                    uncertain_guesses[node.id] = node.text

        # 3. Make a second pass, boosting certain languages, making extra checks
        language_rank: List[Language] = list(
            set(
                [
                    Language(x[0])
                    for x in sorted(
                        language_counts.items(), key=lambda x: x[1], reverse=True,
                    )
                ]
                + [Language.where(tag=LanguageCode.English.value)]
            )
        )

        new_uncertain_guesses = {}

        for id, text in uncertain_guesses.items():
            stripped_punctuation = text.translate(
                str.maketrans("", "", string.punctuation)
            )

            if len(stripped_punctuation.strip()) == 0:
                # Only punctuation or empty.
                # TODO: Update token as 'Punctuation' type
                pass

            nudged_language = self.guess_by_nudging_ranked_languages(
                text, language_rank
            )

            if nudged_language.code is not LanguageCode.Undetermined:
                document_languages[id] = nudged_language
            else:
                new_uncertain_guesses[id] = text

        language_guesses = {}

        for id, language in document_languages.items():
            language_guesses[id] = language.alpha_3

        return language_guesses, new_uncertain_guesses

    def guess_by_nudging_ranked_languages(
        self, text: str, language_rank: List[Language]
    ) -> Language:
        for language in language_rank:
            if language.code is LanguageCode.Undetermined:
                continue

            nudged_language = self.guess_language(text, hintLanguage=language)

            if nudged_language == language:
                return nudged_language

        return Language.where(tag=LanguageCode.Undetermined.value)

    @staticmethod
    def token_sticks_right(token):
        return isinstance(token, PunctuationToken) and token.sticks_right

    @staticmethod
    def token_sticks_left(token):
        return isinstance(token, PunctuationToken) and token.sticks_left

    def add_spaces(self, document: Document):
        for element in document:
            if not isinstance(element, TokenizedDocument):
                continue

            if element.language in [
                LanguageCode.Arabic,
                LanguageCode.Banu,
                LanguageCode.Dutch,
                LanguageCode.English,
                LanguageCode.German,
                LanguageCode.Hawaiian,
                LanguageCode.Hungarian,
                LanguageCode.Portuguese,
                LanguageCode.Russian,
                LanguageCode.Xian,
                LanguageCode.Undetermined,
            ]:
                isRequired = True
            elif element.language in [
                LanguageCode.Chinese,
                LanguageCode.Japanese,
            ]:
                isRequired = False
            else:
                logging.debug(
                    "[Doc] Guessing that spaces are required for %s"
                    % (element.language)
                )
                isRequired = True

            separated_tokens = []

            if len(element.tokens) > 0:
                separated_tokens.append(element.tokens[0])

            for index in range(1, len(element.tokens) - 1):
                next_index = index + 1
                last_token = separated_tokens[-1]

                if isinstance(last_token, SpaceToken) or self.token_sticks_right(
                    last_token
                ):
                    separated_tokens.append(element.tokens[index])
                else:
                    separated_tokens.append(SpaceToken(isRequired))
                    separated_tokens.append(element.tokens[index])

                if not self.token_sticks_left(element.tokens[next_index]):
                    separated_tokens.append(SpaceToken(isRequired))

            if len(element.tokens) > 1:
                separated_tokens.append(element.tokens[-1])

            element.tokens = separated_tokens
