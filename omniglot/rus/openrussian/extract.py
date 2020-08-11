from typing import Optional


def extract_number(value: str) -> int:
    if value is None or not value.isdecimal():
        raise ValueError("Expected a number %s" % (value))
    else:
        return int(value)


def extract_optional_number(value: Optional[str]) -> Optional[int]:
    if value is None or len(value) == 0:
        return None
    elif not value.isdecimal():
        raise ValueError("Expected value to be a number\n%s" % (value))
    else:
        return int(value)


def extract_boolean(text: str) -> bool:
    if not text.isdecimal():
        raise ValueError("Expected 0 or 1 value\n%s" % (text))
    elif int(text) == 0:
        return False
    elif int(text) == 1:
        return True
    else:
        raise ValueError("Expected 0 or 1 value\n%s" % (text))


def extract_optional_boolean(text: Optional[str]) -> Optional[bool]:
    if text is None or len(text) == 0:
        return None
    else:
        return extract_boolean(text)


def extract_optional_string(text: Optional[str]) -> Optional[str]:
    if text is None or len(text) == 0:
        return None
    else:
        return text


def extract_string(text: str) -> str:
    if text is None or len(text) == 0:
        raise ValueError("Expected a string\n%s" % (text))
    else:
        return text
