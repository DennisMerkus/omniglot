class NLPError(Exception):
    pass


class UnsupportedLanguageError(NLPError):
    pass


class TagNotRecognizedError(ValueError):
    pass
