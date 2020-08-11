import re


def replace_tag_strings(xml: str) -> str:
    return re.sub(r"\&(.*)\;", r"\1", xml)
