import logging
import re
from typing import List, Optional, Union

import spacy

from omnilingual import LanguageCode, PartOfSpeech
from .document import Text, TokenizedDocument
from omniglot.mul.numbers import combine_numbers
from omniglot.mul.punctuation import (
    punctuation_sticks_left,
    punctuation_sticks_right,
)

from ..morpheme import Morpheme
from ..parser import PipelineAnnotator
from ..tokens import (
    LetterToken,
    NumberToken,
    PunctuationToken,
    Token,
    WordToken,
)

# https://en.wikipedia.org/wiki/Japanese_grammar#Stem_forms


verb_forms = {
    "irrealis": {
        "name": {"eng": "irrealis", "jpn": "未然形"},
        "1": ".あ",
        "2": ".",
        "k": "来｜こ",
    },
    "cont": {"name": {"eng": "continuative", "jpn": "連用形"}},
    "terminal": {"name": {"eng": "terminal", "jpn": "終止形"}},
    "attributive": {"name": {"eng": "attributive", "jpn": "連体形"}},
    "hyp": {"name": {"eng": "hypothetical", "jpn": "仮定形"}},
    "imperative": {"name": {"eng": "imperative", "jpn": "命令形"}},
}

verb_conjugations = [
    {
        "name": {"eng": "polite imperfective"},
        "form": {
            "1": ["cont", "ます"],
            "2": ["cont", "ます"],
            "k": ["来｜き", "ます"],
            "s": ["し", "ます"],
        },
        "features": {"Polite": "Form", "Aspect": "Imp"},
    },
    {
        "name": {"eng": "plain perfective"},
        "form": {
            "1": ["cont", "た"],
            "2": ["cont", "た"],
            "k": ["来｜き", "た"],
            "s": ["し", "た"],
        },
        "features": {"Polite": "Infm", "Aspect": "Perf"},
    },
    {
        "name": {"eng": "plain negative imperfective"},
        "form": {
            "1": ["irrealis", "ない"],
            "2": ["irrealis", "ない"],
            "k": ["irrealis", "ない"],
            "s": ["し", "ない"],
        },
        "features": {"Polarity": "Neg", "Aspect": "Imp", "Polite": "Infm"},
    },
    {
        "name": {"eng": "plain negative perfective"},
        "form": {
            "1": ["irrealis", "なかった"],
            "2": ["irrealis", "なかった"],
            "k": ["irrealis", "なかった"],
            "s": ["し", "なかった"],
        },
        "features": {"Polarity": "Neg", "Aspect": "Perf", "Polite": "Infm"},
    },
    {
        "name": {"eng": "-te form"},
        "form": {"all": ["cont", "て"]},
        "features": {"VerbForm": "Ger"},
    },
    {
        "name": {"eng": "provisional conditional"},
        "form": {"all": ["hyp", "ば"]},
        "features": {"Mood": "Cnd"},
    },
    {
        "name": {"eng": "past conditional"},
        "form": {"all": ["cont", "たら"]},
        "features": {"Mood": "Cnd", "Tense": "Past"},
    },
    {
        "name": {"eng": "volitional"},
        "form": {
            "1": ["irrealis", "う"],
            "2": ["irrealis", "よう"],
            "k": ["irrealis", "よう"],
            "s": ["し", "よう"],
        },
        "features": {"Mood": "Opt"},
    },
    {
        "name": {"eng": "passive"},
        "form": {
            "1": ["irrealis", "れる"],
            "2": ["irrealis", "られる"],
            "k": ["irrealis", "られる"],
            "s": ["さ", "れる"],
        },
        "features": {"Voice": "Pass"},
    },
    {
        "name": {"eng": "causative"},
        "form": {
            "1": ["irrealis", "せる"],
            "2": ["irrealis", "させる"],
            "k": ["irrealis", "させる"],
            "s": ["さ", "せる"],
        },
        "features": {"Case": "Cau"},
    },
    {
        "name": {"eng": "potential"},
        "form": {
            "1": ["hyp", "る"],
            "2": ["irrealis", "られる"],
            "k": ["irrealis", "られる"],
            "s": ["出来｜でき", "る"],
        },
        "features": {"Mood": "Pot"},
    },
]


