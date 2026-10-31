class InvalidDataError(Exception):
    """Raised when data is invalid"""
    pass


class IndexMismatchError(Exception):
    """Raised when amount of values is not equal to amount of indexes"""
    pass


class DuplicateKeyError(Exception):
    """Raised when arg keys consist key duplicates"""

    def __init__(self, keys):
        seen = set()
        multiple_keys = set()

        for key in keys:
            if key in seen:
                multiple_keys.add(key)
            else:
                seen.add(key)

        duplicates = []
        if multiple_keys:
            for key in keys:
                if key in multiple_keys and key not in duplicates:
                    duplicates.append(key)

        self.duplicates = duplicates
