import re
from typing import Dict, List, Optional

from bs4 import BeautifulSoup, NavigableString, Tag

from omniglot.lexeme import Lexeme

from pydantic import BaseModel

from enum import Enum


class LandmarkNotFoundError(Exception):
    pass


class ExpectedTagNotFoundError(Exception):
    pass


class MissingDefinitionError(Exception):
    pass


class HawaiianPOS(Enum):
    hamani = "ham"
    hehele = "heh"
    a = "ʻaʻ"
    kikino = "kik"
    ioa = "iʻoa"


class MamakaEntry(BaseModel):
    head: str
    syllables: str

    pos: Optional[HawaiianPOS]

    dictionary: bool

    literally: Optional[str]

    definition: str

    see: Optional[List[str]]
    also: Optional[List[str]]
    compare: Optional[List[str]]

    examples: Optional[Dict[str, str]]

    shortened: Optional[List[str]]
    combined: Optional[List[str]]

    english: bool = False
    japanese: bool = False


separator = "·"

abbreviations = {
    "abb.": "abbreviation",
    "Bib.": "Bible",
    "cf.": "compare",
    "comb.": "combined form",
    "dic.": "dictionary definition",
    "e.g.": "for example",
    "Eng.": "English",
    "ext. mng.": "extended meaning",
    "i.e.": "that is",
    "inv.": "invention",
    "Japn.": "Japanese",
    "lit.": "literally",
    "mān.": "mānaleo (native speaker)",
    "new mng.": "new meaning",
    "PPN": "Proto Polynesian",
    "redup.": "reduplication",
    "sh.": "shortened form",
    "sp. var.": "spelling variation",
    "Tah.": "Tahitian",
    "trad.": "traditional literary sources",
    "var.": "variation",
    "ham": "hamani (transitive verb)",
    "heh": "hehele (intransitive verb)",
    "ʻaʻ": "ʻaʻano (stative verb)",
    "kik": "kikino (common noun)",
    "iʻoa": "iʻoa (proper noun)",
}

hawaiian_parts_of_speech = ["ham", "heh", "ʻaʻ", "kik", "iʻoa"]


HEAD_REGEX = r"<span\s+class\s*=\s*\"head\">(?P<head>.*)</span>"


def remove_dic(line):
    new, subs = re.subn(r"<i>dic\.</i>", "", line, flags=re.IGNORECASE)
    if subs > 0:
        return new

    new, subs = re.subn(r"dic\./", "", line, flags=re.IGNORECASE)
    if subs > 0:
        return new

    new, subs = re.subn(r"dic\.,", "", line, flags=re.IGNORECASE)
    if subs > 0:
        return new

    return line


def find_start_of_section_with_title(soup: BeautifulSoup, title: str) -> BeautifulSoup:
    for tag in soup.find_all("i", text=title):
        if tag.parent.name == "h1":
            start = tag.find_parent("table")
            break

    if start is None:
        raise LandmarkNotFoundError("Could not find the start of the %s part" % title)

    return start


def extract_part(head_element: BeautifulSoup, end_tag: str, end_text: str) -> str:
    extracted_part = ""

    for element in head_element.next_siblings:
        if element.name == "table" and element.find(end_tag, text=end_text):
            return extracted_part
        else:
            extracted_part += str(element)

    raise LandmarkNotFoundError(
        "Could not find the %s:%s that marks the section's end" % (end_tag, end_text)
    )


def extract_hawaiian_english_part(head_element: BeautifulSoup) -> str:
    return extract_part(head_element, "i", " English-Hawaiian")


def remove_unnecessary_whitespace(line: str) -> str:
    return re.sub(r"\s+", " ", line).strip()


def normalize_tags(line: str) -> str:
    # Special case
    return line.replace("ʻ<i>a</i>ʻ", "<i>ʻaʻ</i>")


