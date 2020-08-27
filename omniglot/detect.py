from collections import defaultdict
from typing import Dict, Optional

import pycld2

from omnilingual import Language, LanguageCode
from omnilingual.ietf.tag import IetfComponents


def guess_language(text: str, language_hint: Optional[Language] = None) -> Language:
    if language_hint is not None and language_hint.code != LanguageCode.Undetermined:
        is_reliable, _, details = pycld2.detect(
            text,
            hintLanguage=language_hint.ietf_tag(
                IetfComponents(script=True), alpha_3=False
            ),
        )
    else:
        is_reliable, _, details = pycld2.detect(text, bestEffort=True)

    detected_languages: Dict[str, int] = defaultdict(int)

    highest_language: str = "und"
    highest_score: int = 0

    for name, code, percent, score in details:
        detected_languages[code] += percent

        if detected_languages[code] > highest_score:
            highest_score = detected_languages[code]
            highest_language = code

    return Language.where(tag=highest_language)