class JapaneseParser(PipelineAnnotator):
    def __init__(self):
        super().__init__()

        self.nlp = spacy.load("ja_core_news_md")

        self.japanese_punctuation = [
            "？",
            "！",
            "。",
            "、",
            "「",
            "」",
            "『",
            "』",
            "＜",
            "＞",
            "・",
        ]

        # TODO: Add all relevant number reading information to number tokens
        self.add_pipe(self.spacy_tokenize)
        self.add_pipe(combine_numbers)
        self.add_pipe(self._combine_letters)
        self.add_pipe(self._combine_verbs)
        self.add_pipe(self.clean_mecab_data)

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.Japanese]

    def spacy_tokenize(self, text: Text, tokenized: TokenizedDocument) -> None:
        for token in self.nlp(text.text):
            pos: PartOfSpeech

            poses: List[str] = []

            if len(token.pos_) > 0:
                poses.append(token.pos_)

                # Add extra POSes for dictionary lookup later
                if token.pos_ == "PROPN":
                    pos = PartOfSpeech.ProperNoun
                elif token.pos_ == "SCONJ":
                    pos = PartOfSpeech.SubordinatingConjunction
                elif token.pos_ == "CCONJ":
                    pos = PartOfSpeech.CoordinatingConjunction
                elif token.pos_ in ["ADP", "AUX"] and token.text in [
                    "が",
                    "で",
                    "と",
                    "に",
                    "の",
                    "は",
                    "も",
                    "を",
                ]:
                    pos = PartOfSpeech.Particle
                else:
                    pos = PartOfSpeech(token.pos_)

            print(pos)

            if pos is PartOfSpeech.Punctuation:
                if token.text in self.japanese_punctuation:
                    tokenized.tokens.append(PunctuationToken(token.text))

                elif (
                    token.text in punctuation_sticks_left
                    or token.text in punctuation_sticks_right
                ):
                    tokenized.tokens.append(
                        PunctuationToken(
                            text=token.text,
                            sticks_left=(token.text in punctuation_sticks_left),
                            sticks_right=(token.text in punctuation_sticks_right),
                        )
                    )
                elif len(token.text) == 1 and (
                    token.text.islower() or token.text.isupper()
                ):
                    tokenized.tokens.append(LetterToken(token.text))
                else:
                    logging.debug("Unhandled punctuation %s" % (token.text))
                    tokenized.tokens.append(PunctuationToken(token.text))
            elif pos is PartOfSpeech.Symbol:
                tokenized.tokens.append(PunctuationToken(token.text))
            elif pos is PartOfSpeech.Number:
                tokenized.tokens.append(NumberToken(token.text))
            elif pos is PartOfSpeech.Particle:
                tokenized.tokens.append(
                    WordToken(
                        language=LanguageCode.Japanese,
                        text=token.text,
                        lemma=token.text,
                        pos=pos,
                    )
                )
            else:
                tokenized.tokens.append(
                    WordToken(
                        language=LanguageCode.Japanese,
                        text=token.text,
                        lemma=token.lemma_,
                        pos=pos,
                        tags=self._parse_mecab_tag_string(token.tag_),
                    )
                )

    def clean_mecab_data(self, text: Text, tokenized: TokenizedDocument) -> None:
        for token in tokenized.tokens:
            if isinstance(token, WordToken):
                katakana = self._try_if_lemma_is_katakanago(token.lemma)

                if katakana:
                    token.lemma = katakana

                lemma = self._try_if_lemma_is_coded(token.lemma)

                if lemma:
                    token.lemma = lemma

    def _combine_letters(self, text: Text, tokenized: TokenizedDocument) -> None:
        combined_tokens: List[Token] = []

        combined_letters: Optional[str] = None

        for token in tokenized.tokens:
            if isinstance(token, LetterToken):
                if combined_letters is None:
                    combined_letters = token.letter
                elif token.letter.islower() or (
                    token.letter.isupper() and combined_letters[-1].isupper()
                ):
                    combined_letters += token.letter
                else:
                    combined_tokens.append(
                        WordToken(
                            combined_letters,
                            LanguageCode.Japanese,
                            combined_letters,
                            PartOfSpeech.Nil,
                            [],
                        )
                    )

                    combined_letters = token.letter
            else:
                if combined_letters is not None:
                    combined_tokens.append(
                        WordToken(
                            combined_letters,
                            LanguageCode.Japanese,
                            combined_letters,
                            PartOfSpeech.Nil,
                            [],
                        )
                    )
                    combined_letters = None

                combined_tokens.append(token)

        if combined_letters is not None:
            combined_tokens.append(
                WordToken(
                    combined_letters,
                    LanguageCode.Japanese,
                    combined_letters,
                    PartOfSpeech.Nil,
                    [],
                )
            )

        tokenized.tokens = combined_tokens

    def _combine_verbs(self, text: Text, tokenized: TokenizedDocument) -> None:
        if len(tokenized.tokens) == 0:
            return

        combined_tokens: List[Token] = []

        current_verb: List[Morpheme] = []

        for token in tokenized.tokens:
            if isinstance(token, WordToken):
                if (
                    token.pos is PartOfSpeech.Auxiliary
                    or token.pos is PartOfSpeech.Verb
                ):
                    current_verb.append(
                        Morpheme(text=token.text, lemma=token.lemma, features={})
                    )
                elif len(current_verb) > 0 and token.text in [
                    "た",
                    "て",
                    "い",
                    "られ",
                    "れ",
                    "せ",
                    "まし",
                    "ます",
                ]:
                    current_verb.append(
                        Morpheme(text=token.text, lemma=token.lemma, features={})
                    )
                else:
                    if len(current_verb) > 0:
                        combined_tokens.append(
                            self._create_new_word_from_morphemes(current_verb)
                        )
                        current_verb = []

                    combined_tokens.append(token)
            else:
                if len(current_verb) > 0:
                    combined_tokens.append(
                        self._create_new_word_from_morphemes(current_verb)
                    )
                    current_verb = []

                combined_tokens.append(token)

        if len(current_verb) > 0:
            combined_tokens.append(self._create_new_word_from_morphemes(current_verb))

        tokenized.tokens = combined_tokens

    def _create_new_word_from_morphemes(self, morphemes: List[Morpheme]):
        word_text = "".join(map(lambda x: x.text, morphemes))

        return WordToken(
            text=word_text,
            language=LanguageCode.Japanese,
            pos=PartOfSpeech.Verb,
            morphemes=morphemes,
            lemma=morphemes[0].lemma,
        )

    def _try_if_lemma_is_coded(self, word) -> Optional[str]:
        coded_lemma_regex = r"^(\w+)-(\w+.*)$"

        match = re.match(coded_lemma_regex, word)

        if match is None:
            return None
        elif match.group(2) == "助数詞":
            return match.group(1)
        else:
            logging.warning("[MeCab] Unhandled coded lemma: %s" % (word))

            return None

    def _try_if_lemma_is_katakanago(self, word: str) -> Optional[str]:
        katakana_english_regex = r"^([\u30A0-\u30FF]+)-(\w+.*)$"

        match = re.match(katakana_english_regex, word)

        if match is None:
            return None
        else:
            return match.group(1)

    def _unhandled_tag(self, tag: Union[List[str]]) -> None:
        logging.warning("[MeCab] Unhandled tag %s" % (tag))

        raise NotImplementedError("Japanese POS tag %s" % (tag))

    def _parse_mecab_tag_string(self, string: str) -> List[str]:
        tag = re.split(r"[,-]", string)

        tags: List[str] = []

        if len(tag) == 0:
            return []

        if tag[0] == "_SP":
            pass
        elif tag[0] == "空白":
            pass
        elif tag[0] == "名詞":  # Noun. pos:NOUN?
            if tag[1] == "普通名詞":  # Common noun
                if tag[2] == "一般":
                    pass
                elif tag[2] == "副詞可能":  # Possible adverbial
                    pass
                elif tag[2] == "助数詞可能":  # Possible counter
                    # TODO: Mark as possible counter
                    tags.append("Counter?")
                    pass
                elif tag[2] == "サ変可能":  # Possible irregular s-stem verb
                    pass
                elif tag[2] == "形状詞可能":  # Possible shape word
                    pass
                elif tag[2] == "サ変形状詞可能":
                    pass
                else:
                    self._unhandled_tag(tag)
            elif tag[1] == "数詞":
                # TODO: Mark as number if necessary
                pass
            elif tag[1] == "固有名詞":
                if tag[2] == "一般":
                    # TODO: Uncategorized name. Do some checking
                    # Could be foreign (katakana) name
                    pass
                elif tag[2] == "地名":
                    # TODO: Mark as place name
                    tags.append("Name")
                    if tag[3] == "一般":
                        pass
                    elif tag[3] == "国":
                        # TODO: Mark as country name
                        tags.append("Country Name")
                    else:
                        self._unhandled_tag(tag)
                elif tag[2] == "人名":
                    tags.append("Name")
                    tags.append("Person Name")
                    if tag[3] == "一般":
                        # Could be katakana/foreign name
                        pass
                    elif tag[3] == "名":
                        tags.append("First Name")
                    elif tag[3] == "姓":
                        tags.append("Last Name")
                    else:
                        self._unhandled_tag(tag)
                else:
                    self._unhandled_tag(tag)
            elif tag[1] == "助動詞語幹":
                pass
            else:
                self._unhandled_tag(tag)
        elif tag[0] == "動詞":
            if tag[1] == "一般":
                pass
            elif tag[1] == "非自立可能":  # Possible dependent(?) verb
                # TODO: This might be where to reconcile 〜いる verbs
                pass
            else:
                self._unhandled_tag(tag)
        elif tag[0] == "形容詞":  # Adjective
            if tag[1] == "一般":
                pass
            elif tag[1] == "非自立可能":
                pass
            else:
                self._unhandled_tag(tag)
        elif tag[0] == "副詞":  # Adverb. pos:ADV?
            pass
        elif tag[0] == "代名詞":  # Pronoun
            pass
        elif tag[0] == "助詞":  # Particle. pos:ADP?
            # TODO: Mark as particle for looking up words?
            if tag[1] == "係助詞":  # かかりじょし Binding/linking particle
                pass
            elif tag[1] == "格助詞":  # Case-marking particle (が の を に)
                pass
            elif tag[1] == "接続助詞":  # pos:SCONJ?
                # TODO: Includes "が" which isn't handled correctly; SCONJ
                # TODO: For JMDict lookup, add CONJ to CCONJ and SCONJ words
                pass
            elif tag[1] == "準体助詞":  # Attaches to phrase
                # pos:SCONJ?
                pass
            elif tag[1] == "副助詞":  # Adverbial particle
                pass
            elif tag[1] == "終助詞":  # Sentence ending particle
                pass
            else:
                self._unhandled_tag(tag)
        elif tag[0] == "助動詞":  # Auxiliary verb. pos:AUX?
            # TODO: Includes "です". Does this get handled correctly?
            pass
        elif tag[0] == "連体詞":  # Pre-noun adjectival. pos:DET?
            pass
        elif tag[0] == "形状詞":  # Shape(?) word. pos:ADJ?
            if tag[1] == "一般":
                pass
            elif tag[1] == "助動詞語幹":  # Auxiliary stem
                pass
            else:
                self._unhandled_tag(tag)
        elif tag[0] == "接続詞":  # Conjunction
            pass
        elif tag[0] == "接頭辞":  # Prefix
            # TODO: Mark prefix
            pass
        elif tag[0] == "接尾辞":  # Suffix
            tags.append("PART")
            if tag[1] == "名詞的":  # Substantive
                if tag[2] == "一般":  # pos:NOUN?
                    pass
                elif tag[2] == "助数詞":  # pos:NOUN
                    # TODO: Mark counter
                    pass
                elif tag[2] == "副詞可能":  # Possibly adverbial
                    pass
                elif tag[2] == "サ変可能":
                    pass
                else:
                    self._unhandled_tag(tag)
            elif tag[1] == "形容詞的":  # Adjectival
                pass
            elif tag[1] == "形状詞的":  # Shape
                pass
            elif tag[1] == "動詞的":  # Verbial
                pass
            else:
                self._unhandled_tag(tag)
        elif tag[0] == "感動詞":  # Interjection. pos:INTJ?
            # TODO: Go through interjections
            if tag[1] == "一般":
                pass
            elif tag[1] == "フィラー":  # Filler word
                # TODO: Mark filler word
                pass
            else:
                self._unhandled_tag(tag)
        elif tag[0] == "補助記号":  # Supplementary symbol. pos:PUNCT?
            if tag[1] == "一般":
                # TODO: Handle special cases such as '…'
                pass
            elif tag[1] == "句点":  # Period/full stop
                # TODO: Mark as period
                pass
            elif tag[1] == "読点":  # Comma
                # TODO: Mark as comma
                pass
            elif tag[1] == "括弧開":  # Opening bracket
                tags.append("Opening Bracket")
            elif tag[1] == "括弧閉":  # Closing bracket
                tags.append("Closing Bracket")
            else:
                self._unhandled_tag(tag)
        elif tag[0] == "記号":  # Symbol
            # TODO: Go through all symbols and mark to relieve postprocess
            if tag[1] == "一般":
                pass
            elif tag[1] == "文字":  # Latin character?
                # TODO: Candidate for recombining capitalized letters?
                pass
            else:
                self._unhandled_tag(tag)
        else:
            self._unhandled_tag(tag)

        return tags
