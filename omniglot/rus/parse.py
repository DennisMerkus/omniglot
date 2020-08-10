from typing import List, Optional

import pymorphy2
from pymorphy2.tagset import OpencorporaTag
from spacy.lang.ru import Russian as SpacyRussian

from omnilingual import LanguageCode, PartOfSpeech
from documental import Text, Tokens

from omnilingual.features import (
    Animacy,
    Aspect,
    Case,
    Features,
    Gender,
    Mood,
    Number,
    Person,
    Tense,
    Voice,
)
from omniglot.mul.numbers import combine_numbers
from omniglot.mul.punctuation import convert_punctuation_tokens
from omniglot.mul import remove_extra_whitespace

from ..parser import PipelineAnnotator
from ..tokens import WordToken


class RussianParser(PipelineAnnotator):
    def __init__(self):
        super().__init__()

        self.nlp = SpacyRussian()
        self.morphy = pymorphy2.MorphAnalyzer()

        self.add_pipe(self.tokenize)
        self.add_pipe(convert_punctuation_tokens)
        self.add_pipe(combine_numbers)
        self.add_pipe(remove_extra_whitespace)

    def supported_languages(self) -> List[LanguageCode]:
        return [LanguageCode.Russian]

    def tokenize(self, text: Text, tokenized: Tokens) -> None:
        for token in self.nlp(text.text):
            parse = self.morphy.parse(token.text)[0]

            tag: OpencorporaTag = parse.tag

            print(tag)

            word = WordToken(
                language=LanguageCode.Russian,
                text=token.text,
                lemma=parse.normal_form,
                pos=self.convert_pos(tag.POS),
                features=self.convert_features(tag),
            )

            tokenized.tokens.append(word)

    def convert_pos(self, pos: Optional[str]) -> PartOfSpeech:
        if pos is None:
            return PartOfSpeech.Nil
        elif pos == "NOUN":
            return PartOfSpeech.Noun
        elif pos in ["ADJF", "ADJS"]:
            return PartOfSpeech.Adjective
        elif pos == "COMP":
            return PartOfSpeech.Comparative
        elif pos in ["VERB", "INFN", "PRTF", "PRTS", "GRND"]:
            return PartOfSpeech.Verb
        elif pos == "NUMR":
            return PartOfSpeech.Number
        elif pos == "ADVB":
            return PartOfSpeech.Adverb
        elif pos == "NPRO":
            return PartOfSpeech.Noun
        elif pos == "PRED":
            return PartOfSpeech.Predicate
        elif pos == "PREP":
            return PartOfSpeech.Adposition
        elif pos == "CONJ":
            return PartOfSpeech.Conjunction
        elif pos == "PRCL":
            return PartOfSpeech.Particle
        elif pos == "INTJ":
            return PartOfSpeech.Interjection
        else:
            raise NotImplementedError("Unexpected Russian POS tag %s" % (pos))

    def convert_features(self, tag: OpencorporaTag) -> Features:
        animacy: Optional[Animacy] = None
        aspect: Optional[Aspect] = None
        case: Optional[Case] = None
        gender: Optional[Gender] = None
        mood: Optional[Mood] = None
        number: Optional[Number] = None
        person: Optional[Person] = None
        tense: Optional[Tense] = None
        voice: Optional[Voice] = None

        if tag.animacy == "anim":
            animacy = Animacy.Anim
        elif tag.animacy == "inan":
            animacy = Animacy.Inan

        if tag.aspect == "perf":
            aspect = Aspect.Perf
        elif tag.aspect == "impf":
            aspect = Aspect.Imp

        if tag.case == "nomn":
            case = Case.Nom
        elif tag.case in ["gent", "gen1", "gen2"]:
            case = Case.Gen
        elif tag.case == "datv":
            case = Case.Dat
        elif tag.case in ["accs", "acc1", "acc2"]:
            case = Case.Acc
        elif tag.case == "ablt":
            case = Case.Abl
        elif tag.case in ["loct", "loc1", "loc2"]:
            case = Case.Loc
        elif tag.case == "voct":
            case = Case.Voc

        if tag.gender == "masc":
            gender = Gender.Masc
        elif tag.gender == "femn":
            gender = Gender.Fem
        elif tag.gender == "neut":
            gender = Gender.Neut

        if tag.involvement is not None:
            pass

        if tag.mood is not None:
            if tag.mood == "indc":
                mood = Mood.Ind
            elif tag.mood == "impr":
                mood = Mood.Imp

        if tag.number is not None:
            if tag.number == "sing":
                number = Number.Sing
            elif tag.number == "plur":
                number = Number.Plur

        if tag.person == "1per":
            person = Person.First
        elif tag.person == "2per":
            person = Person.Second
        elif tag.person == "3per":
            person = Person.Third

        if tag.tense == "pres":
            tense = Tense.Pres
        elif tag.tense == "past":
            tense = Tense.Past
        elif tag.tense == "futr":
            tense = Tense.Fut

        if tag.transitivity is not None:
            # TODO
            pass

        if tag.voice == "actv":
            voice = Voice.Act
        elif tag.voice == "pssv":
            voice = Voice.Pass

        return Features(
            Animacy=animacy,
            Aspect=aspect,
            Case=case,
            Gender=gender,
            Mood=mood,
            Number=number,
            Person=person,
            Tense=tense,
            Voice=voice,
        )
