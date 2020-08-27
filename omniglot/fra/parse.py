from typing import List

import spacy
from spacy.pipeline import Sentencizer

from documental.token import Ellision, Token, WordToken
from omniglot.mul.numbers import combine_numbers
from omniglot.mul.punctuation import convert_punctuation_tokens
from omniglot.parser import NaturalLanguageProcessor
from omnilingual import LanguageCode, PartOfSpeech
from omnilingual.features import Features, Tense, VerbForm, parse_features

from .numbers import FrenchNumberConverter


class FrenchParser(NaturalLanguageProcessor):
    def __init__(self):
        super().__init__()

        self.nlp = spacy.load("fr_core_news_md")

        self.nlp.add_pipe(Sentencizer())

    def process(self, text: str) -> List[Token]:
        tokens: List[Token] = self.tokenize(text)

        tokens = combine_numbers(tokens)
        tokens = convert_punctuation_tokens(tokens)

        return tokens

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.French]

    def tokenize(self, text: str) -> List[Token]:
        tokens: List[Token] = []

        for token in self.nlp(text):
            print(token.text, token.lemma_, token.pos_, token.tag_)

            if token.pos_ == "SPACE":
                continue

            lemma: str

            if token.text.lower() in ["elle", "lui", "je", "la", "le"]:
                lemma = token.text.lower()
            else:
                lemma = token.lemma_

            pos = PartOfSpeech(token.pos_)

            if pos is PartOfSpeech.Number:
                tokens.append(FrenchNumberConverter.parse(token.text))
            else:
                tokens.append(
                    WordToken(
                        language=LanguageCode.French,
                        text=token.text,
                        lemma=lemma,
                        pos=pos,
                        features=parse_features(token.tag_),
                    )
                )

        tokens = self.fix_ellisions(tokens)
        tokens = self.fix_auxiliary_verb_phrases(tokens)

        return tokens

    def fix_ellisions(self, tokens: List[Token]) -> List[Token]:
        ellided_tokens: List[Token] = []

        index = 0
        while index < len(tokens):
            token = tokens[index]

            if (
                isinstance(token, WordToken)
                and index + 1 < len(tokens)
                and isinstance(tokens[index + 1], WordToken)
            ):
                next_token = tokens[index + 1]

                if not isinstance(next_token, WordToken):
                    ellided_tokens.append(token)

                    index += 1
                elif token.text == "d’":
                    token.text = "de"
                    token.lemma = "de"

                    ellided_tokens.append(
                        Ellision(
                            "d’" + next_token.text,
                            [token, next_token],
                            LanguageCode.French,
                        )
                    )

                    index += 2
                elif token.text == "l’":
                    ellided_tokens.append(
                        Ellision(
                            "l’" + next_token.text,
                            [token, next_token],
                            LanguageCode.French,
                        )
                    )

                    index += 2
                elif token.text == "n’":
                    ellided_tokens.append(
                        Ellision(
                            "n’" + next_token.text,
                            [token, next_token],
                            LanguageCode.French,
                        )
                    )

                    index += 2
                else:
                    ellided_tokens.append(token)

                    index += 1
            else:
                ellided_tokens.append(token)

                index += 1

        return ellided_tokens

    @staticmethod
    def is_passé_composé(word: str) -> bool:
        # TODO: This probably doesn't work for all passé composé forms. Check this.
        return word[-1] == "é"

    def fix_auxiliary_verb_phrases(self, tokens: List[Token]) -> List[Token]:
        fixed_tokens: List[Token] = []

        index = 0
        while index < len(tokens) - 1:
            current_token: Token = tokens[index]
            next_token: Token = tokens[index + 1]

            # Sometimes words get tagged as nouns because their form is similar to a verb form
            if (
                isinstance(current_token, WordToken)
                and isinstance(next_token, WordToken)
                and current_token.pos is PartOfSpeech.Auxiliary
                and next_token.pos is PartOfSpeech.Noun
                and self.is_passé_composé(next_token.text)
            ):
                fixed_tokens.append(current_token)
                fixed_tokens.append(
                    WordToken(
                        text=next_token.text,
                        language=LanguageCode.French,
                        lemma=next_token.text[:-1]
                        + "er",  # TODO: This also might not be correct for all verbs. Need verb conjugator.
                        pos=PartOfSpeech.Verb,
                        features=Features(
                            Gender=current_token.features.Gender,
                            Number=current_token.features.Number,
                            Tense=Tense.Past,
                            VerbForm=VerbForm.Part,
                        ),
                    )
                )

                index += 2
            else:
                fixed_tokens.append(current_token)
                index += 1

        if len(tokens) > 0:
            fixed_tokens.append(tokens[-1])

        return fixed_tokens