def parse_entry(entry: BeautifulSoup) -> MamakaEntry:
    if len(entry.contents) == 0:
        raise ExpectedTagNotFoundError("Expected entry to have contents")

    current_element = entry.contents[0]

    if not (current_element.name == "span" and "head" in current_element["class"]):
        raise ExpectedTagNotFoundError("Expected to find :head <span>", current_element)

    head_syllables = re.sub(r"  +", " ", current_element.string)
    head_phrase = head_syllables.replace("·", "")

    pos: Optional[HawaiianPOS] = None
    is_dictionary_definition = False
    literally: Optional[str] = None

    definition: Optional[str] = None

    also: Optional[List[str]] = None
    compare: Optional[List[str]] = None

    examples: Optional[Dict[str, str]] = None

    references: Optional[List[str]] = None

    combined: Optional[List[str]] = None

    current_element = current_element.next_sibling

    english: bool = False
    japanese: bool = False

    while current_element is not None:
        if isinstance(current_element, Tag):
            if current_element.name == "i":
                if current_element.string in hawaiian_parts_of_speech:
                    pos = HawaiianPOS(current_element.string)
                    current_element = current_element.next_sibling
                elif "Dic." in current_element.string:
                    is_dictionary_definition = True
                    current_element = current_element.next_sibling
                elif "Lit.," in current_element.string:
                    literally = current_element.next_sibling.string.strip(
                        ".\n "
                    ).strip()

                    current_element = current_element.next_sibling.next_sibling
                elif "Eng." in current_element.string:
                    english = True
                    current_element = current_element.next_sibling
                elif isinstance(current_element.next_sibling, NavigableString):
                    if examples is None:
                        examples = {}

                    examples[
                        current_element.string.strip().rstrip(".")
                    ] = current_element.next_sibling.string.strip().rstrip(".")

                    current_element = current_element.next_sibling.next_sibling
                else:
                    raise NotImplementedError("<i>", current_element)
            else:
                raise NotImplementedError(current_element)
        elif isinstance(current_element, NavigableString):
            text = current_element.string.strip()

            if len(text) == 0:
                current_element = current_element.next_sibling
                continue
            elif definition is None:
                if text.endswith("Also"):
                    definition = text[:-4]

                    also = [current_element.next_sibling.string.rstrip(".")]
                    current_element = current_element.next_sibling.next_sibling
                elif text.endswith("Comb."):
                    definition = text[:-5]

                    combined = [
                        s.strip()
                        for s in current_element.next_sibling.string.strip()
                        .rstrip(".")
                        .split("+")
                    ]

                    current_element = current_element.next_sibling.next_sibling
                else:
                    definition = text

                    current_element = current_element.next_sibling
            elif "See" in current_element.string:
                references = [
                    reference.strip()
                    for reference in current_element.next_sibling.string.strip()
                    .rstrip(".")
                    .split(",")
                ]

                current_element = current_element.next_sibling.next_sibling
            elif "Cf." in current_element.string:
                if current_element.next_sibling.name == "i":
                    cf_element = current_element.next_sibling
                    next_string = cf_element.string

                    strings = [s.strip() for s in next_string.split(".") if len(s) > 0]

                    print(strings)

                    if compare is None:
                        compare = []

                    compare.extend(
                        [comparison.strip() for comparison in strings[0].split(",")]
                    )

                    if len(strings) > 1:
                        for sub_string in strings[1:-1]:
                            raise NotImplementedError("Substrings")

                        if isinstance(cf_element.next_sibling, NavigableString,):
                            if examples is None:
                                examples = {}

                            examples[
                                strings[-1].strip()
                            ] = cf_element.next_sibling.string.strip().rstrip(".")

                            current_element = cf_element.next_sibling.next_sibling
                        else:
                            print(cf_element.next_sibling.name)
                            raise NotImplementedError("Navigable")
                    else:
                        current_element = cf_element.next_sibling

                else:
                    raise ExpectedTagNotFoundError("Not <i>")

            else:
                raise NotImplementedError("Other NavigableString")
        else:
            print("Unexpected")
            raise NotImplementedError(current_element)

    if definition is None:
        raise MissingDefinitionError()

    return MamakaEntry(
        head=head_phrase,
        syllables=head_syllables,
        pos=pos,
        dictionary=is_dictionary_definition,
        literally=literally,
        definition=definition.strip().rstrip("."),
        also=also,
        see=references,
        compare=compare,
        combined=combined,
        examples=examples,
        english=english,
        japanese=japanese,
    )


def parse_dictionary(html: str) -> List[Lexeme]:
    soup = BeautifulSoup(html, "lxml")

    hawaiian_english_start = find_start_of_section_with_title(soup, "Hawaiian-English")

    hawaiian_english_section = BeautifulSoup(
        extract_hawaiian_english_part(hawaiian_english_start), "lxml"
    )

    # First ammend broken up entries
    entries: List[BeautifulSoup] = []

    for entry_tag in hawaiian_english_section.find_all(
        "p", {"align": re.compile(r"justify", re.IGNORECASE)}
    ):
        head = entry_tag.find("span", {"class": re.compile(r"head", re.IGNORECASE)})

        if head is not None:
            entries.append(entry_tag)
            # print(head.string)
        else:
            entries[-1].append(entry_tag)

    for tag in entries:
        parse_entry(tag)

    return []
