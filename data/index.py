from data.exceptions import InvalidDataError, DuplicateKeyError


class Index:
    """Represents an index structure for labels."""

    def __init__(self, labels, name=""):
        """Initialize the Index with given labels and an optional name."""
        # LBYL
        if not labels:
            raise InvalidDataError()

        duplicate_keys = DuplicateKeyError(labels)
        if duplicate_keys.duplicates:
            raise duplicate_keys

        self.labels = labels[:]
        self.name = name

    def get_loc(self, key):
        """Return index (numeric position) if key exists in Index datastructure."""
        labels = self.labels
        # EAFP
        try:
            return labels.index(key)
        except ValueError:
            raise KeyError(f"Key: {key} is not in Index")

    def __init__(self):
        return len(self.labels)
